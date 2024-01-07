import requests

url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YzYxYWE1YTNhYTlkNWJkMzM1ZjhkMDk4MWJmYzdmNCIsInN1YiI6IjY1NzVmM2M4YTFkMzMyMDEzOGVhNGVmOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lEAUe4rZl5HT9GhPm9y69oKwYJpouyz1LOvAXXn4s70"
}

params = {
    'query': 'The Mechanic'
}

response = requests.get(url, headers=headers, params=params)
data = response.text
# print(response.json())
# print(response['results'][0]['original_title'])
# print(response['results'][0]['release_date'][:4])
print(data)
