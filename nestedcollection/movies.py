movies=[

    {
        "title": "Bad Asses on the Bayou",
        "year": 2015,
        "cast": [
            "Danny Trejo",
            "Danny Glover",
            "John Amos",
            "Loni Love"
        ],
        "genres": [
            "Action"
        ]
    },
    {
        "title": "Chappie",
        "year": 2015,
        "cast": [
            "Sharlto Copley",
            "Dev Patel",
            "Watkin Tudor Jones",
            "Yolandi Visser"
        ],
        "genres": [
            "Science Fiction"
        ]
    },
    {
        "title": "Road Hard",
        "year": 2015,
        "cast": [
            "Adam Carolla",
            "David Koechner",
            "Diane Farr",
            "Jay Mohr",
            "David Alan Grier"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "The Second Best Exotic Marigold Hotel",
        "year": 2015,
        "cast": [
            "Judi Dench",
            "Maggie Smith",
            "Bill Nighy"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Unfinished Business",
        "year": 2015,
        "cast": [
            "Vince Vaughn",
            "Dave Franco",
            "Sienna Miller",
            "Nick Frost"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "Cinderella",
        "year": 2015,
        "cast": [
            "Lily James",
            "Richard Madden",
            "Cate Blanchett",
            "Helena Bonham Carter",
            "Holliday Grainger"
        ],
        "genres": [
            "Romance"
        ]
    },
    {
        "title": "The Cobbler",
        "year": 2015,
        "cast": [
            "Adam Sandler",
            "Dustin Hoffman",
            "Dan Stevens",
            "Steve Buscemi"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Cymbeline",
        "year": 2015,
        "cast": [
            "Ed Harris",
            "Milla Jovovich",
            "Ethan Hawke",
            "John Leguizamo"
        ],
        "genres": [
            "Crime"
        ]
    },
    {
        "title": "Home Sweet Hell",
        "year": 2016,
        "cast": [
            "Patrick Wilson",
            "Katherine Heigl",
            "Jordana Brewster",
            "Jim Belushi"
        ],
        "genres": [
            "Comedy"
        ]
    }
#     {
#         "title": "It Follows",
#         "year": 2015,
#         "cast": [
#             "Maika Monroe",
#             "Keir Gilchrist",
#             "Jake Weary",
#             "Daniel Zovatto"
#         ],
#         "genres": [
#             "Horror"
#         ]
#     }
]


#q1--> print total no.of movies
print(len(movies))

#q2--> print all movies

all_movies=[m.get("title") for m in movies]
# print(all_movies)

#q3--> print all movies where genres=comedy
comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres") and "Drama" in m.get("genres")]
# print(comedy_movies)

# for m in movies:
#     get_genrs=m.get("genres")
#     if get_genrs[0]=="Comedy":
#       print(m.get("title"))

# q4--> print all movies where year=2015
year_2015=[m.get("title") for m in movies if m.get("year")==2015]
# print(len(year_2015))

# q5--> print all comedy and drama movies
# q6--> print all cast in the movie "Road Hard"

get_cast=[c.get("cast") for c in movies if c.get("title")=="Road Hard"]
# print(get_cast)

# q7--> print movie name where cast= "Maggie Smith"

cast_title=[m.get("title") for m in movies if "Maggie Smith" in m.get("cast")]
# print(cast_title)
    
# q8 --> print comedy or drama movie
comedy_drama_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres") or "Drama" in m.get("genres")]
# print(comedy_drama_movies)

# q9 -->

actors=[]

for m in movies:
   for a in m.get("cast"):
      actors.append(a)
print(actors)
wc={a:actors.count(a) for a in set(actors)}
print(wc)

for k,v in wc.items():
   if v>1:
      print(k)