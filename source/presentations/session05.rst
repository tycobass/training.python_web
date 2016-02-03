.. slideconf::
    :autoslides: True

**********
Session 05
**********

.. image:: /_static/python.png
    :align: center
    :width: 43%



MVC Applications
================

Wherin we learn about the Model View Controller approach to app design and
explore data persistence in Python.

.. figure:: http://upload.wikimedia.org/wikipedia/commons/4/40/MVC_passive_view.png
    :align: center
    :width: 40%

    By Alan Evangelista (Own work) [CC0], via Wikimedia Commons

Separation of Concerns
----------------------

.. rst-class:: build
.. container::

    In the first part of this course, you were introduced to the concept of
    *Object Oriented Programming*

    OOP was `first formalized`_ in the 1970s in *Smalltalk*, invented by Alan
    Kay at *Xerox PARC*

    *Smalltalk* was also the first language which utilized the
    `Model View Controller`_ design pattern.

    This pattern (like all `design patterns`_) seeks to provide a *way of
    thinking* that helps to make software design easier.

    In this case, the goal is to help clarify the high-level *separation of
    concerns* in a system.

.. _first formalized: http://en.wikipedia.org/wiki/Object-oriented_programming#History
.. _Model View Controller: http://en.wikipedia.org/wiki/Model–view–controller
.. _design patterns: http://en.wikipedia.org/wiki/Software_design_pattern

Three Components
----------------

The pattern divides the elements of a system into three parts:

.. rst-class:: build

Model:
  This component represents the *data* that comprises the system, and the
  *logic* used to manipulate that data.

View:
  This component can be any *representation* of the data to the outside world:
  a chart, diagram, table, user interface, etc.

  It also includes representations of the *actions* available in the system.

Controller:
  This component coordinates the Model and the View in a system.

  It accepts input from a user and channels that input into the Model.

  It accepts information about the current state of the Model and transmits
  that information to the View.

On the Web
----------

This pattern has proven useful for thinking about the applications we build for
the web.

.. rst-class:: build
.. container::

    A web browser provides a convenient container for *views* of data.

    These *views* are created by *controller* software hosted on a server.

    This *controller* software accepts input from users via *HTTP requests*,
    channeling it into a *data model*, often stored in some database.

    The *controller* returns information about the state of the *data model* to
    the user via *HTTP responses*

.. nextslide::

This approach is so common, that it has been formalized into any number of *web
frameworks*

.. rst-class:: build
.. container::

    *Web frameworks* abstract away the specifics of the *HTTP request/response
    cycle*, leaving simple MVC components for the developer to use.

    *Web frameworks* exist in nearly all modern languages.

    Python has scores of them.

    Over the weeks to come, we'll learn about two of them, `Pyramid`_ and
    `Django`_.

.. _Pyramid: http://www.pylonsproject.org/projects/pyramid/about
.. _Django: https://www.djangoproject.com/

A Word About Terminology
------------------------

Although the MVC pattern is a useful abstraction, there are a few differences
in how things are named in Python web frameworks

.. rst-class:: build centered
.. container::

    model <--> model

    controller <--> view

    view <--> template (or even HTTP response)

    .. rst-class:: left

    For more on this difference, you can `read this`_ from the Pyramid design
    documentation.

.. _read this: http://docs.pylonsproject.org/projects/pyramid/en/latest/designdefense.html#pyramid-gets-its-terminology-wrong-mvc

Our First Application
=====================

.. rst-class:: left

But enough abstract blabbering.

.. rst-class:: build left
.. container::

    There's no better way to make concepts like these concrete than to build
    something using them.

    Let's make an application!

    We're going to build a Learning Journal.

    When we're done, you'll have a live, online application you can use to keep
    note of the things you are learning about Python development.

    We'll use one of our Python web framework to do this: `Pyramid`_

Pyramid
-------

First published in 2010, `Pyramid`_ is a powerful, flexible web framework.

.. rst-class:: build
.. container::

    You can create compelling one-page applications, much like in
    microframeworks like Flask

    You can also create powerful, scalable applications using the full
    power of Python

    Created by the combined powers of the teams behind Pylons and Zope

    It represents the first true second-generation web framework in
    existence.

Starting the Project
--------------------

The first step is to prepare for the project.

