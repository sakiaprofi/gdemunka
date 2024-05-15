from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price

class SingleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, price=50)

class DoubleRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, price=80)

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

class Reservation:
    def __init__(self, room, date):
        self.room = room
        self.date = date

class ReservationSystem:
    def __init__(self, hotel):
        self.hotel = hotel
        self.reservations = []

    def book_room(self, room_number, date):
        for room in self.hotel.rooms:
            if room.room_number == room_number:
                reservation_date = datetime.strptime(date, "%Y-%m-%d")
                today = datetime.now()
                if reservation_date >= today:
                    reservation = Reservation(room, reservation_date)
                    self.reservations.append(reservation)
                    return room.price
                else:
                    return "Helytelen dátum, kérlek válassz egy jövőbeli dátumot."
        return "Szoba nem található."

    def cancel_reservation(self, room_number, date):
        reservation_date = datetime.strptime(date, "%Y-%m-%d")
        for reservation in self.reservations:
            if reservation.room.room_number == room_number and reservation.date == reservation_date:
                self.reservations.remove(reservation)
                return "Foglalás sikeresen törölve."
        return "Foglalás nem található."

    def list_reservations(self):
        for reservation in self.reservations:
            print(f"Room {reservation.room.room_number} reserved on {reservation.date.strftime('%Y-%m-%d')}")

def populate_system(hotel):
    room1 = SingleRoom("101")
    room2 = DoubleRoom("102")
    room3 = SingleRoom("103")
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    reservation_system = ReservationSystem(hotel)
    reservation_system.book_room("101", "2024-05-17")
    reservation_system.book_room("102", "2024-05-18")
    reservation_system.book_room("103", "2024-05-19")

    return reservation_system

def user_interface(reservation_system):
    while True:
        print("\nÜdvözöl a ", reservation_system.hotel.name)
        print("1. Foglalj egy szobát")
        print("2. Foglalás tőrlése")
        print("3. Listázd a foglalásokat")
        print("4. kilépés")
        choice = input("Válassz szolgáltatást: ")

        if choice == "1":
            room_number = input("Add meg  szoba számát: ")
            date = input("Foglalás időpontja (YYYY-MM-DD): ")
            price = reservation_system.book_room(room_number, date)
            print(f"Sikeres foglalás, szoba ára: {price}")

        elif choice == "2":
            room_number = input("Add meg  szoba számát: ")
            date = input("Foglalás időpontja (YYYY-MM-DD): ")
            message = reservation_system.cancel_reservation(room_number, date)
            print(message)

        elif choice == "3":
            reservation_system.list_reservations()

        elif choice == "4":
            print("Kilépés a programból...")
            break

        else:
            print("Helytelen válasz, kérlek válassz mást.")

if __name__ == "__main__":
    hotel = Hotel("Minta hotel")
    populate_system(hotel)
    user_interface(populate_system(hotel))

    

