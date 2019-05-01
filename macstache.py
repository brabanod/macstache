import pystache
import sys
import os
import json

# Location: /usr/local/bin




# Check command line arguments
if len(sys.argv) == 2:
    if (sys.argv[1] == "-h") or (sys.argv[1] == "-help") or (sys.argv[1] == "--help"):
        print("""
        
macstache, Version 0.1, Pascal Braband 2019

To compile, give macstache 3 files in the following order:
    - Template: contains mustache template
    - Context: contains mustach hash variables in .json format
    - Output: location of the file, where output should be saved
    
More commands:
    Type -h for help
    Type -v for version
            
            """)
        sys.exit(0)

    if (sys.argv[1] == "-v") or (sys.argv[1] == "-version") or (sys.argv[1] == "--version"):
        print("macstache, Version 0.1, Pascal Braband 2019")
        sys.exit(0)

    else:
        print("Invalid arguments, specify TEMPLATE, DATA and OUTPUT file. Type -h for help.")
        sys.exit(2)


elif len(sys.argv) != 4:
    print("Invalid arguments, specify TEMPLATE, DATA and OUTPUT file. Type -h for help.")
    sys.exit(2)




# Compose paths
templatePathRaw = sys.argv[1]
dataPathRaw = sys.argv[2]
outputPathRaw = sys.argv[3]

templatePath = os.path.join(os.getcwd(), templatePathRaw)
dataPath = os.path.join(os.getcwd(), dataPathRaw)
outputPath = os.path.join(os.getcwd(), outputPathRaw)

# Read file content
templateFile = open(templatePath, "r")
templateString = templateFile.read()
templateFile.close()

dataFile = open(dataPath, "r")
dataString = dataFile.read()
dataFile.close()




# Partial subfoldering
partialIndex = 0
while True:
    partialIndex = templateString.find("{{> ", partialIndex+1)
    if partialIndex == -1:
        break

    # Get path from partial
    partialStartIndex = partialIndex+4
    partialEndIndex = templateString.find("}}", partialIndex)
    partialPath = templateString[partialStartIndex: partialEndIndex]

    # Compose updated path to partial
    partialPathNew = os.path.join(os.path.dirname(templatePathRaw), partialPath)

    # Update template to include new path
    templateString = templateString[:partialStartIndex] + partialPathNew + templateString[partialEndIndex:]



# Convert JSON dataString to dictionary
context = json.loads(dataString)

# Generate output
output = pystache.render(templateString, context)


# Save output to file
outputFile = open(outputPath, "w")
outputFile.write(output)
outputFile.close()