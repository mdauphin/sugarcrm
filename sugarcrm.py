#  SugarCRM
#  --------
#  Python client for SugarCRM API.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/sugarcrm
#  License: MIT (see LICENSE file)

__version__ = '0.1-dev'


import base64
import hashlib
import json
import os
import requests


class API:

    def __init__(self, url, username, password, app="Python", lang="en_us"):
        self.url = url
        self.username = username
        self.application = app
        self.language = lang
        result = self.login(username, password)
        self.session_id = result['id']

    def _request(self, method, params):
        data = {
            'method': method,
            'input_type': "JSON",
            'response_type': "JSON",
            'rest_data': json.dumps(params)
        }
        r = requests.post(self.url, data=data)
        if r.status_code == 200:
            return json.loads(r.text)
        raise SugarError("SugarCRM API _request returned status code %d" \
                         % r.status_code)

    def get_available_modules(self, filter="default"):
        """Retrieves a list of available modules in the system."""
        data = [self.session_id, filter]
        results = self._request('get_available_modules', data)['modules']
        ret = []
        for module in results:
            m = Module()
            for key, value in module.items():
                setattr(m, key, value)
            ret.append(m)
        return ret

    def get_document_revision(self):
        raise SugarError("Method not implemented yet.")

    def get_entry(self, module, id, track_view=False):
        """Retrieves a single object based on object ID."""
        data = [self.session_id, module, id, [], [], track_view]
        result = self._request('get_entry', data)['entry_list'][0]
        obj = SugarObject()
        obj.module = module
        for key in result['name_value_list']:
            if isinstance(key, dict):
                # No object found
                return None
            setattr(obj, key, result['name_value_list'][key]['value'])
        return obj

    def get_entries(self, module, ids, track_view=False):
        """Retrieves a list of objects based on specified object IDs."""
        if not isinstance(ids, list):
            ids = [ids,]
        data = [self.session_id, module, ids, [], [], track_view]
        results = self._request('get_entries', data)['entry_list']
        ret = []
        for result in results:
            obj = SugarObject()
            obj.module = module
            for key in result['name_value_list']:
                if isinstance(key, dict):
                    # No objects found
                    return []
                setattr(obj, key, result['name_value_list'][key]['value'])
            ret.append(obj)
        return ret

    def get_entries_count(self):
        raise SugarError("Method not implemented yet.")

    def get_entry_list(self, q):
        """Retrieves a list of objects based on query specifications."""
        data = [self.session_id, q.module, q.query, "", 0, [], [], 0, 0, False]
        results = self._request('get_entry_list', data)['entry_list']
        ret = []
        for result in results:
            obj = SugarObject()
            obj.module = q.module
            for key in result['name_value_list']:
                setattr(obj, key, result['name_value_list'][key]['value'])
            ret.append(obj)
        return ret

    def get_language_definition(self):
        raise SugarError("Method not implemented yet.")

    def get_last_viewed(self):
        raise SugarError("Method not implemented yet.")

    def get_modified_relationships(self):
        raise SugarError("Method not implemented yet.")

    def get_module_fields(self):
        raise SugarError("Method not implemented yet.")

    def get_module_fields_md5(self):
        raise SugarError("Method not implemented yet.")

    def get_module_layout(self):
        raise SugarError("Method not implemented yet.")

    def get_note_attachment(self):
        raise SugarError("Method not implemented yet.")

    def get_quotes_pdf(self):
        raise SugarError("Method not implemented yet.")

    def get_relationships(self):
        raise SugarError("Method not implemented yet.")

    def get_report_entries(self):
        raise SugarError("Method not implemented yet.")

    def get_report_pdf(self):
        raise SugarError("Method not implemented yet.")

    def get_server_info(self):
        raise SugarError("Method not implemented yet.")

    def get_upcoming_activities(self):
        raise SugarError("Method not implemented yet.")

    def get_user_id(self):
        raise SugarError("Method not implemented yet.")

    def get_user_team_id(self):
        raise SugarError("Method not implemented yet.")

    def job_queue_cycle(self):
        raise SugarError("Method not implemented yet.")

    def job_queue_next(self):
        raise SugarError("Method not implemented yet.")

    def job_queue_run(self):
        raise SugarError("Method not implemented yet.")

    def login(self, username, password, app="Python", lang="en_us"):
        """Logs a user into the SugarCRM application."""
        data = [
            {
                'user_name': username,
                'password': hashlib.md5(password).hexdigest()
            },
            app,
            [{
                'name': "language",
                'value': lang
            }]
        ]
        return self._request('login', data)

    def logout(self):
        raise SugarError("Method not implemented yet.")

    def oauth_access(self):
        raise SugarError("Method not implemented yet.")

    def seamless_login(self):
        raise SugarError("Method not implemented yet.")

    def search_by_module(self):
        raise SugarError("Method not implemented yet.")

    def set_campaign_merge(self):
        raise SugarError("Method not implemented yet.")

    def set_document_revision(self, doc, f, revision=None):
        """Creates a new document revision for a specific document record."""
        if isinstance(f, str) or isinstance(f, unicode):
            f = open(f, 'rb')
            fields = {
                'id': doc.id,
                'filename': f.name.split(os.sep)[-1],
                'file': base64.b64encode(f.read()),
                'revision': revision or doc.revision,
            }
            data = [self.session_id, fields]
            return self._request('set_document_revision', data)

    def set_entries(self):
        raise SugarError("Method not implemented yet.")

    def set_entry(self, obj):
        """Creates or updates a specific object."""
        data = [self.session_id, obj.module, obj.fields]
        result = self._request('set_entry', data)
        obj.id = result['id']
        return obj

    def set_note_attachment(self, note, f):
        """Creates an attachmentand associates it to a specific note object."""
        if isinstance(f, str) or isinstance(f, unicode):
            f = open(f, 'rb')
        fields = {
            'id': note.id,
            'filename': f.name,
            'file': base64.b64encode(f.read())
        }
        data = [self.session_id, fields]
        return self._request('set_note_attachment', data)

    def set_relationship(self, parent, child, delete=False):
        """Sets relationships between two records."""
        delete = int(delete)
        related_ids = [child.id,]
        name_value_list = [{
            'name': "%s_%s" % (parent.module.lower(), child.module.lower()),
            'value': 'Other',
        }]
        data = [self.session_id, parent.module, parent.id,
                child.module.lower(), related_ids, name_value_list, delete]
        return self._request('set_relationship', data)

    def set_relationships(self):
        raise SugarError("Method not implemented yet.")

    def snip_import_emails(self):
        raise SugarError("Method not implemented yet.")

    def snip_update_contacts(self):
        raise SugarError("Method not implemented yet.")


