***********************************
Setting Up Your Working Environment
***********************************

 * Good editor
 	* tab completion
 	* good colorization
 	* auto-expand tabs to spaces
 * Code following (the editor should follow along while stepping through breakpoints)
 * Set breakpoints (it should be possible to set breakpoints in code from the editor)

 * You should be able to use the same editor in whatever environment you find yourself.

Sublime Text
============

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

Text wrapping
+++++++++++++

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


reStructuredText
++++++++++++++++

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


Linting
+++++++

I want to have inline code linting set up so I chose to use the 
`SublimeLinter`_ plugin with the `pep8`_ extension installed for python files.
Setup for this one is a bit tricky.

.. _pep8: https://sublime.wbond.net/packages/SublimeLinter-pep8

.. _SublimeLinter: http://sublimelinter.readthedocs.org/en/latest/index.html

First, I created a virtualenv where I can install packages I need to support
the function of the linter.  I installed pep8 into this virtualenv. Then I
installed the ``SublimeLinter`` plugin using the package manager. Before
installing the pep8 linter extension I needed to set some important settings
for ``SublimeLinter`` (Preferences -> Package Settings -> SublimeLinter ->
Settings - User):

.. code-block:: json

        "paths": {
            "linux": [],
            "osx": [
                "/Users/cewing/virtualenvs/sublenv/bin"
            ],
            "windows": []
        },
        "python_paths": {
            "linux": [],
            "osx": [
                "/Users/cewing/virtualenvs/sublenv/bin"
            ],
            "windows": []
        },

The ``"paths"`` key points to additional paths that will contain executables to
be used for linting, like pep8.  I point it to the virtualenv that contains my
pep8.  The ``"python_paths"`` key holds references to paths where the python
executable to be used will be located.  By default this will be something like
``/usr/bin/python``, so to ensure that I had a match between the python used,
and the linter to run, I made sure that the paths for both were set to the same
location.

Code Completion
+++++++++++++++

Code Completion is another important aspect of efficient code writing.  I want
a plugin that will work not only for stock Python symbols, but also for
packages that I include in my project.  There are two candidates that I can
find.  The first is `SublimeCodeIntel`_. the second is `SublimeJedi`_.  The
former has the advantage of supporting a wide variety of languages. The latter
uses the `Jedi`_ code completion library.

.. _Jedi: https://github.com/davidhalter/jedi

.. _SublimeJedi: https://sublime.wbond.net/packages/Jedi%20-%20Python%20autocompletion

.. _SublimeCodeIntel: https://sublime.wbond.net/packages/SublimeCodeIntel

I chose the latter. The primary reason was that I could get it running quickly.
I have heard very good things about ``SublimeCodeIntel`` but when I tried to
install and configure it, it overran my CPU, spiking to 100+% and remaining
there for more than 10 minutes before I killed the sublime text process to
recover.

Once installed, the package provides the ability to set a python interpreter
and additional paths via a project file. For a lot of my work, this is perfect,
as I use buildout and have a python plus an omelette directory that contains
all the source for my project.  Yay!


Git Helpers
===========

I use git for my source control, and there are a couple of nice add-ons and
tricksy commands you can use to make working with git a bit easier.


git-completion
--------------

The ability to tab-complete things like branch names, subcommands and more is
really helpful when you work in git all day long. Luckily, the nice folk who
come up with such things have created a bash script that can do just that:
`git-completion.bash`_. To use it, you simply download the source for your
particular version of git (the link for that script points to the version I had
installed when I wrote this) and put it somewhere.  Then you can use the
``source`` command from your ``.profile`` to include that code in bash whenever
you run a terminal:

.. code-block:: bash

    source ~/.git-completion.bash

.. _git-completion.bash: https://raw.github.com/git/git/v1.8.4.2/contrib/completion/git-completion.bash

I found a nifty script online that `does this automatically`_ for OS X.

.. _does this automatically: https://gist.github.com/johngibb/972430

git-prompt
----------

Keeping track mentally of the state of your working directory can also be quite
challenging in when using git. There've certainly been a number of times I've
committed a change, only to look up and realize I was on the wrong branch. Git
provides ways to dig yourself out of holes like that (thankfully), but it's
also nice to have visual reminders to help out.  The `git-prompt.sh`_ shell
script helps with this. Like ``git-completion.bash`` above, you copy this file 
to your home directory and then ``source`` it from your ``.profile``:

.. code-block:: bash

    source ~/.git-prompt.sh

Once you've done this, you can use the ``__git_ps1`` command, and a number of
environmental variables, to configure ``PS1`` and change your terminal prompt
to show the current branch of a repository when you are inside one. You can get
information about the status of HEAD, modified files, stashes, untracked files
and more, all with the possiblity of color output.  And if you aren't in a
repo, you can set up ``PS!`` to look just like your normal command prompt!
There's really decent documentation in the shell script about the options
available.

My configuration looks like this:

.. code-block:: bash

    source ~/.git-prompt.sh
    GIT_PS1_SHOWDIRTYSTATE=1
    GIT_PS1_SHOWCOLORHINTS=1
    GIT_PS1_SHOWSTASHSTATE=1
    GIT_PS1_SHOWUPSTREAM="auto"
    PROMPT_COMMAND='__git_ps1 "" "\h:\W \u\\\$ " "[%s]\n"'

.. _git-prompt.sh: https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh
