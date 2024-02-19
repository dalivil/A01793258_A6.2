import json

class PersistenceHandler:
    @staticmethod
    def save_hotel_to_file(hotel):
        with open('hotels.json', 'w') as file:
            json.dump(hotel.__dict__, file)

    @staticmethod
    def load_hotel_from_file():
        with open('hotels.json', 'r') as file:
            data = json.load(file)
            hotel = Hotel(data['name'], data['location'])
            hotel.rooms = [Room(room['number'], room['type'], room['price']) for room in data['rooms']]
            return hotel

