<img  height="50px" align="right" src="https://raw.githubusercontent.com/fchavonet/fchavonet/main/resources/images/logo-holberton_school.png" alt="Holberton School logo">

# Markdown to HTML

<details>
        <summary>
		CLICK TO ENLARGE 😇
        </summary>
	    📄 <a href="#description">Description</a>
        <br>
        🎓 <a href="#objectives">Objectives</a>
        <br>
        📋 <a href="#requirements">Requirements</a>
        <br>
        📝 <a href="#instructions">Instructions</a>
        <br>
        🔨 <a href="#tech-stack">Tech stack</a>
        <br>
        📂 <a href="#files-description">Files description</a>
        <br>
        💻 <a href="#installation">Installation</a>
        <br>
        ♥️ <a href="#thanks">Thanks</a>
        <br>
        👷 <a href="#authors">Authors</a>
</details>

## 📄 <span id="description">Description</span>

Markdown is awesome!
<br>
All the `README.md` files are made in Markdown, but do you know how GitHub renders them?
<br>
This project is designed to help me understand and implement the conversion of Markdown to HTML.
<br>
I have created a Python script that takes a Markdown file as input and generates an HTML file as output.
<br>
The script handles various Markdown features such as headings, unordered and ordered lists, paragraphs, bold and emphasis text, and custom text transformations.
<br>
Feel free to test it out yourself and see how it works!

## 🎓 <span id="objectives">Objectives</span>

At the end of this project, I had to be able to explain to anyone, **without the help of Google** :

- What is Markdown?
- How GitHub renders the README.md files.
- How to convert Markdown to HTML.

## 📋 <span id="requirements">Requirements</span>

- All my files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7 or higher).
- The first line of all my files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- My code should use the `PEP 8` style (version 1.7.*).
- All my files must be executable.
- All my modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`.
- My code should not be executed when imported (by using `if __name__ == "__main__":`).

## 📝 <span id="instructions">Instructions</span>

<details>
	<summary>
		<b>0. Start a script</b>
	</summary>
	<br>

Write a script `markdown2html.py` that takes an argument 2 strings:

- First argument is the name of the Markdown file.
- Second argument is the output file name.

Requirements:

- If the number of arguments is less than 2: print in STDERR `Usage: ./markdown2html.py README.md README.html` and exit 1.
- If the Markdown file doesn’t exist: print in STDER `Missing <filename>` and exit 1.
- Otherwise, print nothing and exit 0.

```
guillaume@vagrant:~/$ ./markdown2html.py
Usage: ./markdown2html.py README.md README.html
guillaume@vagrant:~/$ echo $?
1
guillaume@vagrant:~/$
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
Missing README.md
guillaume@vagrant:~/$ echo $?
1
guillaume@vagrant:~/$
guillaume@vagrant:~/$ echo "Test" > README.md
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ 
```

#
**Repo:**
- GitHub repository: `holbertonschool-Markdown2HTML`.
- File: `markdown2html.py`.
<hr>
</details>

<details>
	<summary>
		<b>1. Headings</b>
	</summary>
	<br>

Improve `markdown2html.py` by parsing Headings Markdown syntax for generating HTML:

**Syntax:** (you can assume it will be strictly this syntax).

| **Markdown**            | **HTML generated**         |
| ----------------------- | -------------------------- |
| `# Heading level 1`     | `<h1>Heading level 1</h1>` |
| `## Heading level 2`    | `<h2>Heading level 1</h2>` |
| `### Heading level 3`   | `<h3>Heading level 1</h3>` |
| `#### Heading level 4`  | `<h4>Heading level 1</h4>` |
| `##### Heading level 5` | `<h5>Heading level 1</h5>` |
| `###### Heading level 6`| `<h6>Heading level 1</h6>` |


```
guillaume@vagrant:~/$ cat README.md
# My title
## My title2
# My title3
#### My title4
### My title5

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<h2>My title2</h2>
<h1>My title3</h1>
<h4>My title4</h4>
<h3>My title5</h3>
guillaume@vagrant:~/$ 
```

Spacing and new lines between HTML tags don’t need to be exactly this one.

#
**Repo:**
- GitHub repository: `holbertonschool-Markdown2HTML`.
- File: `markdown2html.py`.
<hr>
</details>

<details>
	<summary>
		<b>2. Unordered listing</b>
	</summary>
	<br>