class SugarObject:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def fields(self):
        params = []
        for key, value in self.__dict__.items():
            if not value:
                continue
            params.append({
                'name': key,
                'value': value
            })
        return params

    @property
    def query(self):
        q = ""
        for key, value in self.__dict__.items():
            if not value:
                continue
            if q:
                q += "AND "
            if value.find('%') >= 0:
                q += "%s.%s LIKE '%s' " % (self.module.lower(), key, str(value))
            else:
                q += "%s.%s='%s' " % (self.module.lower(), key, str(value))
        return q


class Call(SugarObject):
    module = "Calls"


class Campaign(SugarObject):
    module = "Campaigns"


class Contact(SugarObject):
    module = "Contacts"


class Document(SugarObject):
    module = "Documents"


class Email(SugarObject):
    module = "Emails"


class Lead(SugarObject):
    module = "Leads"


class Module(SugarObject):
    module = "Modules"


class Note(SugarObject):
    module = "Notes"


class Opportunity(SugarObject):
    module = "Opportunities"


class Product(SugarObject):
    module = "Products"


class Prospect(SugarObject):
    module = "Prospects"


class ProspectList(SugarObject):
    module = "ProspectLists"


class Quote(SugarObject):
    module = "Quotes"


class Report(SugarObject):
    module = "Reports"


class SugarError(Exception):
    pass
