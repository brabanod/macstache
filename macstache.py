import pystache
import sys
import os
import json
import argparse

# Location: /usr/local/bin




# Check command line arguments
parser = argparse.ArgumentParser(description="macstache, Version 0.1, Pascal Braband 2019")

parser.add_argument("template", type=str, help="File containing mustache template")
parser.add_argument("data", type=str, help="File containing mustache hash variables in .json format")
parser.add_argument("output", type=str, help="Location of the file, where output should be saved")

parser.add_argument('-ps', '--partial-subfolder', action='store_true', help='Activate subfolder replacement for partials')

args = parser.parse_args()




# Compose paths
templatePathRaw = args.template
dataPathRaw = args.data
outputPathRaw = args.output

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




# Partial subfolder replacement
if args.partial_subfolder:
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