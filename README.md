# macstache
Mustache command line tool implementation for Mac written in Python

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


