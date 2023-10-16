
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def imdb(movie):
    return movie["imdb"]>5.5
movie = {    "name": "The Dark Knight",
    "imdb": 9.0,
    "category":"Adventure"}
print(imdb(movie))  

#2

def above_5_5(movies):
    idmb=5.5
    return [movie for movie in movies if movie["imdb"] > idmb]
above_5_5_movies = above_5_5(movies)
print("Movies with IMDB score above 5.5:")
for movie in above_5_5_movies:
    print(f"{movie['name']} - IMDB Score: {movie['imdb']}")

    #3


def get_category(movies, category):
    return [movie for movie in movies if movie["category"]==category]
name = input()
romance_movies = get_category(movies, name)
print(f"{name} movies:")
for movie in romance_movies:
    print(f"{movie['name']} - IMDB Score: {movie['imdb']}")

    #4
    def average_imdb(movies):
    if not movies:
        return 0.0
    summ = sum(movie["imdb"] for movie in movies)
    return summ / len(movies)
average_imdb1=average_imdb(movies)
print(f"Movies' average IMDB score: {average_imdb1}")

#5

def by_category(movies, category):
    total = 0.0
    cnt = 0
    for movie in movies:
        if movie["category"] == category:
            total += movie["imdb"]
            cnt += 1
    return total / cnt if cnt > 0 else 0.0
category = input()
average_imdb = by_category(movies, category)
print(f"Average IMDB score of {category} movies is: {average_imdb}")
