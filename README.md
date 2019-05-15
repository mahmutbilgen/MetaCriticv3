
### This is a test-1 TEXT written in Windows CR LF UTF8 
# Parsing  Metacritic Test / REST API
## Task:  

#### Write a proof of application in which scraping a web site and service it in REST API server

Application can do the following:

1. Parse the HTML for the "Top Games " on Metacritic's Games page: `http://www.metacritic.com/game`.

2. Expose a REST API for retrieving top games. There should be 2 exposed methods:

## GET   /games
An HTTP `GET` request to `/games` returns all top games on the Metacritic page as an array of JSON objects. For example:


 ```json
[
  {
    "title": "Persona 5",
    "score": 94
  }, 
  {
    "title": "Horizon:ZeroDawn",
    "score": 89
   }
]
```

## GET /games/<title> 

 An HTTP GET request to `/games/<title>` returns JSON for a specific game that matches the corresponding game title. 
 For example, an HTTP GET to `/games/Nioh` should return an individual JSON object for Nioh:
 
```json
{
   "title":"Nioh", 
   "score": 88
}
```

### Deliverables:

1. Provide the source-code, which satisfies the requirements above. 
2. Include unit tests to test the functionality of the source code.
3. Provide “README” style documentation on how to run the code and execute the unit tests.

### Python 3

```
pip3 install -r requirements.txt
python3 main.py
```
### Run with Docker

```
docker run -it -p 8080:8080 mbilgen/metacriticv3:latest
```

### Send test requests

```
curl http://127.0.0.1:8080/games # returns top10 as json
curl http://127.0.0.1:8080/games/Undertale # returns score for game if it is in top 10
```
-OR- you can call from your internet browser

## Unittests

To run unittests:
```
python3 -m unittest discover -v
```
Following test were created
