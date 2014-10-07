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
        result = self.api('login', data)
        self.session_id = result['id']

    def request(self, method, params):
        data = {
            'method': method,
            'input_type': "JSON",
            'response_type': "JSON",
            'rest_data': json.dumps(params)
        }
        r = requests.post(self.url, data=data)
        return json.loads(r.text)

    def get_entry_list(self, obj):
        data = [self.session_id, obj.type, obj.query, "", 0, [], [], 2, 0, False]
        return self.request('get_entry_list', data)

    def set_entry(self, obj):
        data = [self.session_id, obj.type, obj.fields]
        result = self.request('set_entry', data)
        obj.id = result['id']

    def set_note_attachment(self, obj, f):
        pass


class SugarObject:

    def __init__(self, name):
        self.name = name

    @property
    def fields(self):
        params = []
        for key, value in self.__dict__.items():
            params.append({
                'name': key,
                'value': value
            })
        return params

    @property
    def query(self):
        q = ""
        for key, value in self.__dict__.items():
            if q:
                q += "AND "
            if value.find('%') >= 0:
                q += "%s.%s LIKE '%s' " % (self.type.lower(), key, str(value))
            else:
                q += "%s.%s='%s' " % (self.type.lower(), key, str(value))
        print q
        return q


class Note(SugarObject):

    @property
    def type(self):
        return "Notes"
