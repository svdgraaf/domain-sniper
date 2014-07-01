import requests
from openprovider import api

client = api('https://api.openprovider.eu', auth={'username':'foo','hash':'bar'})
domains = [
    {
        'name': 'example',
        'extension': 'com',
    },
]
data = client.checkDomainRequest(domains=domains)
print data[0]['status']
