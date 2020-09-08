//
//  main.swift
//  macstache
//
//  Created by Pascal Braband on 08.09.20.
//  Copyright © 2020 Pascal Braband. All rights reserved.
//

import Foundation
import ArgumentParser
import Yams
import Mustache

struct macstache: ParsableCommand {
    @Option(name: [.short, .customLong("template")], help: "The .mustache template file.")
    var templateFile: String
    
    @Option(name: [.short, .customLong("context")], parsing: .upToNextOption, help: "One/Multiple .json or .yaml file containing the context for the texmplate. If one (or more) folder is given, all .json and .yaml files from that folder will be used.")
    var contextFiles: [String]
    
    @Option(name: [.short, .customLong("output")], help: "Name of the generated output file.", completion: nil)
    var outputFile: String
    
    
    mutating func run() throws {
        let templatePath = templateFile.toURL()
        let contextPaths = contextFiles.map({ $0.toURL() })
        let outputPath = outputFile.toURL()
        
        var contextData = [String: Any]()
        
        do {
            // Read Context
            for contextPath in contextPaths {
                var isDir : ObjCBool = false
                
                // Check if path exists
                if FileManager.default.fileExists(atPath: contextPath.path, isDirectory:&isDir) {
                    // Check if path is a directory
                    if isDir.boolValue {
                        // Iterate over all files in the directory
                        if let enumerator = FileManager.default.enumerator(at: contextPath, includingPropertiesForKeys: [.isRegularFileKey], options: [.skipsHiddenFiles, .skipsPackageDescendants]) {
                            for case let fileURL as URL in enumerator {
                                do {
                                    let fileAttributes = try fileURL.resourceValues(forKeys:[.isRegularFileKey])
                                    if fileAttributes.isRegularFile! {
                                        // Read contents and join them to one combined dictionary
                                        contextData.merge(try extractContents(from: fileURL), uniquingKeysWith: {(current,_) in current})
                                    }
                                } catch {
                                    print(error, fileURL)
                                }
                            }
                        }
                    } else {
                        // Only read contents from the file at path
                        contextData = try extractContents(from: contextPath)
                    }
                } else {
                    throw RuntimeError("The path \(contextPath.path) does not exist.")
                }
            }
            
            
            // Generate Output
            
            // Create template from templatePath
            let template = try Template(URL: templatePath)
            
            // Render output
            let output = try template.render(contextData)
            
            
            // Write Output
            try output.write(to: outputPath, atomically: false, encoding: .utf8)
            
        } catch let error {
            Self.exit(withError: error)
        }
    }
    
    
    func extractContents(from path: URL) throws -> [String: Any] {
        let contents = try String(contentsOf: path, encoding: .utf8)
        guard let data = contents.data(using: .utf8) else { throw RuntimeError("Couldn't read file \(path.path).") }
        var dataDictonary: [String: Any]!
        
        switch path.pathExtension {
        case "json":
            dataDictonary = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any]
        case "yaml":
            dataDictonary = try Yams.load(yaml: contents) as? [String: Any]
        case "plist":
            dataDictonary = try! PropertyListSerialization.propertyList(from:data, format: nil) as! [String:Any]
        default:
            throw RuntimeError("Unrecognized context file extension \(path.pathExtension) for \(path.path). Files must be .json, .yaml or .plist.")
        }
        
        return dataDictonary
    }
}

macstache.main()




extension String {
    
    /**
     Creates a URL from the String and appends the current working directory, if the path itself does not start with the root directory (i.e. "/")
     */
    func toURL() -> URL {
        if self.hasPrefix("/") {
            return URL(fileURLWithPath: self)
        } else {
            return URL(fileURLWithPath: FileManager.default.currentDirectoryPath + "/" + self)
        }
    }
}




struct RuntimeError: Error {
    let message: String

    init(_ message: String) {
        self.message = message
    }

    public var localizedDescription: String {
        return message
    }
}
