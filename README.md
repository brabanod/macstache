<br></br>
<p align="center">
  <img src="https://github.com/brabanod/macstache/blob/master/resources/macstache.png?raw=true" alt="macstache" width="400"/>
</p>
<br></br>


# macstache
A [Mustache](https://mustache.github.io) command line tool implementation for Mac written in Python. Uses `.json`, `.yaml` or `.plist`  files to read hash values for Mustache.



# Installation

## Pre-Build
If you only want the command line tool, go to `dist` folder and grab the `macstache` executable. Copy it to a folder, which is part of your `$PATH`, for example `usr/local/bin`. The following commands should install macstache on macOS
```
git clone https://github.com/brabanod/macstache.git
sudo cp macstache/dist/macstache /usr/local/bin/macstache
```
After that, just use the tool by calling `macstache` in the terminal.


## Build yourself
If you want to build the binary yourself, you need to open the Xcode project, build the project, then open the produced binary in Finder and copy it to the location stated above. 



# Usage
After installing macstache (i.e. moving the executable to `/usr/local/bin`), you can start macstache on the terminal by calling `macstache`.


## Command Line Parameters
macstache needs 3 parameters as input, in order to compile the result
* **Template**: This file contains your template with Mustach tags, such as `{{name}}`
* **Context**: The context or data file is as a `.json`, `.yaml` or `.plist` file. This can be one or multiple files or you give it a directory, which will collect all the files from this directory and its subdirectories. If multiple files are used, they are combined to one large context to be used for the template. The files are parsed in the same order, in which they are given to macstache, so when files have the same keys, the current key-value-pair overrides the previous key-value-pair.
* **Output**: Specify the location, to where macstache should save the compiled output

Options:
* `-h`: Display help

An example command would look like this:
```
macstache -t source/index.mustache -c source/index.json -o build/index.html
```
