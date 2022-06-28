import requests

SHEET_ENDPOINT = "https://api.sheety.co/c1f1746032c9aec15f2be1a359090c96/flightDeals/prices"
HEADERS = {
    "Authorization": "Bearer YOUR_SHEETY_BEARER_TOKEN"
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data, headers=HEADERS)
            print(response.text)