Improve `markdown2html.py` by parsing Unordered listing syntax for generating HTML:

**Syntax:** (you can assume it will be strictly this syntax).

Markdown:

```
- Hello
- Bye
```

HTML generated:

```
<ul>
    <li>Hello</li>
    <li>Bye</li>
</ul>
```

```
guillaume@vagrant:~/$ cat README.md
# My title
- Hello
- Bye

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>Hello</li>
<li>Bye</li>
</ul>
guillaume@vagrant:~/$ 
```

Spacing and new lines between HTML tags don’t need to be exactly this one.

#
**Repo:**
- GitHub repository: `holbertonschool-Markdown2HTML`.
- File: `markdown2html.py`.
<hr>
</details>

<details>
	<summary>
		<b>3. Ordered listing</b>
	</summary>
	<br>

Improve `markdown2html.py` by parsing Ordered listing syntax for generating HTML:

**Syntax:** (you can assume it will be strictly this syntax).

Markdown:

```
* Hello
* Bye
```

HTML generated:

```
<ol>
    <li>Hello</li>
    <li>Bye</li>
</ol>
```

```
guillaume@vagrant:~/$ cat README.md
# My title
* Hello
* Bye

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ol>
<li>Hello</li>
<li>Bye</li>
</ol>
guillaume@vagrant:~/$ 
```

Spacing and new lines between HTML tags don’t need to be exactly this one.

#
**Repo:**
- GitHub repository: `holbertonschool-Markdown2HTML`.
- File: `markdown2html.py`.
<hr>
</details>

<details>
	<summary>
		<b>4. Simple text</b>
	</summary>
	<br>

Improve `markdown2html.py` by parsing paragraph syntax for generating HTML:

**Syntax:** (you can assume it will be strictly this syntax).

Markdown:

```
Hello

I'm a text
with 2 lines
```

HTML generated:

```
<p>
    Hello
</p>
<p>
    I'm a text
        <br />
    with 2 lines
</p>
```

```
guillaume@vagrant:~/$ cat README.md
# My title
- Hello
- Bye

Hello

I'm a text
with 2 lines

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>Hello</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm a text
<br/>
with 2 lines
</p>
guillaume@vagrant:~/$ 
```

Spacing and new lines between HTML tags don’t need to be exactly this one.

#
**Repo:**
- GitHub repository: `holbertonschool-Markdown2HTML`.
- File: `markdown2html.py`.
<hr>
</details>

<details>
	<summary>
		<b>5. Bold and emphasis text</b>
	</summary>
	<br>

Improve `markdown2html.py` by parsing bold syntax for generating HTML:

**Syntax:** (you can assume it will be strictly this syntax).

| **Markdown** | **HTML generated** |
| ------------ | ------------------ |
| `**Hello**`  | `<b>Hello</b>`     |
| `__Hello__`  | `<em>Hello</em>`   |

```
guillaume@vagrant:~/$ cat README.md
# My title
- He**l**lo
- Bye

Hello

I'm **a** text
with __2 lines__

**Or in bold**

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>He<b>l</b>lo</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm <b>a</b> text
<br/>
with <em>2 lines</em>
</p>
<p>
<b>Or in bold</b>
</p>
guillaume@vagrant:~/$ 
```

Spacing and new lines between HTML tags don’t need to be exactly this one.

#
**Repo:**
- GitHub repository: `holbertonschool-Markdown2HTML`.
- File: `markdown2html.py`.
<hr>
</details>

<details>
	<summary>
		<b>6. ... but why??</b>
	</summary>
	<br>

Improve `markdown2html.py` by parsing bold syntax for generating HTML:

**Syntax:** (you can assume it will be strictly this syntax).

| **Markdown**        | **HTML generated**                 | **Description**                                   |
| ------------------- | ---------------------------------- | ------------------------------------------------- |
| `[[Hello]]`         | `8b1a9953c4611296a827abf8c47804d7` | Convert in MD5 (lowercase) the content.           |
| `((Hello Chicago))` | `Hello hiago`                      | Remove all c (case insensitive) from the content. |

```
guillaume@vagrant:~/$ cat README.md
# My title
- He**l**lo
- Bye

Hello

I'm **a** text
with __2 lines__

((I will live in Caracas))

But it's [[private]]

So cool!

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>He<b>l</b>lo</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm <b>a</b> text
<br/>
with <em>2 lines</em>
</p>
<p>
I will live in araas
</p>
<p>
But it's 2c17c6393771ee3048ae34d6b380c5ec
</p>
<p>
So cool!
</p>
guillaume@vagrant:~/$
```

