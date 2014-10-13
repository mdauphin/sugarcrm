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
    note = sugarcrm.Note(name="Test Note")

    # Save note
    sugar.set_entry(note)

    # Add attachment to note
    sugar.set_note_attachment(note, "sugarcrm.py")

    # Query for all notes that have a name that begins with "Test"
    note_query = sugarcrm.Note(name="Test%")
    results = sugar.get_entry_list(note_query)

    # Query for all contacts with the first name "Mylee"
    contact_query = sugarcrm.Contact(first_name="Mylee")
    results = sugar.get_entry_list(contact_query)

    # Get the email address for the user assigned to an Opportunity
    op = sugar.get_entry("Opportunities", "82f72939-735e-53a2-0944-5418c4edae2a")
    user = sugar.get_entry("Users", op.assigned_user_id)
    print user.email1

    # Change the status of an Opportunity
    op = sugarcrm.Opportunity(id="82f72939-735e-53a2-0944-5418c4edae2a")
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

class sugarcrm.API(url, username, password, app="Python", lang="en_us")
    The main class used to connect to the SugarCRM API and make quests with.

.. code-block:: python

    url = "http://your-sugarcrm-domain/service/v4/rest.php"
    sugar = sugarcrm.API(url, username, password)


API Methods
-----------

get_entry(module, object_id, track_view=False)
    Retrieves a single object based on object ID.

.. code-block:: python

    note = sugar.get_entry("Notes", "f0c78aab-e051-174a-12aa-5439a7146977")
    print note.name

get_entries(module, object_ids, track_view=False)
    Retrieves a list of objects based on specified object IDs.

.. code-block:: python

    ids = [
        "f0c78aab-e051-174a-12aa-5439a7146977",
        "32f02fj2-4ggn-4nnf-fs33-f3fh3f93n333",
        "82f72939-735e-53a2-0944-5418c4edae2a",
    ]
    notes = sugar.get_entries("Notes", ids)
    for note in notes:
        print note.name

get_entry_list(query_object)
    Retrieves a list of objects based on query specifications.

.. code-block:: python

    # Get a list of all notes with a name that begins with "Test"
    nq = sugarcrm.Note(name="Test%")
    notes = sugar.get_entry_list(nq)
    for note in notes:
        print note.name

login(username, password, app="Python", lang="en_us")
    Logs a user into the SugarCRM application.

set_entry(sugar_object)
    Creates or updates a specific object.

.. code-block:: python

    note = sugarcrm.Note()
    note.name = "Test Note"
    note.assigned_user_id = "82f72939-735e-53a2-0944-5418c4edae2a"
    sugar.set_entry(note)
    print note.id

set_note_attachment(note, attachment)
    Creates an attachmentand associates it to a specific note object.

.. code-block:: python

    with open("test1.pdf") as pdf_file:
        sugar.set_note_attachment(note1, pdf_file)
    sugar.set_note_attachment(note2, "test2.pdf")
    print note1.filename, note2.filename

get_available_modules()
    Method not implemented yet.

get_document_revision()
    Method not implemented yet.

get_entries_count()
    Method not implemented yet.

get_language_definition()
    Method not implemented yet.

get_last_viewed()
    Method not implemented yet.

get_modified_relationships()
    Method not implemented yet.

get_module_fields()
    Method not implemented yet.

get_module_fields_md5()
    Method not implemented yet.

get_module_layout()
    Method not implemented yet.

get_note_attachment()
    Method not implemented yet.

get_quotes_pdf()
    Method not implemented yet.

get_relationships()
    Method not implemented yet.

get_report_entries()
    Method not implemented yet.

get_report_pdf()
    Method not implemented yet.

get_server_info()
    Method not implemented yet.

get_upcoming_activities()
    Method not implemented yet.

get_user_id()
    Method not implemented yet.

get_user_team_id()
    Method not implemented yet.

job_queue_cycle()
    Method not implemented yet.

job_queue_next()
    Method not implemented yet.

job_queue_run()
    Method not implemented yet.

logout()
    Method not implemented yet.

oauth_access()
    Method not implemented yet.

seamless_login()
    Method not implemented yet.

search_by_module()
    Method not implemented yet.

set_campaign_merge()
    Method not implemented yet.

set_document_revision()
    Method not implemented yet.

set_entries()
    Method not implemented yet.

set_relationship()
    Method not implemented yet.

set_relationships()
    Method not implemented yet.

snip_import_emails()
    Method not implemented yet.

snip_update_contacts()
    Method not implemented yet.


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