.. rst-class:: build
.. container::

    Begin by creating a location where you'll do your work.

    I generally put all my work in a folder called ``projects`` in my home
    directory:

    .. code-block:: bash

        $ cd
        $ mkdir projects
        $ cd projects
        $ mkdir learning-journal
        $ cd learning-journal
        $ pwd
        /Users/cewing/project/learning-journal

.. nextslide:: Creating an Environment

We continue our preparations by creating the virtual environment we will use
for our project.

.. rst-class:: build
.. container::

    Again, this will help us to keep our work here isolated from anything else
    we do.

    Remember how to make a new venv?

    .. code-block:: bash

        $ pyvenv ljenv

    .. code-block:: posh

        c:\Temp>python -m venv myenv

    And then, how to activate it?

    .. code-block:: bash

        $ source ljenv/bin/activate
        (ljenv)$

    .. code-block:: posh

        C:> ljenv/Scripts/activate.bat

.. nextslide:: Installing Pyramid

Next, we install the Pyramid web framework into our new virtualenv.

.. rst-class:: build
.. container::

    We can do this with the ``pip`` in our active ``ljenv``:

    .. code-block:: bash

        (ljenv)$ pip install pyramid
        Collecting pyramid
          Downloading pyramid-1.5.2-py2.py3-none-any.whl (545kB)
            100% |################################| 548kB 172kB/s
        ...
        Successfully installed PasteDeploy-1.5.2 WebOb-1.4
        pyramid-1.5.2 repoze.lru-0.6 translationstring-1.3
        venusian-1.0 zope.deprecation-4.1.1 zope.interface-4.1.2

    Once that is complete, we are ready to create a *scaffold* for our project.

Working with Pyramid
--------------------

Many web frameworks require at least a bit of *boilerplate* code to get
started.

.. rst-class:: build
.. container::

    Pyramid does not.

    However, our application will require a database and handling that does
    require some.

    Pyramid provides a system for creating boilerplate called ``pcreate``.

    You use it to generate the skeleton for a project based on some pattern:

    .. code-block:: bash

        (ljenv)$ pcreate -s alchemy learning_journal
        Creating directory /Users/cewing/projects/learning-journal/learning_journal
        ...
        Welcome to Pyramid.  Sorry for the convenience.
        ===============================================================================

    Let's take a quick look at what that did

.. nextslide:: What You Get

.. code-block:: bash

    ...
    ├── development.ini
    ├── learning_journal
    │   ├── __init__.py
    │   ├── models.py
    │   ├── scripts
    │   │   ├── __init__.py
    │   │   └── initializedb.py
    │   ├── static
    ...
    │   ├── templates
    │   │   └── mytemplate.pt
    │   ├── tests.py
    │   └── views.py
    ├── production.ini
    └── setup.py

.. nextslide:: Saving Your Work

You've now created something worth saving.

.. rst-class:: build
.. container::

    Start by initializing a new git repository in the `learning_journal` folder
    you just created:

    .. code-block:: bash

        (ljenv)$ cd learning_journal
        (ljenv)$ git init
        Initialized empty Git repository in
         /Users/cewing/projects/learning-journal/learning_journal/.git/

.. nextslide:: Saving Your Work

Check ``git status`` to see where things stand:

.. code-block:: bash

    (ljenv)$ git status
    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        CHANGES.txt
        MANIFEST.in
        README.txt
        development.ini
        learning_journal/
        production.ini
        setup.py

.. nextslide:: Add the Project Code

Add your work to this new repository:

.. code-block:: bash

    (ljenv)$ git add .
    (ljenv)$ git status
    ...
    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

        new file:   CHANGES.txt
        new file:   MANIFEST.in
        ...
        new file:   production.ini
        new file:   setup.py

.. nextslide:: Ignore Irrelevant Files

Python creates ``.pyc`` files when it executes your code.

.. rst-class:: build
.. container::

    There are many other files you don't want or need in your repository

    You can ignore this in ``git`` with the ``.gitignore`` file.

    Create one now, in this same directory, and add the following basic lines::

        *.pyc
        .DS_Store

    Finally, add this new file to your repository, too.

    .. code-block:: bash
    
        (ljenv)$ git add .gitignore

.. nextslide:: Make It Permanent

To preserve all these changes, you'll need to commit what you've done:

.. code-block:: bash

    (ljenv)$ git commit -m "initial commit of the Pyramid learning journal"

.. rst-class:: build
.. container::

    This will make a first commit here in this local repository.

    For homework, you'll put this into GitHub, but this is enough for now.

    Let's move on to learning about what we've built so far.

