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
