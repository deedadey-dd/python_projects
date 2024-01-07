import requests
from bs4 import BeautifulSoup
response = requests.get(url='https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')


movies_data = [movie.getText() for movie in soup.find_all(name='h3', class_='listicleItem_listicle-item__title__hW_Kn')]

movies = movies_data[::-1]
print(movies)
with open("movies.txt", mode='w') as file:
    for movie in movies:
        file.write(f'{movie}\n')

# with open("movies.txt", mode='w') as file:
#     for num in range((len(movies_data)-1), -1, -1):
#         file.write(f'{movies_data[num]}\n')



