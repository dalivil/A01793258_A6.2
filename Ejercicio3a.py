
class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def delete_room(self, room_number):
        self.rooms = [room for room in self.rooms if room.number != room_number]

    def display_info(self):
        print(f"Hotel Name: {self.name}")
        print(f"Location: {self.location}")
        print("Rooms:")
        for room in self.rooms:
            print(f"Room Number: {room.number}, Type: {room.type}, Price: {room.price}")

    # Implementa los demás métodos según los requisitos

class Room:
    def __init__(self, number, type, price):
        self.number = number
        self.type = type
        self.price = price

class Reservation:
    def __init__(self, customer, hotel, room):
        self.customer = customer
        self.hotel = hotel
        self.room = room

    def cancel_reservation(self):
        # Implementación de la cancelación de reserva
        pass

    # Implementa los demás métodos según los requisitos

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

  