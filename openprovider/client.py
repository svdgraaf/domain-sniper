from .dicttoxml import dicttoxml
import collections
import xmltodict
import requests

class OpenProviderClient:
    auth = {}
    methods = [
        'createCustomerRequest',
        'checkDomainRequest',
        'createDomainRequest',
    ]

    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth

    def __getattr__(self, name):
        if name not in self.methods:
            raise AttributeError(name)

        def wrapper(name=name, *args, **kwargs):
            return self._process_call(self, name, *args, **kwargs)
        return wrapper

    def _process_call(self, method, *args, **kwargs):
        method = args[0]
        args = args[1:]

        data = collections.OrderedDict()
        data['credentials'] = self.auth
        data[method] = kwargs

        xml = dicttoxml(data, custom_root='openXML', attr_type=False)
        response = self._send_request(xml)
        data = self._parse_response(response.content)
        return data

    def _send_request(self, data):
        response = requests.post(self.base_url, data=data)
        return response

    def _parse_response(self, xml):
        # cleanup the weird OpenProvider response into sane python objects
        data = xmltodict.parse(xml)
        if int(data['openXML']['reply']['code']) != 0:
            raise Exception(data['openXML']['reply']['desc'])

        reply = data['openXML']['reply']['data']

        if reply.keys() == ['array']:
            data = []
            rows = reply['array']['item']
            try:
                rows.items() # this will fail on 1 item
                row = dict(rows)
                data = [row]
            except:
                for row in rows:
                    data.append(dict(row))
            return data
        else:
            # we got an object
            return dict(data)
        return data

    def _parse_dict(self, data):
        data
