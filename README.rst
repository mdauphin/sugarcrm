========
SugarCRM
========

Simple Python client for SugarCRM API.


Example Usage
-------------

.. code-block:: python

    >>> import sugarcrm
    >>> # Connect
    >>> sugar = sugarcrm.API(url, username, password)
    >>> # Create a new note
    >>> note = sugarcrm.Note("Test Note")
    >>> # Save note
    >>> sugar.set_entry(note)
    >>> # Add attachment to note
    >>> sugar.set_note_attachment(note, "sugarcrm.py")
    >>> # Query for all notes that have a name that begins with "Test"
    >>> note_query = sugarcrm.Note("Test%")
    >>> results = sugar.get_entry_list(note_query)
