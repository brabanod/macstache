<br></br>
<p align="center">
  <img src="https://github.com/columbbus/macstache/blob/master/resources/macstache.png?raw=true" alt="macstache" width="400"/>
</p>
<br></br>


# macstache
A [Mustache](https://mustache.github.io) command line tool implementation for Mac written in Python. Uses `.json` files to read hash values for Mustache.



# Installation

## Pre-Build
If you only want the command line tool, go to `dist` folder and grab the `macstache` executable. Copy it to a folder, which is part of your `$PATH`, for example `usr/local/bin`. The following commands should install macstache on macOS
```
git clone https://github.com/columbbus/macstache.git
sudo cp macstache/dist/macstache /usr/local/bin/macstache
```
After that, just use the tool by calling `macstache` in the terminal.


## Build yourself
If you want to build the binary yourself, you're going to need [PyInstaller](https://www.pyinstaller.org). Compile the source code with the command
```
pyinstaller --onefile macstache.py
```

Make sure [Pystache](https://github.com/defunkt/pystache) is installed. If you don't already have it, install it using
```
pip install pystache
```



# Usage
After installing macstache (i.e. moving the executable to `/usr/local/bin`), you can start macstache on the terminal by calling `macstache`. Look into the `/demo` folder, it contains an example which showcases all features.


## Command Line Parameters
macstache needs 3 files as input, in order to compile the result
* **Template**: This file contains your template with Mustach tags, such as `{{name}}`
* **Context**: The context or data file is a `.json` file, which contains the hashes, for example: `{ "name": "John" }`
* **Output**: Specify the location, to where macstache should save the compiled output

Options:
* `-h`: Display help

An example command would look like this:
```
macstache source/index.mustache source/index.json build/index.html
```

## Directories in macstache
macstache changes the working directory to the directory, where your template is in. So you don't need to worry, that Mustache partials won't work, when you are calling macstache from a different directory than your template is in

This is particularly useful when working with `make` and you have a folder structure with `source` and `build` folders (see demo for more information).
