from data_manager import DataManager
from flight_search import *
from notification_manager import NotificationManager

ORIGIN = 'LON'

# This file will need to use the
# DataManager,
# FlightSearch,
# FlightData,
# NotificationManager classes to achieve the program requirements.

sheet_data = DataManager()

for num in range(0, len(sheet_data.bargain_data['prices'])):
    if sheet_data.bargain_data['prices'][num]['iataCode'] == '':
        sheet_data.update_iata_codes()

# pprint(sheet_data.bargain_data)
# paris_bargain = sheet_data.bargain_data['prices'][0]['lowestPrice']
# pprint(paris_bargain)
#
# prices = {sheet_data.bargain_data['prices'][num]['iataCode']: sheet_data.bargain_data['prices'][num]['lowestPrice']
#           for num in range(0, len(sheet_data.bargain_data['prices']))}
# pprint(prices)

new_search = FlightSearch()
# new_search.search_for_flight(LON, destination=)

# print(sheet_data.bargain_data)
# current_price: int

for x in range(0, len(sheet_data.bargain_data['prices'])):
    destination = sheet_data.bargain_data['prices'][x]['iataCode']
    city = sheet_data.bargain_data['prices'][x]['city']

    # handle exception for the line below
    try:
        new_search.search_for_flight(ORIGIN, destination=destination)
        current_price = new_search.deal['price']
    except IndexError:
        print(f"Flight Details {new_search.deal}")
    else:

        # the code below sends an SMS to my 020 number. It is intentionally disabled so that multiple SMS are not sent.
        # it can also send emails to the emails of the addresses saved in the Google sheet.

        bargain_price = sheet_data.bargain_data['prices'][x]['lowestPrice']
        if current_price <= bargain_price:
            message = (f'LOW PRICE ALERT!!!\nOnly £{current_price} to fly from {new_search.deal["dept_city"]}-'
                       f'{new_search.deal["dept_airport"]} to {new_search.deal["arrival_city"]}-'
                       f'{new_search.deal["arrival_airport"]} from {new_search.deal["outbound_date"]} '
                       f'to {new_search.deal["inbound_date"]}')

            notify = NotificationManager(message=message)
            notify.send_email()
