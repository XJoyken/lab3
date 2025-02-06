# Dictionary of movies

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
#-----------------------------------
movie = {
    "name": "We Two",
    "imdb": 7.2,
    "category": "Romance"
    }
def above_5_5(movie):
    return movie['imdb'] > 5.5
print(above_5_5(movie))
print("------------------------------------")
def sublist(movies):
    lst = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            lst.append(movie)
    return lst
for i in sublist(movies):
    print(i)
print("------------------------------------")
category = input()
def in_categ(category):
    lst = []
    for movie in movies:
        if movie['category'] == category:
            lst.append(movie)
    return lst
for i in in_categ(category):
    print(i)
print("------------------------------------")
def avg_imdb(movies):
    sum = 0;
    count = 0;
    for movie in movies:
        sum += movie['imdb']
        count += 1
    return sum / count
print("AVG:", avg_imdb(movies))
print("------------------------------------")
category = input()
def abg_by_categ(category):
    sum = 0
    count = 0
    for movie in movies:
        if movie['category'] == category:
            sum += movie['imdb']
            count += 1
    return sum / count
print(f"AVG by category {category}:", abg_by_categ(category))