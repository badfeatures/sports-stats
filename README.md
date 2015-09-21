# sports-stats

sports-stats is written to make restful API calls to [Stats, LLC](http://www.stats.com/) easier and faster.

sports-stats must be used with Python 2.7 or above.

## Install

To install sports-stats using `pip`:

    pip install sports-stats -U

To manually install sports-stats:

    python setup.py install

To install sports-stats using `pip` from GitHub:

    pip install -e git+git://github.com/sportsy/sports-stats.git#egg=sports-stats


## Example
You can make a simple call with this API wrapper, below is an example to get a MLB team's information. Please refer to the IO docs on Stats for endpoints and data returned.

```python
from sportsstats import StatsAPI

#Get a team's schedule
api = StatsAPI('API_KEY', 'API_SECRET')
resp = api.request('/stats/baseball/mlb/events/teams/:teamId', {'teamId': 251})
print resp.json()
```
The wrapper itself is pretty flexible allowing both rest url parameters and get parameters when passing flags in with the request.

To make requests, you can keep the same structure as the endpoints on Stats documentation and the second argument in the request method is the rest URL params you want to replace with their values. The third argument is the URL get parameters. Both of these method arguments take a *dictionary*.
```python
from sportsstats import StatsAPI

#Get an event's score
api = StatsAPI('API_KEY', 'API_SECRET')
resp = api.request('/stats/baseball/mlb/scores/:eventId', {'eventId': 1234}, {'linescore': 'true'})
print resp.json()
```

```python
from sportsstats import StatsAPI

#Get information about a specific MLB team
api = StatsAPI('API_KEY', 'API_SECRET')
resp = api.request('/stats/baseball/mlb/teams/:teamId', {'teamId': 251})
print resp.json()
```

## Response methods / values
- `resp.headers` returns the headers of the request
- `resp.status_code` returns the status code of the request
- `resp.text()` returns the raw object
- `resp.json()` returns the object in json format

## Testing
We've integrated pytest into our library so you can run your tests. To run your test, all you need to do is run
    
    python setup.py test
    
The test will then run and make API calls to the Stats API, we've put 1 second delay into each call so there won't be any false positives with API rate limiting.

## Need help?
Submit a ticket, we'll be more than happy to help out!

## Useful Links
[Stats IO Docs](http://developer.stats.com/io-docs)  
[Stats Documentation](http://developer.stats.com/docs)  
