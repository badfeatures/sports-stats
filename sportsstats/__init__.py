__title__ = 'Stats LLC API Wrapper'
__version__ = '0.0.1'
__author__ = 'Sportsy, Inc.'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Sportsy, Inc.'

import logging


# No logging unless the client provides a handler,
logging.getLogger(__name__).addHandler(logging.NullHandler())

try:
    from .api import StatsAPI, StatsResponse
    from .exceptions import StatsConnectionError, StatsError, StatsRequestError
except:
    pass


__all__ = [
    'StatsAPI',
    'StatsResponse',
    'StatsConnectionError',
    'StatsError',
    'StatsRequestError'
]