.. nextslide:: Project Structure

When you ran the ``pcreate`` command, a new folder was created:
``learning_journal``.

.. rst-class:: build
.. container::

    This folder contains your *project*.

    At the top level, you have *configuration* (.ini files)

    You also have a file called ``setup.py``

    This file turns this collection of Python code and configuration into an
    *installable Python distribution*

    Let's take a moment to look over the code in that file

.. nextslide:: ``setup.py``

.. code-block:: python

    from setuptools import setup, find_packages
    ...
    requires = [
        'pyramid',
        ... # packages on which this software depends (dependencies)
        ]
    setup(name='learning_journal',
          version='0.0',
          ... # package metadata (used by PyPI)
          install_requires=requires,
          # Entry points are ways that we can run our code once installed
          entry_points="""\
          [paste.app_factory]
          main = learning_journal:main
          [console_scripts]
          initialize_learning_journal_db = learning_journal.scripts.initializedb:main
          """,
          )

Pyramid is Python
-----------------

In the ``__init__.py`` file of your app *package*, you'll find a ``main``
function:

.. code-block:: python

    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        config = Configurator(settings=settings)
        config.include('pyramid_chameleon')
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_route('home', '/')
        config.scan()
        return config.make_wsgi_app()

Let's take a closer look at this, line by line.

.. nextslide:: System Configuration

.. code-block:: python

    def main(global_config, **settings):

Configuration is passed in to an application after being read from the
``.ini`` file we saw above.

.. rst-class:: build
.. container::

    These files contain sections (``[app:main]``) containing ``name = value``
    pairs of *configuration data*

    This data is parsed with the Python
    `ConfigParser <http://docs.python.org/2/library/configparser.html>`_ module.

    The result is a dict of values:

    .. code-block:: python

        {'app:main': {'pyramid.reload_templates': True, ...}, ...}

    The default section of the file is passed in as ``global_config``, the
    section for *this app* as ``settings``.

.. nextslide:: Database Configuration

.. code-block:: python

    from sqlalchemy import engine_from_config
    from .models import DBSession, Base
    ...
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

We will use a package called ``SQLAlchemy`` to interact with our database.

.. rst-class:: build
.. container::

    Our connection is set up using settings read from the ``.ini`` file.

    Can you find the settings for the database?

    The ``DBSession`` ensures that each *database transaction* is tied to HTTP
    requests.

    The ``Base`` provides a parent class that will hook our *models* to the
    database.

.. nextslide:: App Configuration

.. code-block:: python

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()

Pyramid controlls application-level configuration using a ``Configurator`` class.

.. rst-class:: build
.. container::

    It uses app-specific settings passed in from the ``.ini`` file

    We can also ``include`` configuration from other add-on packages

    Additionally, we can configure *routes* and *views* needed to connect our
    application to the outside world here (more on this next week).

    Finally, the ``Configurator`` instance performs a ``scan`` to ensure there
    are no problems with what we've created.

.. nextslide:: A Last Word on Configuration

We will return to the configuration of our application repeatedly over the next
sessions.

.. rst-class:: build
.. container::

    Pyramid configuration is powerful and flexible.

    We'll use a few of its features

    But there's a lot more you could (and should) learn.

    Read about it in the `configuration chapter`_ of the Pyramid documentation.

.. _configuration chapter: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html

.. nextslide:: Break Time

Let's take a moment to rest up and absorb what we've learned.

When we return, we'll see how we can create *models* that will embody the data
for our Learning Journal application.

.. rst-class:: centered

**Pyramid Models**


Models in Pyramid
=================

.. rst-class:: left
.. container::

    The central component of MVC, the model, captures the behavior of the
    application in terms of its problem domain, independent of the user
    interface. The model directly manages the data, logic and rules of the
    application

    -- from the Wikipedia article on `Model-view-controller`_

.. _Model-view-controller: http://en.wikipedia.org/wiki/Model–view–controller

Models and ORMs
---------------

In an MVC application, we define the *problem domain* by creating one or more
*Models*.

.. rst-class:: build
.. container::

    These capture relevant details about the information we want to preserve
    and how we want to interact with it.

    In Python-based MVC applications, these *Models* are implemented as Python
    classes.

    The individual bits of data we want to know about are *attributes* of our
    classes.

    The actions we want to take using that data are *methods* of our classes.

    Together, we can refer to this as the *API* of our system.

