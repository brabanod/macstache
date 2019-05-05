import pystache
import sys
import os
import json
import argparse

# Location: /usr/local/bin




# Check command line arguments
parser = argparse.ArgumentParser(description="macstache, Version 1.0, Pascal Braband 2019")

parser.add_argument("template", type=str, help="File containing mustache template")
parser.add_argument("data", type=str, help="File containing mustache hash variables in .json format")
parser.add_argument("output", type=str, help="Location of the file, where output should be saved")

args = parser.parse_args()




# Compose paths
templatePathRaw = args.template
dataPathRaw = args.data
outputPathRaw = args.output

templatePath = os.path.join(os.getcwd(), templatePathRaw)
dataPath = os.path.join(os.getcwd(), dataPathRaw)
outputPath = os.path.join(os.getcwd(), outputPathRaw)

# Change working directory to directory of template file
os.chdir(os.path.dirname(templatePath))

# Read file content
templateFile = open(templatePath, "r")
templateString = templateFile.read()
templateFile.close()

dataFile = open(dataPath, "r")
dataString = dataFile.read()
dataFile.close()




# Convert JSON dataString to dictionary
context = json.loads(dataString)

# Generate output
output = pystache.render(templateString, context)


# Save output to file
outputFile = open(outputPath, "w")
outputFile.write(output)
outputFile.close()