import logging


class StatsError(Exception):

    """Base class for exceptions"""
    pass


class StatsConnectionError(StatsError):

    """Raised when the connection needs to be re-established"""

    def __init__(self, value):
        super(Exception, self).__init__(value)
        logging.warning('%s %s' % (type(value), value))


class StatsRequestError(StatsError):

    """Raised when request fails"""

    def __init__(self, status_code):
        if status_code >= 500:
            msg = 'Stats internal error (you may re-try)'
        else:
            msg = 'Stats request failed'
        logging.info('Status code %d: %s' % (status_code, msg))
        super(Exception, self).__init__(msg)
        self.status_code = status_code
        
    def __str__(self):
        return '%s (%d)' % (self.args[0], self.status_code)