.. nextslide:: Persistence

It's all well and good to have a set of Python classes that represent your
system.

.. rst-class:: build
.. container::

    But what happens when you want to *save* information.

    What happens to a instance of a Python class when you quit the interprer?

    When your script stops running?

    The code in a website runs when an HTTP request comes in from a client.

    It stops running when an HTTP response goes back out to the client.

    So what happens to the data in your system in-between these moments?

    The data must be *persisted*

.. nextslide:: Alternatives

In the last class from part one of this series, you explored a number of
alternatives for persistence

.. rst-class:: build

* Python Literals
* Pickle/Shelf
* Interchange Files (CSV, XML, INI)
* Object Stores (ZODB, Durus)
* NoSQL Databases (MongoDB, CouchDB)
* SQL Databases (sqlite, MySQL, PostgreSQL, Oracle, SQLServer)

.. rst-class:: build
.. container::

    Any of these might be useful for certain types of applications.

    On the web, you tend to see two used the most:

    .. rst-class:: build

    * NoSQL
    * SQL

.. nextslide:: Choosing One

How do you choose one over the other?

.. rst-class:: build
.. container::

    In general, the telling factor is going to be how you intend to use your
    data.

    In systems where the dominant feature is viewing/interacting with
    individual objects, a NoSQL storage solution might be the best way to go.

    In systems with objects that are related to eachother, SQL-based Relational
    Databases are a better choice.

    Our system is more like this latter type (trust me on that one for now).

    We'll be using SQL (sqlite to start with).


.. nextslide:: Objects and Tables

So we have a system where our data is captured in Python *objects*

.. rst-class:: build
.. container::

    And a storage system where our data must be rendered as database *tables*

    Python provides a specification for interacting directly with databases:
    `dbapi2`_

    And there are multiple Python packages that implement this specification
    for various databases:

    .. rst-class:: build

    * sqlite3
    * python-mysql
    * psycopg2
    * ...

    With these, you can write SQL to save your Python objects into your
    database.

.. _dbapi2: https://www.python.org/dev/peps/pep-0249/

.. nextslide:: ORMs

But that's a pain.

.. rst-class:: build
.. container::

    SQL, while not impossible, is yet another language to learn.

    And there is a viable alternative in using an *Object Relational Manager*
    (ORM)

    An ORM provides a layer of *abstraction* between you and SQL

    You instantiate Python objects and set attributes on them

    The ORM handles converting data from these objects into SQL statements (and
    back)

SQLAlchemy
----------

In our project we will be using the `SQLAlchemy`_ ORM.

.. rst-class:: build
.. container::

    You can find SQLAlchemy among the packages in ``requires`` in ``setup.py``
    in our new ``learning_journal`` package.

    However, we don't yet have that code installed.

    To do so, we will need to "install" our own package

    Make sure your ``ljenv`` virtualenv is active and then type the following:

    .. code-block:: bash

        (ljenv)$ python setup.py develop
        running develop
        running egg_info
        creating learning_journal.egg-info
        ...
        Finished processing dependencies for learning-journal==0.0

.. nextslide::

Once that is complete, all the *dependencies* listed in our ``setup.py`` will
be installed.

.. rst-class:: build
.. container::

    You can also install the package using ``python setup.py install``

    But using ``develop`` allows us to continue developing our package without
    needing to re-install it every time we change something.

    It is very similar to using the ``-e`` option to ``pip``

    Now, we'll only need to re-run this command if we change ``setup.py``
    itself.

.. nextslide::

We also need to adjust our ``.gitignore`` file:

.. rst-class:: build
.. code-block:: bash

    (ljenv)$ git status
    ...
    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        learning_journal.egg-info/

.. rst-class:: build
.. container::

    The ``egg-info`` directory that was just created is an artifact of
    installing a Python egg.

    It should never be committed to a repository.

    Let's add ``*.egg-info`` to our ``.gitignore`` file and then commit that
    change

    Remember how?

.. nextslide:: Our First Model

Our project skeleton contains up a first, basic model created for us:

.. code-block:: python

    # in models.py
    Base = declarative_base()

    class MyModel(Base):
        __tablename__ = 'models'
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        value = Column(Integer)
    Index('my_index', MyModel.name, unique=True, mysql_length=255)

.. _SQLAlchemy: http://docs.sqlalchemy.org/en/rel_0_9/

