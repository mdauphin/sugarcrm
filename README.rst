========
SugarCRM
========

Python client for SugarCRM API.


Example Usage
-------------

.. code-block:: python

    import sugarcrm

    # Connect
    url = "http://your-sugarcrm-domain/service/v4/rest.php"
    sugar = sugarcrm.API(url, username, password)

    # Create a new note
    note = sugarcrm.Note("Test Note")

    # Save note
    sugar.set_entry(note)

    # Add attachment to note
    sugar.set_note_attachment(note, "sugarcrm.py")

    # Query for all notes that have a name that begins with "Test"
    note_query = sugarcrm.Note("Test%")
    results = sugar.get_entry_list(note_query)

    # Query for all contacts with the first name "Mylee"
    contact_query = sugarcrm.Contact()
    contact_query.first_name = "Mylee"
    results = sugar.get_entry_list(contact_query)

    # Get the email address for the user assigned to an Opportunity
    op = sugar.get_entry("Opportunities", "82f72939-735e-53a2-0944-5418c4edae2a")
    user = sugar.get_entry("Users", op.assigned_user_id)
    print user.email1

    # Change the status of an Opportunity
    op = sugarcrm.Opportunity()
    op.id = "82f72939-735e-53a2-0944-5418c4edae2a"
    op.sales_stage = "Approved"
    sugar.set_entry(op)


Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install sugarcrm

If the above fails, please use easy_install instead:

.. code-block:: bash

    $ easy_install sugarcrm


SugarCRM Objects
----------------

.. code-block:: python

    >>> contact = sugarcrm.Contact()
    >>> print contact.module
    "Contacts"

    >>> note = sugarcrm.Note()
    >>> print note.module
    "Notes"

    >>> opportunity = sugarcrm.Opportunity()
    >>> print opportunity.module
    "Opportunities"


API Object
----------

class sugarcrm.API(url, username, password)
    The main class used to connect to the SugarCRM API and make quests with.

.. code-block:: python

    url = "http://your-sugarcrm-domain/service/v4/rest.php"
    sugar = sugarcrm.API(url, username, password)


API Methods
-----------

sugar.get_entry(module, id, track_view=False)

.. code-block:: python

    note = sugar.get_entry("Notes", "f0c78aab-e051-174a-12aa-5439a7146977")
    print note.name

sugar.get_entries(module, ids, track_view=False)

.. code-block:: python

    ids = [
        "f0c78aab-e051-174a-12aa-5439a7146977",
        "32f02fj2-4ggn-4nnf-fs33-f3fh3f93n333",
        "82f72939-735e-53a2-0944-5418c4edae2a",
    ]
    notes = sugar.get_entries("Notes", ids)
    for note in notes:
        print note.name

sugar.get_entry_list(query_object)

.. code-block:: python

    # Get a list of all notes with a name that begins with "Test"
    nq = sugarcrm.Note()
    note.name = "Test%"
    notes = sugar.get_entry_list(nq)
    for note in notes:
        print note.name

sugar.set_entry(obj)

.. code-block:: python

    note = sugarcrm.Note()
    note.name = "Test Note"
    sugar.set_entry(note)
    print note.id

sugar.set_note_attachment(note, f)

.. code-block:: python

    with open("test1.pdf") as pdf_file:
        sugar.set_note_attachment(note1, pdf_file)
    sugar.set_note_attachment(note2, "test2.pdf")
    print note1.filename, note2.filename


Development Version
-------------------

The latest development version can be installed directly from GitHub:

.. code-block:: bash

    $ pip install --upgrade https://github.com/ryanss/sugarcrm/tarball/master


Contributions
-------------

.. _issues: https://github.com/ryanss/sugarcrm/issues
.. __: https://github.com/ryanss/sugarcrm/pulls

Issues_ and `Pull Requests`__ are always welcome.


License
-------

.. __: https://github.com/ryanss/sugarcrm/raw/master/LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
