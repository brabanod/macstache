<br></br>
<p align="center">
  <img src="https://github.com/columbbus/macstache/blob/master/resources/macstache.png?raw=true" alt="macstache" height="300"/>
</p>
<br></br>


# macstache
[Mustache](https://mustache.github.io) command line tool implementation for Mac written in Python



# Installation

## Pre-Build
If you only want the command line tool, go to `dist` folder and grab the `macstache` executable. Copy it to a folder, which is part of your `$PATH`. You can drag it into `usr/local/bin` for example. After that, just user the tool by calling `macstache` in the terminal.


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
After installing macstache (i.e. moving the executable to `/usr/local/bin`), you can start macstache on the terminal by calling `macstache`.


## Command Line Parameters
macstache needs 3 files as input, in order to compile the result
* **Template**: This file contains your template with Mustach tags, such as `{{name}}`
* **Context**: The context or data file is a `.json` file, which contains the hashes, for example:
```
{
   "name": "John"
}
```

* **Output**: Specify the location, to where macstache should save the compiled output

An example command would look like this:
```
macstache source/index.html source/index.json build/index.html
```


## Additional features
I've included some additional features, that I am missing from the original Mustache.

### File referencing
Say you have an `.html` template an you want to reuse your navigation bar, which is saved in `nav.html`. In macstache you can load a file's content in the context file by having the value in this format: `@path/to/file.html`. macstache then replaces the file reference with the content of `file.html`. A context file would look like this:
```
{
   "navbar": "@nav.html"
}
```

### Recursive templating
The file being loaded from the context file (e.g. `nav.html`) can also be a Mustache template. If this *sub*-template contains a tag like `{{color}}`, then your context file (json) should contain a key value pair for `color`. macstache then first compile this *sub*-template, and then puts it into the context file. If there are no other *sub*-templates, macstache then compiles your primary template.

***Be careful with infinite loops!***

**THIS FEATURE IS NOT IMPLEMENTED YET**