Spacing and new lines between HTML tags don’t need to be exactly this one.

#
**Repo:**
- GitHub repository: `holbertonschool-Markdown2HTML`.
- File: `markdown2html.py`.
<hr>
</details>

## 🔨 <span id="tech-stack">Tech stack</span>

<p align="left">
    <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge" alt="HTML badge" alt="HTML5 badge">
    <img src="https://img.shields.io/badge/MARKDOWN-000000?logo=markdown&logoColor=white&style=for-the-badge" alt="Markdown badge">
    <img src="https://img.shields.io/badge/PYTHON-3776ab?logo=python&logoColor=white&style=for-the-badge" alt="Python badge">
<p>

## 📂 <span id="files-description">File description</span>

| **FILE**           | **DESCRIPTION**                                                 |
| :----------------: | --------------------------------------------------------------- |
| `README.md`        | The readme file you are currently reading 😉.                   |
| `markdown2html.py` | Python script to convert Markdown to HTML.                      |
| `test.html`        | Generated HTML file from the sample Markdown file.              |
| `test.md`          | Sample Markdown file for testing the `markdown2html.py` script. |

## 💻 <span id="installation">Installation</span>

- Ensure Python is installed on your system.

1. Clone this repository:
    - Open your preferred Terminal.
    - Navigate to the directory where you want to clone the repository.
    - Run the following command:
```
git clone https://github.com/fchavonet/holbertonschool-Markdown2HTML.git
```

2. Open the repository you've just cloned.

3. Run the script:

*On Windows:*
```
python markdown2html.py test.md test.html
```

*On Linux or MacOS:*
```
python3 markdown2html.py test.md test.html
```

4. Check the new HTML file:

```
cat test.html
```

<details>
    <summary>
		<b>Click here to see the expected result ↓ </b>
	</summary>
	<br>

```
<h1>Welcome to Markdown2HTML Project!</h1>
<p>
This tool converts <b>Markdown</b> to <b>HTML</b>.
</p>
<h2>Features</h2>
<ul>
<li>Converting headings to HTML.</li>
<li>Handling unordered lists.</li>
<li>Handling ordered lists.</li>
<li>Handling paragraphs.</li>
<li>Parsing <b>bold</b> text.</li>
<li>Parsing <em>italic</em> text.</li>
<li>Custom syntax for MD5 hashing.</li>
<li>Removing "c" characters from content.</li>
</ul>
<p>
So to truly understand the reality, you must take the <b>red pill</b>...
</p>
<h1>Heading</h1>
<h2>Heading</h2>
<h3>Heading</h3>
<h4>Heading</h4>
<h5>Heading</h5>
<h6>Heading</h6>
<h2>Unordered List</h2>
<ul>
<li>Pikachu.</li>
<li>Bulbizarre.</li>
<li>Salamèche.</li>
<li>Carapuce.</li>
</ul>
<h2>Ordered List</h2>
<ol>
<li>Goku.</li>
<li>Vegeta.</li>
<li>Piccolo.</li>
<li>Krillin.</li>
<li>Yamcha.</li>
</ol>
<h2>Example Paragraph</h2>
<p>
This is an example paragraph.
<br/>
It includes various features such as <b>bold text</b>, <em>italic text</em>, and custom syntax.
<br/>
For example, we can hash your 5f4dcc3b5aa765d61d8327deb882cf99 to keep it secure.
<br/>
Or we might need to clean up text by removing <em>speifi haraters</em>.
</p>
<p>
And don't forget the <em>ultimate answer to life, the universe, and everything</em> is <b>42</b>.
</p>
<h2>Final Thoughts</h2>
<p>
With great power comes great responsibility.
<br/>
Use this <b>Markdown to HTML</b> converter wisely!
</p>
```
</details>
<br>

To directly view the HTML page result, click [here](https://fchavonet.github.io/holbertonschool-Markdown2HTML/test.html).

## ♥️ <span id="thanks">Thanks</span>

A big thank you to all my Holberton School peers for their help and support throughout these projects.

## 👷 <span id="authors">Authors</span>

**Fabien CHAVONET**
- Github: [@fchavonet](https://github.com/fchavonet)
