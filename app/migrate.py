from main import Movies,db
import json
f = open('data.json')
data = json.load(f)
db.create_all()
for dat in data:
    movie = Movies(popularity= dat['99popularity'],director = dat['director'], genre = dat['genre'],imdb_score = dat['imdb_score'],name = dat['name'])
    db.session.add(movie)
    db.session.commit()
