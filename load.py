import pickle

p_obj = open("pawan_movies", "r")
p_movies = pickle.load(p_obj)

print(p_movies)
