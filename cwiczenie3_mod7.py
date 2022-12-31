from datetime import datetime

import random



class Films:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        
        self.views = 0
  
    def play(self, view = 1):
        self.views += view

    def __str__(self):
        return f"{self.title} ({self.year})"

    
class Series(Films):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

    def number_of_episodes(list, serie_title, serie_season):
        episodes = 0
        for i in list:
            if type(i) == Series and serie_title == i.title and serie_season == i.season:
                episodes += 1
        return f"{serie_title} - {episodes} episodes"


print("Biblioteka Filmów")
print()

film_library = []
film_library.append(Films(title = "Mania Wielkości", year = "1971", genre = "Komedia"))
film_library.append(Films(title = "Skąpiec", year = "1980", genre = "Komedia"))
film_library.append(Films(title = "Kapuśniaczek", year = "1981", genre = "Komedia"))
film_library.append(Films(title = "Przygody Rabina Jakuba", year = "1973", genre = "Komedia"))
film_library.append(Films(title = "Człowiek Orkiestra", year = "1970", genre = "Komedia"))
film_library.append(Films(title = "Zawieszeni na drzewie", year = "1971", genre = "Komedia"))
film_library.append(Films(title = "Nie Czas Umierać", year = "2021", genre = "Sensacyjny"))
film_library.append(Films(title = "Spectre", year = "2015", genre = "Sensacyjny"))
film_library.append(Films(title = "Skyfall", year = "2012", genre = "Sensacyjny"))
film_library.append(Films(title = "Casino Royale", year = "2006", genre = "Sensacyjny"))
film_library.append(Films(title = "Świat To Za Mało", year = "1999", genre = "Komedia"))
film_library.append(Films(title = "Śmierć Nadejdzie Jutro", year = "2002", genre = "Komedia"))

def add_series(s_title, s_year, s_genre, s_season, number_of_episodes):       
    return [Series(title = s_title, year = s_year, genre = s_genre, season = s_season, episode = i) for i in range(1, number_of_episodes + 1)]
    
film_library = film_library + add_series("The Office", "2010", "Komedia", 1, 15) + add_series("Friends", "1995", "Komedia", 5, 24) + add_series("Downtown Abbey", "2015", "Kostiumowy", 1, 15)


def get_movies(list):
    film_list = [i for i in list if type(i) == Films]
    return sorted(film_list, key = lambda i: i.title)

def get_series(list):
    series_list = [i for i in list if type(i) == Series]
    return sorted(series_list, key = lambda i: i.title)

def search(title, list):
    for i in range(len(list)):          
        if title.capitalize() == list[i].title:                    
            return list[i].title
        elif list[i] == list[-1]:
            return "Title not found"

def generate_views(list):
    index = list.index(random.choice(list))
    views_number = random.randint(1, 100)
    for i in range(1, views_number + 1):
        list[index].play(view = views_number)
        return list

def multiple(func, *args, times = 10):
    for i in range(times):
        func(*args)

multiple(generate_views, film_library)


def top_titles(list, number, content_type = 'All'):
    film_list = get_movies(list)
    series_list = get_series(list)
    if content_type == 'Series':
        series_list = sorted(series_list, key = lambda x: x.views)
        return series_list[-number:]  
    elif content_type == 'Films':
        film_list = sorted(film_list, key = lambda x: x.views)
        return film_list[-number:]
    else:
        list = sorted(list, key = lambda x: x.views)
        return list[-number:]


now = datetime.now()
date = now.strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {date}:")

for i in top_titles(film_library, 3):
    print(f"{i}, {i.views} views")







  
            



