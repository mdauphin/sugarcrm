==========================
SugarCRM API Python Client
==========================

Simple Python client for SugarCRM API.


Example Usage
-------------

.. code-block:: python

    >>> import sugarcrm
    >>> sugar = sugarcrm.API(url, username, password)
    >>> note = sugarcrm.Note("Test Note")
    >>> sugar.set_entry(note)
    >>> note_query = sugarcrm.Note("Test%")
    >>> results = sugar.get_entry_list(note_query)
