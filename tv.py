import requests

class TV:
	def __init__(self):
		self.tv = requests.get('https://api.themoviedb.org/3/tv/popular?api_key=d6982a301b9628f78bb3be565a945c79&language=en-US&page=1').json()

	def get_data(self):
		return self.tv