.. rst-class:: build
.. container::

    Our class inherits from ``Base``

    We ran into ``Base`` earlier when discussing configuration.

    We were binding it to the database we wanted to use (the ``engine``)

.. nextslide:: ``Base``

Any class we create that inherits from this ``Base`` becomes a *model*

.. rst-class:: build
.. container::

    It will be connected through the ORM to a table in our database.

    The name of the table is determined by the ``__tablename__`` special
    attribute.

    Other aspects of table configuration can also be controlled through special
    attributes

    Instances of the class, once saved, will become rows in the table.

    Attributes of the model that are instances of ``Column`` will become
    columns in the table.

    You can learn much more in the `Declarative`_ chapter of the SQLAlchemy docs

.. _Declarative: http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/declarative/

.. nextslide:: Columns

Each attribute of your model that will be persisted must be an instance of
`Column`_.

.. rst-class:: build
.. container::

    Each instance requires *at least* a specific `data type`_ (such as
    Integer).

    Additionally, you can control other aspects of the column such as it being
    a primary key.

    In the *declarative* style we are using, the name of the column in the
    database will default to the attribute name you assigned.

    If you wish, you may provide a name specifically.  It must be the first
    argument and must be a string.

.. _Column: http://docs.sqlalchemy.org/en/rel_0_9/core/metadata.html#sqlalchemy.schema.Column
.. _data type: http://docs.sqlalchemy.org/en/rel_0_9/core/types.html

Creating The Database
---------------------

We have a *model* which allows us to persist Python objects to an SQL database.

.. rst-class:: build
.. container::

    But we're still missing one ingredient here.

    We need to create our database, or there will be nowhere for our data to
    go.

    Luckily, our ``pcreate`` scaffold also gave us a convenient way to handle
    this:

    .. code-block:: python

        # in setup.py
        entry_points="""\
        [paste.app_factory]
        main = learning_journal:main
        [console_scripts]
        initialize_learning_journal_db = learning_journal.scripts.initializedb:main
        """,

    The ``console_script`` set up as an entry point will help us.

.. nextslide:: ``initialize_learning_journal_db``

Let's look at that code for a moment.

.. code-block:: python

    # in scripts/intitalizedb.py
    from ..models import DBSession, MyModel, Base
    # ...
    def main(argv=sys.argv):
        if len(argv) < 2:
            usage(argv)
        config_uri = argv[1]
        options = parse_vars(argv[2:])
        setup_logging(config_uri)
        settings = get_appsettings(config_uri, options=options)
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = MyModel(name='one', value=1)
            DBSession.add(model)

.. nextslide:: Console Scripts

By connecting this function as a ``console script``, our Python package makes
this command available to us.

.. rst-class:: build
.. container::

    When we exectute ``initialize_learning_journal_db`` at the command line, we
    will be running this function.

    Let's try it out.

    We'll need to provide a configuration file name, let's use
    ``development.ini``:

    .. code-block:: bash

        (ljenv)$ initialize_learning_journal_db development.ini
        2015-01-05 18:59:55,426 INFO  [sqlalchemy.engine.base.Engine][MainThread] SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
        ...
        2015-01-05 18:59:55,434 INFO  [sqlalchemy.engine.base.Engine][MainThread] COMMIT

    The ``[loggers]`` configuration in our ``.ini`` file sends a stream of
    INFO-level logging to sys.stdout as the console script runs.

.. nextslide:: A Bit More Cleanup

So what was the outcome of running that script?

.. rst-class:: build
.. container::

    .. code-block:: bash

        (ljenv)$ ls
        ...
        learning_journal.sqlite
        ...

    We've now created an sqlite database.

    You'll need to add ``*.sqlite`` to ``.gitignore`` so you don't
    inadvertently add that file to your repository.

    Once you've done so, commit the change to your repository

Interacting with SQLA Models
----------------------------

It's pretty easy to play with your models from in an interpreter.

.. rst-class:: build
.. container::

    But before we do so, let's make a nicer interpreter available for our
    project

    You've been using iPython in class, we can use it here too.

    Just install it with ``pip``:

    .. code-block:: bash
    
        (ljenv)$ pip install ipython pyramid_ipython

    Once that finishes, you'll be able to use iPython as your interpreter for
    this project.

    And ``Pyramid`` provides a way to connect your interpreter to the
    application code you are writing:

    The ``pshell`` command

.. nextslide:: The ``pshell`` command

Let's fire up ``pshell`` and explore for a moment to see what we have at our
disposal:

