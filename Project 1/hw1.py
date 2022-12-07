import math
from collections import defaultdict
from collections import Counter

# You may not add any other imports

# For each function, replace "pass" with your code

# Zain Chalisa (zc285)

# --- TASK 1: READING DATA ---

# 1.1
# return dictionary
def read_ratings_data(f):
    movieDict = {}
    movieFile = open(f)
    for line in movieFile:
        key, value, idNumber = line.split('|')
        if key not in movieDict.keys():
            movieDict[key] = []
            movieDict[key].append(value)
        else:
            movieDict[key].append(value)

    return movieDict

# 1.2
# return dictionary
def read_movie_genre(f):
    movieDict = {}
    movieFile = open(f)
    for line in movieFile:
        (genre, value, key) = line.split('|')
        if key not in movieDict.keys():
            movieDict[key.strip()] = []
            movieDict[key.strip()] = genre.strip()
        else:
            movieDict[key.strip()] = genre.strip()

    return movieDict

# --- TASK 2: PROCESSING DATA ---

# 2.1

# return dictionary
def create_genre_dict(d):
    genreDict = {}
    for key, value in d.items():
        if value not in genreDict.keys():
            genreDict[value] = []
            genreDict[value].append(key)
        else:
            genreDict[value].append(key)

    return genreDict
        


# 2.2
# return dictionary
def calculate_average_rating(d):
    
    avgMovieRating = {}

    for key in d.keys():
        sum = 0
        for val in d[key]:
            sum += float(val)
        avg = sum / len(d[key])
        avgMovieRating[key] = avg

    return avgMovieRating
    

# --- TASK 3: RECOMMENDATION ---

# 3.1
# return top 10 list
def get_popular_movies(d, n=10):

    popularMovies = {}

    if (len(d) < n):
        popularMovies = dict(sorted(d.items(), key=lambda rating: rating[1], reverse= True))
    else:
        popularMovies = dict(sorted(d.items(), key=lambda rating: rating[1], reverse= True) [:n])
    
    return popularMovies


# 3.2
# return dictionary
def filter_movies(d, thres_rating=3):
    filteredMovies = {}
    for key, value in d.items():
        if d[key] >= thres_rating:
            filteredMovies[key] = value
    
    return filteredMovies

# 3.3
# return dictionary
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    popularBasedGenre = {}

    for value in genre_to_movies[genre]:
        if value not in popularBasedGenre:
            popularBasedGenre[value] = []
            
    for k1 in popularBasedGenre.keys():
        for k2 in movie_to_average_rating.keys():
            if k1 == k2:
                popularBasedGenre[k1] = movie_to_average_rating[k2]

    if len(popularBasedGenre) < n:
        popularBasedGenre = dict(sorted(popularBasedGenre.items(), key=lambda rating: rating[1], reverse= True))
    else:
        popularBasedGenre = dict(sorted(popularBasedGenre.items(), key=lambda rating: rating[1], reverse= True) [:n])

    return popularBasedGenre
    
# 3.4
# returns dictionary
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):

    sum = 0
            
    for k1 in genre_to_movies[genre]:
        for k2 in movie_to_average_rating.keys():
            if k1 == k2:
                sum += movie_to_average_rating[k2]
    
    avg = sum / len(genre_to_movies[genre])
    

    return avg    

# 3.5
# return a dictionary
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):

    genrePop = {}

    for key in genre_to_movies.keys():
        genrePop[key] = get_genre_rating(key, genre_to_movies, movie_to_average_rating)

    if len(genrePop) < n:
        genrePop = dict(sorted(genrePop.items(), key=lambda rating: rating[1], reverse= True))
    else:
        genrePop = dict(sorted(genrePop.items(), key=lambda rating: rating[1], reverse= True) [:n])

    return genrePop

# --- TASK 4: USER FOCUSED ---

# 4.1
# return dictionary
def read_user_ratings(f):
    userRatings = {}
    movieFile = open(f)
    for line in movieFile:
        key, value, idNumber1 = line.split('|')
        idNumber = idNumber1.strip()
        rating = (key, value)
        if idNumber not in userRatings.keys():
            userRatings[idNumber] = []
            userRatings[idNumber].append(rating)
        else:
            userRatings[idNumber].append(rating)

    return userRatings


# 4.2
# return genre
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    
    usersMovies = user_to_movies[user_id]
    favGenre = {}

    for (key, value) in usersMovies:
        genre = movie_to_genre[key]
        if genre not in favGenre:
            favGenre[genre] = []
            favGenre[genre].append(value)
        else:
            favGenre[genre].append(value)

    maxRating = 0
    genreTop = ""

    for key in favGenre.keys():
        sum = 0
        for val in favGenre[key]:
            sum += float(val)
        avg = sum/len(favGenre[key])
        if maxRating < avg:
            maxRating = avg
            genreTop = key
        favGenre[key] = avg

    favGenre = dict(sorted(favGenre.items(), key=lambda rating: rating[1], reverse= True))

    return genreTop

# 4.3
#return dictionary
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):

    n = 3
    
    topGenre = get_user_genre(user_id, user_to_movies, movie_to_genre)

    reccomendations = {}

    for movie1, genre in movie_to_genre.items():
        if topGenre == genre and len([item for item in user_to_movies[user_id] if movie1 in item]) == 0: # the list will be populated if the movie has already been rated
            reccomendations[movie1] = movie_to_average_rating[movie1]

    reccomendations = dict(sorted(reccomendations.items(), key=lambda rating: rating[1], reverse= True) [:n])

    return reccomendations


# --- main function for your testing ---
def main():
# function 1 test
    print("read_ratings_data")
    print(read_ratings_data("movieRatingSample.txt"))
    print()
# function 2 test
    print("read_movie_genre")
    print(read_movie_genre("genreMovieSample.txt"))
    movieToGenre = read_movie_genre("genreMovieSample.txt")
    print()
# function 3 test
    print("create_genre_dict")
    genreMovie = create_genre_dict(read_movie_genre("genreMovieSample.txt"))
    print(create_genre_dict(read_movie_genre("genreMovieSample.txt")))
    print()
# function 4 test
    print("calculate_average_rating")
    movieAvg = calculate_average_rating(read_ratings_data("movieRatingSample.txt"))
    print(calculate_average_rating(read_ratings_data("movieRatingSample.txt")))
    print()
# function 5 test
    print("get_popular_movies")
    print(get_popular_movies(movieAvg))
    print()

#function 6 test
    print("filter_movies")
    print(filter_movies(calculate_average_rating(read_ratings_data("movieRatingSample.txt"))))
    print()

#function 7 test
    print("get_popular_in_genre")
    print(get_popular_in_genre("Adventure", genreMovie, movieAvg))
    print()

#function 8 test

    print("get_genre_rating")
    print(get_genre_rating("Action", genreMovie, movieAvg))
    print()

#function 9 test
    print("genre_popularity")
    print(genre_popularity(genreMovie, movieAvg))
    print()

#function 10 test
    print("read_user_ratings")
    print(read_user_ratings("movieRatingSample.txt"))
    userToMovie = read_user_ratings("movieRatingSample.txt")
    print()

#function 11 test
    print("get_user_genre")
    print(get_user_genre('6', userToMovie, movieToGenre))
    print()

#function 12 test
    print("reccomend_movies")
    print(recommend_movies("6", userToMovie, movieToGenre, movieAvg))
    print()

    print("end of assignment")


main()
