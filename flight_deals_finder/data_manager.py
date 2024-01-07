from flight_search import *


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.SHEET_URL = 'https://api.sheety.co/2ca53f58a7655a73fd473d0607e391fa/flightDeals/prices'
        self.response = requests.get(url=self.SHEET_URL)
        self.bargain_data = self.response.json()

    def update_iata_codes(self):
        search = FlightSearch()
        for num in range(0, len(self.bargain_data['prices'])):
            city = self.bargain_data['prices'][num]['city']
            the_id = self.bargain_data['prices'][num]['the_id']
            code = search.get_iata_code(city)
            parameters = {
                'price': {
                    'iataCode': code,
                }
            }
            requests.put(url=f"{self.SHEET_URL}/{the_id}", json=parameters)
            # print(f'{city}, {code}, {posting.status_code}, id: {the_id}')
