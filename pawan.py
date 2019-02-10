import pickle



def get_pawan_chemistry_meter():

    movie1 = {"name" : "gabbar singh", "actress_name":"shruthi haasan", "chemistry_meter":8}
    movie2 = {"name" : "kushi", "actress_name":"boomikha", "chemistry_meter":10}
    print (movie1)
    movie_list = [movie1, movie2]
    #print(movie_list)
    return movie_list

k_movie_list = get_pawan_chemistry_meter()

filename_dft="pawan_movies"
f_obj = open(filename_dft,"wb")

pickle.dump(k_movie_list, f_obj)
f_obj.close()