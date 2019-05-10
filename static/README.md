
# Parsing​ ​Metacritic​ ​Test / REST API
# Task:

Write an application in which can do the following:

1. Parse the HTML for the "Top Playstation 4 Games (By Metascore)" on Metacritic's PS4 page: `http://www.metacritic.com/game/playstation-4`.

2. Expose a REST API for retrieving top PS4 games. There should be 2 exposed methods:

## GET​​ ​​/games
An​ ​HTTP​ `​GET`​ ​request​ ​to​ `​​/games`​​ ​returns​ ​all​ ​top​ ​PS4​ ​games​ ​on​ ​the​ ​Metacritic page​ ​as​ ​an​ ​array​ ​of​ ​JSON​ ​objects.​ ​For​ ​example:


 ```json
[
  {
    "title": "Persona​ ​5",
    "score": 94
  }, 
  {
    "title": "Horizon:​ ​Zero​ ​Dawn",
    "score": 89
   }
]
```

## GET​​ ​​/games/<title> 
 An​ ​HTTP​ ​GET​ ​request​ ​to​ ​​`/games/​<title>`​​ ​returns​ ​JSON​ ​for​ ​a​ ​specific​ ​game that​ ​matches​ ​the​ ​corresponding​ ​game​ ​title.​ ​
 For​ ​example,​ ​an​ ​HTTP​ ​GET​ ​to `/games/Nioh​​` ​should​ ​return​ ​an​ ​individual​ ​JSON​ ​object​ ​for​ ​Nioh:
 
```json
{
​ ​​ ​​ ​​"title":​​"Nioh", 
​​ ​​ ​​ ​​"score":​ ​88
}
```

### Deliverables:

1. Provide​ ​the​ ​source-code,​ ​which​ ​satisfies​ ​the​ ​requirements​ ​above.​ ​Do​ ​​not place​ ​this​ ​code​ ​on​ ​a​ ​public​ ​source​ ​code​ ​repository​ ​such​ ​as​ ​GitHub.
2. Include​ ​unit​ ​tests​ ​to​ ​test​ ​the​ ​functionality​ ​of​ ​the​ ​source​ ​code.
3. Provide​ ​“README”​ ​style​ ​documentation​ ​on​ ​how​ ​to​ ​run​ ​the​ ​code​ ​and​ ​execute the​ ​unit​ ​tests.

### Time tracking
I started working on this task Monday,  and finished it Wednesday evening. In general spent 5-7 hours, I think. I did some research on the web

 - Spent approximately 2 hour looking into Metacritic site, their page structure, googling for API providers for metacritic. 
 - Another couple hours I spent reading about BeautifulSoup and  Flask  (I never used any of them before, so concepts were a bit unusual for me)
 - Last 4 hours I was testing and writing this code. 
 - 1  hour for Readme, unittest and git repo.

### Python 3

```
pip3 install -r requirements.txt
python3 main.py
```

### Send test requests

```
curl http://127.0.0.1:8080/games # returns top10 as json
curl http://127.0.0.1:8080/games/Undertale # returns score for game if it is in top 10
```

## Unittests

To run unittests:
```
python3 -m unittest discover -v
```
Following test were created
