<br></br>
<p align="center">
  <img src="https://github.com/columbbus/macstache/blob/master/resources/macstache.png?raw=true" alt="macstache" height="300"/>
</p>
<br></br>


# macstache
A [Mustache](https://mustache.github.io) command line tool implementation for Mac written in Python. Uses `.json` files to read hash values for Mustache.



# Installation

## Pre-Build
If you only want the command line tool, go to `dist` folder and grab the `macstache` executable. Copy it to a folder, which is part of your `$PATH`. You can drag it into `usr/local/bin` for example. After that, just use the tool by calling `macstache` in the terminal.


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
* **Context**: The context or data file is a `.json` file, which contains the hashes, for example:
```
{
   "name": "John"
}
```

* **Output**: Specify the location, to where macstache should save the compiled output

An example command would look like this:
```
macstache source/index.mustache source/index.json build/index.html
```


## Additional features
I've included some additional features, that I am missing from the original Mustache.

### Partials subfoldering (*not yet implemented*)
Partial subfoldering automatically updates the reference to a partial, by putting the correct path in front of it.

Say I have the following file tree:
```
project
|
|__ source
|   |__ index.mustache
|   |__ index.json
|   |__ nav.mustache
|
|__ build
|   |__ index.html
```
I am in the `/project` folder and want to compile `index.html` using the following command
```
macstache source/index.mustache source/index.json build/index.html
```
For Mustache to work, a reference in `index.html` to the partial needs to look like this
```
{{> source/nav}}
```
Since this is inconvenient, because it depends on the overlaying directory structure, I would rather have something like this:
```
{{> nav}}
```
macstache solves this problem by automatically putting the given folder of the template (in this case `/source`) in front of the partial, so you don't need to worry about the current directory structure. Thus converting
```
{{> nav}}
to
{{> source/nav}}
```
or
```
{{> sub/folder/nav}}
to
{{> source/sub/folder/nav}}
```
