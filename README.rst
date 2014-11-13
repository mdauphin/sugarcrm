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

    # Extract all non-empty email fields from all Contacts in SugarCRM
    emails = set()
    contact_query = sugarcrm.Contact()  # No filters provider finds all objects
    contact_count = sugar.get_entries_count(contact_query, deleted=True)
    print "Extracting emails from %d Contacts" % contact_count
    # Grab 100 Contact objects at a time from SugarCRM
    for offset in range(0, count, 100):
        contacts = sugar.get_entry_list(contact_query, deleted=True,
                                        max_results=100, offset=offset)
        for contact in contacts:
            for field in dir(contact):
                if field.find("email") >= 0 and getattr(contact, field, "").find("@") >= 0:
                    emails.add(getattr(contact, field).lower())
    print "Found %d emails" % len(emails)



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

get_available_modules(filter="default")
    Retrieves a list of available modules in the system.
    Possible filter values: "default", "mobile", "all"

.. code-block:: python

    modules = sugar.get_available_modules()
    for m in modules:
        print m.module_key

get_entry(module, object_id, links=dict(), track_view=False)
    Retrieves a single object based on object ID.

.. code-block:: python

    note = sugar.get_entry("Notes", "f0c78aab-e051-174a-12aa-5439a7146977")
    print note.name

    # Get a lead and specific fields from linked contacts in one query
    links = { 'Contacts': ['id', 'first_name', 'last_name'] }
    lead = sugar.get_entry("Leads", "d7dac88d-ce33-d98a-da8b-5418bba9e664",
                           links=links)
    for c in lead.contacts:
        print c.id, c.first_name, c.last_name

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

get_entries_count(query_object, deleted=False)
    Retrieves a count of beans based on query specifications.

.. code-block:: python

    # Get a count of all Contacts with a first name of "Fred"
    # and include Contacts that have been deleted
    contact_query = sugarcrm.Contact(first_name="Fred")
    contacts = sugar.get_entries_count(contact_query, deleted=True)
    for contact in contacts:
        print contact.first_name, contact.last_name

get_entry_list(query_object, field_list=[], order_by="", max_results=0, offset=0, deleted=False, favorites=False)
    Retrieves a list of objects based on query specifications.

.. code-block:: python

    # Get a list of all Notes with a name that begins with "Test"
    note_query = sugarcrm.Note(name="Test%")
    notes = sugar.get_entry_list(note_query)
    for note in notes:
        print note.name

login(username, password, app="Python", lang="en_us")
    Logs a user into the SugarCRM application.

set_document_revision(document, file)
    Creates a new document revision for a specific document record.

.. code-block:: python

    doc = sugarcrm.Document(document_name="Test Doc", revision=1)
    sugar.set_entry(doc)
    sugar.set_document_revision(doc, "/path/to/test.pdf")


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

set_relationship(parent, child, delete=False)
    Sets the relationships between two records.

.. code-block:: python

    doc = sugarcrm.Document(document_name="Test Doc", revision=1)
    sugar.set_entry(doc)
    sugar.set_document_revision(doc, "/path/to/test.pdf")
    opportunity = sugar.get_entry("Opportunities", "5b671886-cfe4-36f5-fa9d-5418a24e4aca")
    sugar.set_relationship(opportunity, doc)

get_document_revision()
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

set_entries()
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
