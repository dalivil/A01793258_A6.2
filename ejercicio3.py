import unittest

class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []

    def create_room(self, room_number, room_type, price):
        room = {"room_number": room_number, "room_type": room_type, "price": price}
        self.rooms.append(room)

    def delete_room(self, room_number):
        self.rooms = [room for room in self.rooms if room['room_number'] != room_number]

    def display_info(self):
        return f"Hotel Name: {self.name}\nLocation: {self.location}"

    def modify_info(self, name=None, location=None):
        if name:
            self.name = name
        if location:
            self.location = location

    def reserve_room(self, room_number):
        room = next((room for room in self.rooms if room['room_number'] == room_number), None)
        if room:
            return f"Room {room_number} reserved successfully."
        else:
            return f"Room {room_number} not found."

    def cancel_reservation(self, room_number):
        room = next((room for room in self.rooms if room['room_number'] == room_number), None)
        if room:
            self.rooms.remove(room)
            return f"Reservation for room {room_number} cancelled."
        else:
            return f"Room {room_number} not found."


class Customer:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email

    def display_info(self):
        return f"Customer Name: {self.name}\nEmail: {self.email}"

    def modify_info(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email

class Reservation:
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def create_reservation(self):
        return f"Reservation created for {self.customer.name} at {self.hotel.name}."

    def cancel_reservation(self):
        return f"Reservation cancelled for {self.customer.name} at {self.hotel.name}."


class Reservation:
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def create_reservation(self):
        return f"Reservation created for {self.customer.name} at {self.hotel.name}"        


# Unit tests
class TestHotel(unittest.TestCase):
    def test_create_room(self):
        hotel = Hotel("Hotel ABC", "City A")
        hotel.create_room(101, "Single", 100)
        self.assertEqual(len(hotel.rooms), 1)


class TestCustomer(unittest.TestCase):
    def test_modify_info(self):
        customer = Customer("Alice", "alice@example.com")
        customer.modify_info(email="new_email@example.com")
        self.assertEqual(customer.email, "new_email@example.com")

class TestReservation(unittest.TestCase):
    def test_create_reservation(self):
        customer = Customer("Alice", "alice@example.com")
        hotel = Hotel("Hotel ABC", "City A")
        reservation = Reservation(customer, hotel)
        self.assertEqual(reservation.create_reservation(), "Reservation created for Alice at Hotel ABC")

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.hotel = Hotel("Hotel ABC")
        self.reservation = Reservation(self.customer, self.hotel)

    def test_create_reservation(self):
        self.assertEqual(self.reservation.create_reservation(), "Reservation created for Alice at Hotel ABC")

    def test_cancel_reservation(self):
        self.assertEqual(self.reservation.cancel_reservation(), "Reservation cancelled for Alice at Hotel ABC")

    def test_modify_reservation(self):
        new_hotel = Hotel("Hotel XYZ")
        self.assertEqual(self.reservation.modify_reservation(new_hotel), "Reservation modified for Alice at Hotel XYZ")

    def test_display_reservation(self):
        self.assertEqual(self.reservation.display_reservation(), "Reservation details for Alice at Hotel ABC")

    def test_get_customer_name(self):
        self.assertEqual(self.reservation.get_customer_name(), "Alice")



class Hotel:
    def __init__(self, name):
        self.name = name

class Reservation:
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def create_reservation(self):
        return f"Reservation created for {self.customer.name} at {self.hotel.name}"

    def cancel_reservation(self):
        return f"Reservation cancelled for {self.customer.name} at {self.hotel.name}"

    def modify_reservation(self, new_hotel):
        self.hotel = new_hotel
        return f"Reservation modified for {self.customer.name} at {self.hotel.name}"

    def display_reservation(self):
        return f"Reservation details for {self.customer.name} at {self.hotel.name}"

    def get_customer_name(self):
        return self.customer.name

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice", "alice@example.com")
        self.hotel = Hotel("Hotel ABC")
        self.reservation = Reservation(self.customer, self.hotel)

    def test_create_reservation(self):
        self.assertEqual(self.reservation.create_reservation(), "Reservation created for Alice at Hotel ABC")

    def test_cancel_reservation(self):
        self.assertEqual(self.reservation.cancel_reservation(), "Reservation cancelled for Alice at Hotel ABC")

    def test_modify_reservation(self):
        new_hotel = Hotel("Hotel XYZ")
        self.assertEqual(self.reservation.modify_reservation(new_hotel), "Reservation modified for Alice at Hotel XYZ")

    def test_display_reservation(self):
        self.assertEqual(self.reservation.display_reservation(), "Reservation details for Alice at Hotel ABC")

    def test_get_customer_name(self):
        self.assertEqual(self.reservation.get_customer_name(), "Alice")

class Customer:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email

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

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice", "alice@example.com")

    def test_modify_info(self):
        self.assertEqual(self.customer.modify_info(email="new_email@example.com"), "Email updated for Alice")

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

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice", "alice@example.com")

    def test_modify_info(self):
        self.assertEqual(self.customer.modify_info(email="new_email@example.com"), "Email updated for Alice")

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



if __name__ == "__main__":
    unittest.main()