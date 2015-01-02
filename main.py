from pulsar import provider

def search(query):
	resp = provider.GET("http://kickass.to/usearch", params={
		"q": query,
	})
	return provider.extract_magnets(resp.data)

def search_episode(episode):
	return search("%(title)s S%(season)02dE%(episode)02d  category:tv 720p OR 1080p" % episode)

def search_movie(movie):
	return search("%(title)s %(year)d" % movie)


provider.register(search, search_movie, search_episode)


