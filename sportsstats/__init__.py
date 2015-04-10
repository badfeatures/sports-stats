from .api import StatsAPI
from .api import StatsResponse
from .exceptions import StatsConnectionError
from .exceptions import StatsError
from .exceptions import StatsRequestError

import logging


# No logging unless the client provides a handler,
logging.getLogger(__name__).addHandler(logging.NullHandler())

__title__ = 'sportsstats'
__author__ = 'Sportsy, Inc.'
