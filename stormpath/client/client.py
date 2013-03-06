__author__ = 'ecrisostomo'

from stormpath.ds.data_store import DataStore
from stormpath.http.http_client_request_executor import HttpClientRequestExecutor
from stormpath.resource.tenants import Tenant

class Client:

    def __init__(self, api_key, base_url):
        request_executor = HttpClientRequestExecutor(api_key)
        self.data_store = DataStore(request_executor, base_url)

    @property
    def current_tenant(self):
        return self.data_store.get_resource('/tenants/current', Tenant)

class ApiKey:

    def __init__(self, id, secret):
        self.id = id
        self.secret = secret