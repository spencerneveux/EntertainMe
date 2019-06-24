from flask import Flask, render_template, url_for
from movie import Movie 

app = Flask(__name__)
m = Movie()

@app.route('/')
def home():
	# Get Recent movies
	data = m.get_data()
	length = m.get_result_count()
	# Get popular tv shows 
	popular_tv = m.get_tv()
	# Get trending items
	trending = m.get_trending()
	return render_template('home.html', data=data, length=length, popular_tv=popular_tv, trending=trending)

@app.route('/details/')
@app.route('/details/<type>/<id>')
def details(id, type):
	if type == 'movie':
		details = m.get_movie_details(id)
		video = m.get_movie_video(id)
	elif type == 'tv':
		details = m.get_tv_details(id)
		video = m.get_tv_video(id)
	return render_template('details.html', details=details, id=id, video=video)

@app.route('/tv')
def tv():
	tv = m.get_tv()
	return render_template('tv.html', tv=tv)