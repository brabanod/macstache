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
templatePath = os.path.join(os.getcwd(), sys.argv[1])
dataPath = os.path.join(os.getcwd(), sys.argv[2])
outputPath = os.path.join(os.getcwd(), sys.argv[3])


# Read file content
templateFile = open(templatePath, "r")
templateString = templateFile.read()
templateFile.close()

dataFile = open(dataPath, "r")
dataString = dataFile.read()
dataFile.close()


# Convert dataString JSON to dictionary
context = json.loads(dataString)


# Replace occurrences of file references with file's content
for key, value in context.items():
    if value[0] == "@":
        # Get path for sub file
        sub = value[1:]
        subPath = os.path.join(os.path.dirname(dataPath), sub)

        # Read contents of sub file
        subFile = open(subPath, "r")
        subString = subFile.read()
        subFile.close()

        # Replace value with contents of sub file
        context[key] = subString


# Generate output
output = pystache.render(templateString, context)


# Save output to file
outputFile = open(outputPath, "w")
outputFile.write(output)
outputFile.close()