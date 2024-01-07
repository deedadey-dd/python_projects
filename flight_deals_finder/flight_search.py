import requests
from datetime import datetime, timedelta

MAIN_URL = 'https://api.tequila.kiwi.com/'
KIWI_URL = MAIN_URL + 'v2/search'
KIWI_API = 'tSRAkJ-YreTnApbzQeIk3u7AYAyy3mmU'
MONTHS_TO_SEARCH = 6

LOCATION_API = MAIN_URL + 'locations/query'

header = {
    'apikey': KIWI_API
}


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.deal = {}

    def search_for_flight(self, origin, destination):
        current_date = datetime.today()
        after_months = current_date + timedelta(days=30 * MONTHS_TO_SEARCH)

        from_date = current_date.strftime('%d/%m/%Y')
        to_date = after_months.strftime('%d/%m/%Y')

        parameters = {
            'fly_from': origin,
            'fly_to': destination,
            'date_from': from_date,
            'date_to': to_date,
            'curr': 'GBP',
            'sort': 'price',
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,

        }

        response = requests.get(url=KIWI_URL, params=parameters, headers=header)
        try:
            all_data = response.json()['data'][0]
            # total_results = all_data['_results']
        except IndexError:
            print("...No flights found...")

        else:
            to_city = all_data['cityTo']
            price = all_data['price']
            outbound = all_data['utc_departure'][:10]
            inbound = all_data['utc_arrival'][:10]

            self.deal = {
                'to_city': to_city,
                'price': price,
                'dept_city': all_data['cityFrom'],
                'dept_airport': all_data['flyFrom'],
                'arrival_city': all_data['cityTo'],
                'arrival_airport': all_data['flyTo'],
                'outbound_date': f"{outbound}",
                'inbound_date': f"{inbound}",

            }

            print(f'{to_city}: £{price}')

    def get_iata_code(self, city_name):
        location_data = {
            'term': city_name,
            'location_types': 'city',
        }

        location_response = requests.get(url=LOCATION_API, params=location_data, headers=header)
        response_data = location_response.json()
        iata_code = response_data['locations'][0]['code']

        return iata_code


n_search = FlightSearch()
n_search.search_for_flight('LON', 'NYC')
