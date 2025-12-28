<h1 align="center">🧠 LETS-BUILD-OUR-OWN-REGEX-ENGINE</h1>

<p align="center"><em>Demystifying Regular Expressions by Building One from Scratch</em></p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/<YOUR_GITHUB_USERNAME>/<REPO_NAME>?color=blue&label=last%20commit">
  <img src="https://img.shields.io/badge/python-100%25-blue">
  <img src="https://img.shields.io/github/languages/count/<YOUR_GITHUB_USERNAME>/<REPO_NAME>?color=blue&label=languages">
</p>

<p align="center">
  Built with the tools and technologies:<br>
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
</p>

---

# 🧬 PyRegex — A Complete Regex Engine Built from Scratch

**PyRegex** is a fully functional **Regular Expression Engine** implemented entirely in **Python**, without using the built-in `re` module.

It recreates the **entire regex pipeline** — from **lexing** and **parsing** to **AST construction** and **backtracking-based matching** — giving deep insight into how real regex engines work internally.

> 🧠 *“If you truly want to understand regex, build the engine — not just use it.”*

---

## 📖 What is PyRegex?

PyRegex takes a regex pattern and:
1. **Tokenizes** it (Lexer)
2. **Parses** it using recursive-descent parsing
3. **Builds an Abstract Syntax Tree (AST)**
4. **Executes matches** via AST traversal and backtracking

All logic is implemented manually — no shortcuts, no wrappers.

---

## ⚙️ Core Components

| Component | Description |
|----------|-------------|
| 🔍 **Lexer** | Converts the regex pattern into a stream of tokens |
| 🧠 **Parser** | Recursive-descent parser that respects regex precedence |
| 🌳 **AST** | Represents regex structure using typed nodes |
| ⚙️ **Matcher** | Traverses the AST and performs backtracking matches |
| 📦 **Match Result** | Returns match span, text, and captured groups |

---

## 🚀 Supported Features

| Category | Supported |
|--------|-----------|
| Literals | `a`, `b`, `c` |
| Concatenation | `abc` |
| Alternation | `a|b` |
| Quantifiers | `*`, `+`, `?`, `{m,n}` |
| Greedy / Lazy | `*?`, `+?`, `{m,n}?` |
| Character Classes | `[a-z]`, `[^0-9]` |
| Predefined Classes | `\d`, `\D`, `\w`, `\W`, `\s`, `\S` |
| Capturing Groups | `(abc)` |
| Non-Capturing Groups | `(?:abc)` |
| Backreferences | `\1`, `\2` |
| Lookahead | `(?=abc)`, `(?!abc)` |
| Lookbehind | `(?<=abc)`, `(?<!abc)` |
| Anchors | `^`, `$`, `\b`, `\B` |

---

## 🧠 Regex Engine Architecture