.. rst-class:: build
.. container::

    .. code-block:: bash
    
        (ljenv)$ pshell development.ini
        Python 3.5.0 (default, Sep 16 2015, 10:42:55)
        Type "copyright", "credits" or "license" for more information.

        IPython 4.0.1 -- An enhanced Interactive Python.
        ?         -> Introduction and overview of IPython's features.
        %quickref -> Quick reference.
        help      -> Python's own help system.
        object?   -> Details about 'object', use 'object??' for extra details.

        Environment:
          app          The WSGI application.
          registry     Active Pyramid registry.
          request      Active request object.
          root         Root of the default resource tree.
          root_factory Default root factory used to create `root`.

.. nextslide::

The ``environment`` created by ``pshell`` provides us with a few useful tools. 

.. code-block:: bash

    app          The WSGI application.
    registry     Active Pyramid registry.
    request      Active request object.
    root         Root of the default resource tree.
    root_factory Default root factory used to create `root`.

.. rst-class:: build

* The ``app`` is our new learning journal application
* The ``registry`` provides us with access to settings and other useful
  information
* The ``request`` is an artificial HTTP request we can use if we need to
  pretend we are listening to clients
* ...
  
.. nextslide:: 

Let's use this environment to build a database session and interact with our
data:

.. code-block:: ipython

    In [1]: from sqlalchemy import engine_from_config
    In [2]: engine = engine_from_config(registry.settings, 'sqlalchemy.')
    In [3]: from sqlalchemy.orm import sessionmaker
    In [4]: Session = sessionmaker(bind=engine)
    In [5]: session = Session()
    In [6]: from learning_journal.models import MyModel
    In [7]: session.query(MyModel).all()
    ...
    2015-12-21 18:06:05,179 INFO  [sqlalchemy.engine.base.Engine][MainThread] SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value
    FROM models
    2015-12-21 18:06:05,179 INFO  [sqlalchemy.engine.base.Engine][MainThread] ()
    Out[7]: [<learning_journal.models.MyModel at 0x105f30208>]

We've stolen a lot of this from the ``initializedb.py`` script

.. nextslide:: Basic Interactions

Any interaction with the database requires a ``session``.

.. rst-class:: build
.. container::

    This object represents the connection to the database.

    All database queries are phrased as methods of the session.

    .. container::

        .. code-block:: ipython

            In [8]: query = session.query(MyModel)
            In [9]: type(query)
            Out[9]: sqlalchemy.orm.query.Query

        The ``query`` method of the session object returns a ``Query`` object

    Arguments to the ``query`` method can be a *model* class or *columns* from
    a model class.

.. nextslide:: Queries are Iterators

You can iterate over a query object. The result depends on the args you passed.

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [10]: q1 = session.query(MyModel)
        In [11]: for row in q1:
           ....:     print(row)
           ....:     print(type(row))
           ....:
        <learning_journal.models.MyModel object at 0x105f30208>
        <class 'learning_journal.models.MyModel'>

.. nextslide:: Queries are Iterators

You can iterate over a query object. The result depends on the args you passed.

    .. code-block:: ipython

        In [12]: q2 = session.query(MyModel.name, MyModel.id, MyModel.value)
        In [13]: for name, id, val in q2:
           ....:     print(name)
           ....:     print(type(name))
           ....:     print(id)
           ....:     print(type(id))
           ....:     print(val)
           ....:     print(type(val))
           ....:
        one
        <class 'str'>
        1
        <class 'int'>
        1
        <class 'int'>

.. nextslide:: Queries have SQL

You can view the SQL that your query will use:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [14]: str(q1)
        Out[14]: 'SELECT models.id AS models_id, models.name AS models_name, models.value AS models_value \nFROM models'

        In [15]: str(q2)
        Out[15]: 'SELECT models.name AS models_name, models.id AS models_id, models.value AS models_value \nFROM models'

    You can use this to check that the query the ORM is constructing looks like
    you expect.

    It can be helpful in debugging.

.. nextslide:: Methods of the Query Object

The methods of the ``Query`` object fall into two rough categories

.. rst-class:: build
.. container::

    .. rst-class:: build

    1.  Methods that return a new ``Query`` object
    2.  Methods that return *scalar* values or *model* instances

    Let's start by looking quickly at a few methods from the second category

.. nextslide:: ``query.get()``

A good example of this category of methods is ``get``, which returns one
instance only.

