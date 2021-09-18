from app import app,db
from app.models import Movies,User
from flask import make_response,jsonify,request,render_template
from flask_login.utils import login_required, login_user
import json
from flask_login import logout_user, current_user
from app.form import LoginForm, Search

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get',methods=['GET'])
def get_all():
    try:
        movies = Movies.query.all()
        
        for movie in movies:
            data = jsonify( [{'99popularity': o.popularity,
                           'director': o.director ,'genre':o.genre,'imdb_score':o.imdb_score, 'name':o.name} for o in movies] )
        
        return make_response(data,200)
    except Exception as e:
        return json.dumps({'error occured': str(e)})
        pass
@app.route('/get_one/<int:id>',methods = ['GET'] )
def get_one(id):
    try:
        movie = Movies.query.filter_by(id = id).first()
        data = {'99popularity': movie.popularity,
                           'director': movie.director ,'genre':movie.genre,'imdb_score':movie.imdb_score, 'name':movie.name}
        return make_response(jsonify(data),200)
    except Exception as e:
        data = {'Message':'Id Does not exist'}
        return make_response(jsonify(data),400)
        pass

@app.route('/delete',methods = ['POST'])
@login_required
def delete():
    received_json_data=request.json
    movie_name = received_json_data['name']
    print(movie_name)
    try :
        movies = Movies.query.filter_by(name = movie_name)
        print('-----------------',movies)
        if movies.first()  is not None:
            for movie in movies:
                db.session.delete(movie)
                db.session.commit()
            data = {'Message':'Success'}
            return make_response(jsonify(data),200)
        else:
            data = {'Message':'Movie not Present'}
            return make_response(jsonify(data),400)
    except:
        data = {'Message':'Movie Does not exist'}
        return make_response(jsonify(data),400)

@app.route('/create',methods=['POST'])
@login_required
def create():
    try:
        received_json_data=request.json
        popularity = received_json_data['99popularity']
        director = received_json_data['director']
        genre = received_json_data['genre']
        imdb_score = received_json_data['imdb_score']
        name = received_json_data['name']

        movie = Movies(popularity = popularity,director=director,genre=genre,imdb_score = imdb_score, name = name)
        db.session.add(movie) 
        db.session.commit()
        data = {'Message':'Success'}
        return make_response(jsonify(data),200)
    except Exception as e:
        return json.dumps({'error occured': str(e)})

@app.route('/update/<int:id>',methods = ['POST'])
@login_required
def update(id):
    movie = Movies.query.filter_by(id = id).first()
    if movie:
        try:
            received_json_data=request.json
            popularity = received_json_data['99popularity']
            director = received_json_data['director']
            genre = received_json_data['genre']
            imdb_score = received_json_data['imdb_score']
            name = received_json_data['name']

            if popularity:
                movie.popularity = popularity
            if director:
                movie.director = director
            if genre:
                movie.genre = genre
            if imdb_score:
                movie.imdb_score = imdb_score
            if name:
                movie.name = name
            db.session.commit()
            data = {'Message':'Updated'}
            return make_response(jsonify(data),200)
        except Exception as e:
            return json.dumps({'error occured': str(e)})
    return f"Employee with id = {id} Does nit exist"

@app.route('/login_tmp', methods = ['POST','GET'])
def login_tmp():
    try: 
        
        form = LoginForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                username = form.user_name.data
                password = form.password.data
                user = User.query.filter_by(username=username).first()
                if user.password == password:
                    login_user(user)
                    #return 'Loggedin'
                    #return redirect(url_for('admin.index'))
                    data = {'Message':'Logged In'}
                    return make_response(jsonify(data),200)
        return render_template('login.html', form=form)
    except Exception as e:
        return json.dumps({'error occured': str(e)})

@app.route('/login', methods = ['POST','GET'])
def login():
    try: 
        #form = LoginForm()
        if request.method == 'POST':
                received_json_data=request.json
                username = received_json_data['username']
                password = received_json_data['password']
                user = User.query.filter_by(username=username).first()
                if user.password == password:
                    login_user(user)
                    #return 'Loggedin'
                    #return redirect(url_for('admin.index'))
                    data = {'Message':'Logged In'}
                    return make_response(jsonify(data),200)
        #return render_template('login.html', form=form)
        data = {'Message':'Please Login Via Admin'}
        return make_response(jsonify(data),400)
    except Exception as e:
        return json.dumps({'error occured': str(e)})



@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return 'Logged out'
    return 'Login First to logout'

@app.route('/search',methods = ['POST','GET'])
def search():
    form = Search()
    if form.validate_on_submit():
        movie_name = form.movie_name.data
        try :
            movies = Movies.query.filter_by(name = movie_name)
            if movies.first() is not None:
                for movie in movies:
                    data = jsonify( [{'99popularity': o.popularity,
                            'director': o.director ,'genre':o.genre,'imdb_score':o.imdb_score, 'name':o.name} for o in movies] )
                return make_response(data,200)
            else:
                data = {'Message':'Movie not Present.'}
                return make_response(jsonify(data),400)
        except Exception as e:
            #return json.dumps({'error occured': str(e)})
            data = {'Message':'Movie not Present'}
            return make_response(jsonify(data),400)
    return render_template('search.html', form=form)
