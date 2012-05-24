CacheInvalidationTester
=======================

Tool to Test Cache Invalidation scenarios

To run the tests:
```bash
python server.py [portnumber]
```
portnumber defaults to 8000, if you don't specify it.

Open a browser to http://localhost:8000
        

#Test 0
This test checks to make sure that two back to back GET requests are correctly cached.

1. GET data.json
2. GET data.json

This means the first GET comes from the server (or cache depending on what else has happend) and the second one must come from the browser cache.


#Test 1
This test is meant to check to make sure that a POST invalidates the local cache so it does:

1. GET data.json
2. POST data.json
3. GET data.json

* Step one's GET should come from the server (or cache depending on what else has happend)
* Step two's POST should always go to the server
* Step three's GET should always come from the server

#Currently Status:

##Test 0 Results:

###Passing

    Chrome
    Firefox
    Safari

##Test 1 Results:

###Passing

    Firefox

###Failing
  
    Chrome
    Safari