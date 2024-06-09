# Lab work 1 MTRPZ IM-23 Anastasia Dyvnych

# Markdown to HTML Parser

### Description

This is a simple console application written in Python that converts Markdown files to HTML. It supports basic Markdown features like bold, italic, monospaced text, preformatted text, and paragraphs.

### Instructions

In order to use this application, you need to have Python 3 installed. To get started, you need to clone this repository using the command:

git clone https://github.com/anastasiadyvnich/markdown-html.git

### To start the parser, you need to:

In the terminal, write the command
```
python main.py <your_file.md>
```

If you need to write the converted Markdown syntax to an HTML file, you need to specify the `--out` flag, as shown in the example below:

```
python main.py <your_file.md> --out <output.html>
```

### Example:

```
Lorem ipsum `dolor` sit amet, 
consectetur adipiscing elit, 
sed do eiusmod _tempor_ incididunt ut labore et dolore magna aliqua.

Ut enim ad **minim** veniam, quis nostrud exercitation _ullamco_ laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure **dolor** in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 

,```
Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum.
,```
```

### Result:

```html
<p>Lorem ipsum <tt>dolor</tt> sit amet,  consectetur adipiscing elit,  sed do eiusmod <i>tempor</i> incididunt ut labore et dolore magna aliqua.</p>
<p>Ut enim ad <b>minim</b> veniam, quis nostrud exercitation <i>ullamco</i> laboris nisi ut aliquip ex ea commodo consequat.  Duis aute irure <b>dolor</b> in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </p>
<p><pre>Excepteur sint occaecat cupidatat non proident,  sunt in culpa qui officia deserunt mollit anim id est laborum.</pre></p>
```

### Revert commit

git link