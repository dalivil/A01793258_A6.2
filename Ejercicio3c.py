import unittest

class Customer:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email

    def modify_info(self, email=None):
        if email:
            self.email = email
            return f"Email updated for {self.name}"
        else:
            return "No changes made"

    def display_customer_info(self):
        return f"Customer: {self.name}, Email: {self.email}"

    def delete_customer(self):
        return f"Customer {self.name} deleted"

class Hotel:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.rooms = []

    def create_room(self, room_number):
        self.rooms.append(room_number)
        return f"Room {room_number} created for {self.name}"

    def delete_room(self, room_number):
        self.rooms.remove(room_number)
        return f"Room {room_number} deleted for {self.name}"

    def display_hotel_info(self):
        return f"Hotel {self.name} in {self.city} has {len(self.rooms)} rooms"

    def modify_hotel_info(self, city=None):
        if city:
            self.city = city
            return f"City updated for Hotel {self.name}"
        else:
            return "No changes made"

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dalina", "dalina@example.com")

    def test_modify_info(self):
        self.assertEqual(self.customer.modify_info(email="new_email@example.com"), "Email updated for Dalina")

    def test_display_customer_info(self):
        self.assertEqual(self.customer.display_customer_info(), "Customer: Dalina, Email: dalina@example.com")

    def test_delete_customer(self):
        self.assertEqual(self.customer.delete_customer(), "Customer Dalina deleted")

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("Hotel ABC", "City A")

    def test_create_room(self):
        self.assertEqual(self.hotel.create_room(101), "Room 101 created for Hotel ABC")

    def test_delete_room(self):
        self.hotel.create_room(102)
        self.assertEqual(self.hotel.delete_room(102), "Room 102 deleted for Hotel ABC")

    def test_display_hotel_info(self):
        self.hotel.create_room(201)
        self.hotel.create_room(202)
        self.assertEqual(self.hotel.display_hotel_info(), "Hotel Hotel ABC in City A has 2 rooms")

    def test_modify_hotel_info(self):
        self.assertEqual(self.hotel.modify_hotel_info(city="City B"), "City updated for Hotel Hotel ABC")

if __name__ == '__main__':
    unittest.main()