.. rst-class:: build
.. container::

    It takes a primary key as an argument:

    .. code-block:: ipython

        In [16]: session.query(MyModel).get(1)
        Out[16]: <learning_journal.models.MyModel at 0x105f30208>
        In [17]: session.query(MyModel).get(10)
        In [18]: 


    If no item with that primary key is present, then the method returns
    ``None``

.. nextslide:: ``query.all()``

Another example is one we've already seen.

.. rst-class:: build
.. container::

    ``query.all()`` returns a list of all rows returned by the database:

    .. code-block:: ipython

        In [18]: q1.all()
        Out[18]: [<learning_journal.models.MyModel at 0x105f30208>]

        In [19]: type(q1.all())
        Out[19]: list

    ``query.count()`` returns the number of rows that would have been returned
    by the query:

    .. code-block:: ipython

        In [20]: q1.count()
        Out[20]: 1

.. nextslide:: Creating New Objects

Before getting into the other category, let's learn how to create new objects.

.. rst-class:: build
.. container::

    .. container::

        We can create new instances of our *model* just like normal Python
        objects:

        .. code-block:: ipython

            In [21]: new_model = MyModel(name='fred', value=3)
            In [22]: new_model
            Out[22]: <learning_journal.models.MyModel at 0x105f4af28>

    .. container::

        In this state, the instance is *ephemeral*, our ``session`` knows
        nothing about it:

        .. code-block:: pycon

            In [23]: session.new
            Out[23]: IdentitySet([])

.. nextslide:: Adding Objects to the Session

For the database to know about our new object, we must ``add`` it to the
session:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [24]: session.add(new_model)
        In [25]: session.new
        Out[25]: IdentitySet([<learning_journal.models.MyModel object at 0x105f4af28>])

    We can even bulk-add new objects:

    .. code-block:: ipython

        In [26]: new = []
        In [27]: for name, val in [('bob', 34), ('tom', 13)]:
           ....:     new.append(MyModel(name=name, value=val))
           ....:
        In [28]: session.add_all(new)
        In [29]: session.new
        Out[29]: IdentitySet([<learning_journal.models.MyModel object at 0x105f4af28>,
                              <learning_journal.models.MyModel object at 0x105f4a4a8>,
                              <learning_journal.models.MyModel object at 0x105f30550>])

.. nextslide:: Committing Changes

Up until now, the changes you've made are not permanent.

