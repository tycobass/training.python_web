Setting Up Your Working Environment
===================================

 * Good editor
 	* tab completion
 	* good colorization
 	* auto-expand tabs to spaces
 * Code following (the editor should follow along while stepping through breakpoints)
 * Set breakpoints (it should be possible to set breakpoints in code from the editor)

 * You should be able to use the same editor in whatever environment you find yourself.

Sublime Text
------------

 * supports all platforms (Win, OSX, Linux) except BSD/FreeBSD :(
 * Highly configurable
 * Plugin system very advanced (and written in Python, so you can write your own!!)

 Pricey ($70), but imo very worth while (You can now buy a license that will work for both 2 and 3)

Set Up
------

All basic configuration is in Preferences -> Settings - Default

You can override one or more in Preferences -> Settings - User. Copy originals
from the default file

Settings files are always in JSON

Common settings to update:

.. code-block:: json

	{
		"font_face": "Droid Sans Mono Slashed",
		"font_size": 15,
		"ignored_packages":
		[
			// I'm not a vi user, so this is of no use to me.
			"Vintage"
		],
		"rulers":
		[
			// set text rulers so I can judge line length for pep8
			72, // docstrings
			79, // optimum code line length
			100  // maximum allowable length
		],
		"word_wrap": false,
		"wrap_width": 79
	}


Plugins
-------

Sublime comes with a package control system which can install/uninstall
packages for you.  It's not half bad.  To install it follow the `instructions
here <https://sublime.wbond.net/installation>`_.

Once the Package control system is installed, you can install packages as
follows:

 * type 'shift-super-P' to toggle open the ``command palette``
 * type 'install' and select ``Package Control: Install Package``
 * type the name of the package you want to install (or part of it) and select
   the match from the list

I like more control over text wrapping, so I first installed 
`Wrap Plus <https://github.com/ehuss/Sublime-Wrap-Plus>`_.  This allows me to 
have a keyboard command that will hard-wrap text at the value of my
`wrap_width` setting.  My old editor used ``ctrl-Q`` for this command, so I
bind the same key in Preferences -> Key Bindings - User:

.. code-block:: json

	[
		{ "keys": ["ctrl+q"], "command": "wrap_lines_plus" }
	]

There are also a couple of settings that require updating for me:

.. code-block:: json

	"WrapPlus.break_long_words": false,
	"WrapPlus.break_on_hyphens": false


I write a lot of RestructuredText (rst) so I want a plugin that will offer me
colorization and snippets for things I do in that language.  The best one I've
found is `sublime-rst-completion`_.  It offers a number of useful snippets for
common rst directives and even provides the ability to render items if you have
``docutils`` or ``pandoc`` installed.  All you have to do is install the
``Restructured Text (RST) Snippets`` plugin as directed above.  After that, you
can update the plugin user settings to point to your ``docutils``/``pandoc``
installation

.. code-block:: json

    { "command_path": [ "/Users/cewing/bin" ] }

.. _sublime-rst-completion: https://github.com/mgaitan/sublime-rst-completion

Pairing this with `reStructuredText Improved`_ provides quite a powerful
editing experience for rst authors.

.. _reStructuredText Improved: https://sublime.wbond.net/packages/RestructuredText%20Improved


