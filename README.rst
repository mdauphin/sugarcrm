========
SugarCRM
========

Simple Python client for SugarCRM API.


Example Usage
-------------

.. code-block:: python

    import sugarcrm

    # Connect
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