.. rst-class:: build
.. container::

    In order for these new objects to be saved to the database, the session
    must be ``committed``:

    .. code-block:: ipython

        In [30]: other_session = Session()
        In [31]: other_session.query(MyModel).count()
        Out[31]: 1
        In [32]: session.commit()
        In [33]: other_session.query(MyModel).count()
        Out[33]: 4

    When you are using a ``scoped_session`` in Pyramid, this action is
    automatically handled for you.

    The session that is bound to a particular HTTP request is committed when a
    response is sent back.

    (don't worry if this seems confusing, more to come next week)

.. nextslide:: Altering Objects

You can edit objects that are already part of a session, or that are fetched by
a query.

.. rst-class:: build
.. container::

    Simply change the values of a persisted attribute, the session will know
    it's been updated:

    .. code-block:: ipython
    
        In [34]: new_model
        Out[34]: <learning_journal.models.MyModel at 0x105f4af28>
        In [35]: new_model.name
        Out[35]: 'fred'
        In [36]: new_model.name = 'larry'
        In [37]: session.dirty
        Out[37]: IdentitySet([<learning_journal.models.MyModel object at 0x105f4af28>])

    Commit the session to persist the changes:

    .. code-block:: ipython
    
        In [38]: session.commit()
        In [39]: [model.name for model in other_session.query(MyModel)]
        Out[39]: ['one', 'larry', 'bob', 'tom']

.. nextslide:: Methods Returning Queries

Returning to query methods, a good example of the second type is the ``filter``
method.

.. rst-class:: build
.. container::

    This method allows you to reduce the number of results, based on criteria:

    .. code-block:: ipython
    
        In [40]: [(o.name, o.value) for o in session.query(MyModel).filter(MyModel.value < 20)]
        Out[40]: [('one', 1), ('larry', 3), ('tom', 13)]

.. nextslide:: ``order_by``

Another typical method in this category is ``order_by``:

.. rst-class:: build
.. container::

    .. code-block:: ipython
    
        In [41]: [o.value for o in session.query(MyModel).order_by(MyModel.value)]
        Out[41]: [1, 3, 13, 34]

        In [42]: [o.name for o in session.query(MyModel).order_by(MyModel.name)]
        Out[42]: ['bob', 'larry', 'one', 'tom']

.. nextslide:: Method Chaining

Since methods in this category return ``Query`` objects, they can be safely
*chained* to build more complex queries:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [43]: q1 = session.query(MyModel).filter(MyModel.value < 20)
        In [44]: q1 = q1.order_by(MyModel.name)
        In [45]: [(o.name, o.value) for o in q1]
        Out[45]: [('larry', 3), ('one', 1), ('tom', 13)]

    Note that you can do this inline as well
    (``s.query(Model).filter().order_by()``)

    Also note that when using chained queries like this, no query is actually
    sent to the database until you require a result.


Cleaning Up After Ourselves
---------------------------

When you are experimenting with a new system, you often create data that is
messy or incomplete.

.. rst-class:: build
.. container::

    It's good to remember that none of the information we've persisted to our
    database is vital to us.

    For homework this week we'll be making new models, and the data we have in
    our current database will only get in the way.

    Until you have real production data it is always safe simply to delete the
    database and start over:

    .. code-block:: bash
    
        $ rm learning_journal.sqlite

    You can always re-create it by executing ``initialize_learning_journal_db``

Homework
========

.. rst-class:: left

Okay, that's enough for the moment.

.. rst-class:: build left
.. container::

    You've learned quite a bit about how *models* work in SQLAlchemy

    It's time to put that knowledge to good use.

    For the first part of your assignment this week you will begin to define
    the data model for our learning journal application.

    I'll provide a specification, you define the model required to do the job.

    I'll also ask you to define a few methods to complete the first part of our
    API.

The Model
---------

Our model will be called an ``Entry``. Here's what you need to know:

* It should be stored in a database table called ``entries``
* It should have a primary key field called ``id``
* It should have a ``title`` field which accepts unicode text up to 255 characters in length
* The ``title`` should be unique and it should be impossible to save an
  ``entry`` without a ``title``.
* It should have a ``body`` field which accepts unicode text of any length
  (including none)
* It should have a ``created`` field which stores the date and time the object
  was created.
* It should have an ``edited`` field which stores the date and time the object
  was last edited.

.. nextslide::

* Both the ``created`` and ``edited`` field should default to ``now`` if not
  provided when a new instance is constructed.
* The ``entry`` class should support a classmethod ``all`` that returns all the
  entries in the database, ordered so that the most recent entry is first.
* The ``entry`` class should support a classmethod ``by_id`` that returns a
  single entry, given an ``id``.

Remember that in order to have your new model table created, you will have to
re-run the ``initialize_learning_journal_db`` script after creating your model.

.. nextslide:: Words of Advice

Use the documentation linked in this presentation to assist you.  SQLAlchemy
has fantastic documentation, but it can be a bit overwhelming.  Everything you
require for this assignment is on one or more of the pages linked above.

As you define this new model for our application, make frequent commits to your
github repository. Remember to write meaningful commit messages.

Don't be afraid to start up a Python interpreter and play with your model. Try
things out. Learn how this all works by making mistakes. Remember the
``pshell`` command and how we set up a session once the shell is running.

Errors at the SQL level can sometimes leave your session unusable. To restore
it, use the ``session.rollback()`` method.  You'll lose uncommitted changes,
but you'll gain a session that can be used again.

.. nextslide:: Submitting Your Work

I want to be able to review your code (and you want to be able to share it).

To submit this assignment, you'll need to add this learning_journal repository
to GitHub.

On the GitHub website you can create a new repository.  Set it up to be
completely empty. Name it ``learning_journal`` and give it any description you
like.

When you've created an empty repository in GitHub, you should see a set of
directions for connecting it to a repository that you've already built. Follow
those instructions to connect your emtpy GitHub repository as the ``origin``
remote to your ``learning_journal`` repository on your machine.

Finally, push your ``master`` branch to your new ``origin`` remote on GitHub.

When you are done, send me an email with the URL for your new repository.

.. nextslide::

**Our work next week will assume that you have completed this assignment**

Do not delay working on this until the last moment.

Do not skip this assignment.

Do ask questions frequently via email (use the `class google group`_).

See you next week!

.. _class google group: https://groups.google.com/forum/#!forum/programming-in-python
