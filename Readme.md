============
Sublime Text Soar Tools
============

Sublime Text package for [Soar](http://sitemaker.umich.edu/soar/home) development.

Getting Started
===============

* After installing [Package Control](https://sublime.wbond.net/installation), use the *Command Palette* (``Ctrl+Shift+P``) to select
   ``Install Package`` and then search for ``Soar Tools``.
<!-- * Access commands from **Tools | Packages | Package Development** or the *Command Palette*. -->

Current Functionality
=====================

Many features, including ones requiring connection with a Soar agent, are TODO.

###Syntax Highlighting

Soar syntax highlighting is applied to files with the '.soar' or '.soarunit' extensions. Code folding is also provided but is irregular at the moment.

###Snippets

Several snippets are currently provided for various types of Soar productions, [SoarDoc](http://web.eecs.umich.edu/~soar/sitemaker/projects/soardoc/soardoc.html), and [SoarUnit](https://code.google.com/p/jsoar/wiki/SoarUnit) setup/test blocks. SoarDoc snippets are triggered by `##!` and production snippets are triggered by `sp`. Provided snippets are:

* SoarDoc, triggered by `##!`, for:
    - documenting a file
    - documenting an operator
    - documenting a production
* Soar productions, triggered by `sp`, for:
    - propose/compare/apply operator
    - elaborate state
    - elaborate substate
* SoarUnit blocks:
    - setup block
    - test block

