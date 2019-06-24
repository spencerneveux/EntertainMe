import requests

KEY = 'API KEY'

class Movie:

	def __init__(self):
		self.movie = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key='+ KEY + '&language=en-US&page=1').json()

	def get_data(self):
		return self.movie['results'] 

	def get_result_count(self):
		return len(self.movie['results'])

	def get_movie_details(self, id):
		details = requests.get('https://api.themoviedb.org/3/movie/' + id + '?api_key='+ KEY + '&language=en-US').json()
		return details

	def get_tv_details(self, id):
		details = requests.get('https://api.themoviedb.org/3/tv/' + id + '?api_key='+ KEY + '&language=en-US').json()
		return details

	def get_movie_video(self, id):
		video = requests.get('https://api.themoviedb.org/3/movie/' + id + '/videos?api_key='+ KEY + '&language=en-US').json()
		return video

	def get_tv_video(self, id):
		video = requests.get('https://api.themoviedb.org/3/tv/' + id + '/videos?api_key='+ KEY + '&language=en-US').json()
		return video

	def get_trending(self):
		trending = requests.get('https://api.themoviedb.org/3/trending/all/day?api_key='+ KEY + '').json()
		return trending


	def get_tv(self):
		tv = requests.get('https://api.themoviedb.org/3/tv/popular?api_key='+ KEY + '&language=en-US&page=1').json()
		return tv
