import requests
import hashlib
import socket
import ssl
import time

from requests.exceptions import ConnectionError, ReadTimeout, SSLError
from urllib3.exceptions import ReadTimeoutError, ProtocolError
from .exceptions import *


BASE_URL = 'http://api.stats.com/v1'
REST_TIMEOUT = 30.0
API_SECRET = None


class StatsAPI(object):

    """Access REST API or Streaming API resources.
    :param key: Stats application key
    :param secret: Stats application secret
    :param accept: Stats accept type (json, xml)
    """

    api_key = None
    api_secret = None
    api_accept = None

    def __init__(
            self,
            key=None,
            secret=None,
            accept='json'):
        """Initialize with your application credentials"""

        if not all([key, secret]):
            raise Exception('Missing authentication parameter')

        self.api_key = key
        self.api_secret = secret
        self.api_accept = accept

    def _prepare_url(self, domain, path, params=None):
        auth = self.generate_auth()
        url = '{}{}?api_key={}&sig={}'.format(domain, path, auth['api_key'], auth['sig'])
        if params is not None:
            for k in params:
                url += '&{}={}'.format(str(k), str(params[k]))
        return url

    def _get_endpoint(self, resource, params=None):
        """Substitute any parameters in the resource path with :PARAM."""
        if ':' in resource:
            if params is not None:
                for k in params:
                    try:
                        url_param = ':%s' % k
                        resource = resource.replace(url_param, str(params[k]))
                    except:
                        pass
                return resource, resource

            else:
                return resource, resource

        else:
            return resource, resource

    def request(self, resource, rest_params=None, params=None, files=None):
        """Request a Stats REST API .
        :param resource: A valid Stats endpoint
        :param params: Dictionary with endpoint parameters or None (default)
        :returns: StatsResponse
        :raises: StatsConnectionError
        """
        resource, endpoint = self._get_endpoint(resource, rest_params)
        # if endpoint not in ENDPOINTS:
        #    raise Exception('Endpoint "%s" unsupported' % endpoint)

        # payload = {'key1': 'value1', 'key2': 'value2'}
        # r = requests.get("http://httpbin.org/get", params=payload)
        session = requests.Session()
        # session.headers = {'User-Agent': USER_AGENT}
        method = 'GET'
        subdomain = BASE_URL
        url = self._prepare_url(subdomain, resource, params)
        session.stream = False
        timeout = REST_TIMEOUT
        try:
            r = session.request(
                method,
                url,
                timeout=timeout,
                files=files,
            )
        except (ConnectionError, ProtocolError, ReadTimeout, ReadTimeoutError,
                SSLError, ssl.SSLError, socket.error) as e:
            raise StatsConnectionError(e)
        return StatsResponse(r)

    def generate_auth(self):
        """Returns the dictionary for the authentication get params
        """
        return {'accept': self.api_accept, 'api_key': self.api_key, 'sig': self.generate_sig()}

    def generate_sig(self):
        """Returns the SHA256 signature for making requests
        """
        timestamp = int(time.time())
        hash_it = '{}{}{}'.format(self.api_key, self.api_secret, timestamp)
        return hashlib.sha256(hash_it).hexdigest()


class StatsResponse(object):

    """Response from either a REST API call.
    :param response: The requests.Response object returned by the API call
    """

    def __init__(self, response):
        self.response = response

    @property
    def headers(self):
        """:returns: Dictionary of API response header contents."""
        return self.response.headers

    @property
    def status_code(self):
        """:returns: HTTP response status code."""
        return self.response.status_code

    @property
    def text(self):
        """:returns: Raw API response text."""
        return self.response.text

    @property
    def url(self):
        """:returns: Raw API response url."""
        return self.response.url

    def json(self):
        """:returns: response as JSON object."""
        return self.response.json()
