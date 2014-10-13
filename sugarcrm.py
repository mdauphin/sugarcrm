import base64
import hashlib
import json
import requests


class API:

    def __init__(self, url, username, password):
        self.url = url
        data = [{
            'user_name': username,
            'password': hashlib.md5(password).hexdigest(),
            'version': "1"
        }]
        result = self.request('login', data)
        self.session_id = result['id']

    def request(self, method, params):
        data = {
            'method': method,
            'input_type': "JSON",
            'response_type': "JSON",
            'rest_data': json.dumps(params)
        }
        r = requests.post(self.url, data=data)
        if r.status_code == 200:
            return json.loads(r.text)
        raise SugarError("SugarCRM API request returned status code %d" \
                         % r.status_code)

    def get_entry(self, module, id, track_view=False):
        data = [self.session_id, module, id, [], [], track_view]
        result = self.request('get_entry', data)['entry_list'][0]
        obj = SugarObject()
        obj.type = module
        for key in result['name_value_list']:
            setattr(obj, key, result['name_value_list'][key]['value'])
        return obj

    def get_entries(self, module, ids, track_view=False):
        if not isinstance(ids, list):
            ids = [ids,]
        data = [self.session_id, module, ids, [], [], track_view]
        results = self.request('get_entries', data)['entry_list']
        ret = []
        for result in results:
            obj = SugarObject()
            obj.type = module
            for key in result['name_value_list']:
                setattr(obj, key, result['name_value_list'][key]['value'])
            ret.append(obj)
        return ret

    def get_entry_list(self, q):
        data = [self.session_id, q.type, q.query, "", 0, [], [], 0, 0, False]
        results = self.request('get_entry_list', data)['entry_list']
        ret = []
        for result in results:
            obj = SugarObject()
            obj.type = q.type
            for key in result['name_value_list']:
                setattr(obj, key, result['name_value_list'][key]['value'])
            ret.append(obj)
        return ret

    def set_entry(self, obj):
        data = [self.session_id, obj.type, obj.fields]
        result = self.request('set_entry', data)
        obj.id = result['id']
        return obj

    def set_note_attachment(self, note, f):
        if isinstance(f, str):
            f = open(f, 'rb')
        fields = {
            'id': note.id,
            'filename': f.name,
            'file': base64.b64encode(f.read())
        }
        data = [self.session_id, fields]
        return self.request('set_note_attachment', data)


class SugarObject:

    def __init__(self, name=None):
        self.name = name

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
                q += "%s.%s LIKE '%s' " % (self.type.lower(), key, str(value))
            else:
                q += "%s.%s='%s' " % (self.type.lower(), key, str(value))
        return q


class Contact(SugarObject):
    type = "Contacts"


class Opportunity(SugarObject):
    type = "Opportunities"


class Note(SugarObject):
    type = "Notes"


class SugarError(Exception):
    pass
