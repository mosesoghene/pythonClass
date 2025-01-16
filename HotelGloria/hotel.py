import json
from datetime import datetime, timedelta
import os
from collections import defaultdict
from guest import Guest
from room import Room
from booking import Booking


class HotelSystem:
    def __init__(self):
        self.rooms = []
        self.bookings = []
        self.guests = {}
        self.load_data()

    def initialize_rooms(self):

        room_configs = [

            {"number": "101", "type": "Single", "price": 100},
            {"number": "102", "type": "Single", "price": 100},
            {"number": "103", "type": "Single", "price": 100},

            {"number": "201", "type": "Double", "price": 150},
            {"number": "202", "type": "Double", "price": 150},
            {"number": "203", "type": "Double", "price": 150},

            {"number": "301", "type": "Suite", "price": 250},
            {"number": "302", "type": "Suite", "price": 250},
            {"number": "303", "type": "Suite", "price": 250},
            {"number": "304", "type": "Suite", "price": 250}
        ]


        for config in room_configs:
            room = Room(config["number"], config["type"], config["price"])
            self.rooms.append(room)

        self.save_data()
        print(f"Initialized {len(self.rooms)} rooms successfully.")

    def load_data(self):
        if not os.path.exists('hotel_data.json'):
            self.initialize_rooms()
            return

        with open('hotel_data.json', 'r') as f:
            data = json.load(f)

        self.rooms = [Room.from_dict(room_data) for room_data in data['rooms']]
        self.guests = {email: Guest.from_dict(guest_data)
                       for email, guest_data in data.get('guests', {}).items()}

        self.bookings = []
        for booking_data in data['bookings']:
            guest = Guest.from_dict(booking_data['guest'])
            room = Room.from_dict(booking_data['room'])
            booking = Booking.from_dict(booking_data, guest, room)
            self.bookings.append(booking)


    def view_available_rooms(self, check_in_date=None, check_out_date=None):

        if not check_in_date:
            check_in_date = datetime.now().strftime('%Y-%m-%d')
        if not check_out_date:
            check_out_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')


        check_in = datetime.strptime(check_in_date, '%Y-%m-%d')
        check_out = datetime.strptime(check_out_date, '%Y-%m-%d')


        unavailable_rooms = set()
        for booking in self.bookings:
            booking_check_in = datetime.strptime(booking.check_in_date, '%Y-%m-%d')
            booking_check_out = datetime.strptime(booking.check_out_date, '%Y-%m-%d')


            if (booking_check_in < check_out and booking_check_out > check_in and
                    booking.status != "cancelled"):
                unavailable_rooms.add(booking.room.room_number)


        available_rooms = [room for room in self.rooms
                           if room.room_number not in unavailable_rooms
                           and not room.needs_maintenance]

        if not available_rooms:
            print(f"\nNo rooms available between {check_in_date} and {check_out_date}")
            return


        print(f"\nAvailable Rooms for {check_in_date} to {check_out_date}:")
        print("\nRoom No. | Type   | Price/Night | Status")
        print("-" * 45)

        for room in available_rooms:
            status = "Available"
            if room.needs_maintenance:
                status = "Maintenance"
            print(f"{room.room_number:8} | {room.room_type:6} | ${room.price_per_night:9} | {status}")


    def cancel_booking(self):

        ref = input("\nEnter booking reference: ")


        booking = next((b for b in self.bookings if b.booking_reference == ref), None)

        if not booking:
            print("Booking not found.")
            return


        check_in = datetime.strptime(booking.check_in_date, '%Y-%m-%d')
        if check_in < datetime.now():
            print("Cannot cancel bookings that have already started or completed.")
            return


        booking.status = "cancelled"
        booking.room.is_available = True


        if booking.guest.email in self.guests:
            guest = self.guests[booking.guest.email]
            guest.stay_history = [stay for stay in guest.stay_history
                                  if stay['booking_reference'] != ref]

        self.save_data()
        print(f"Booking {ref} cancelled successfully.")


        days_until_checkin = (check_in - datetime.now()).days
        if days_until_checkin > 7:
            refund = booking.total_payment
            refund_percent = "100%"
        elif days_until_checkin > 3:
            refund = booking.total_payment * 0.5
            refund_percent = "50%"
        else:
            refund = 0
            refund_percent = "0%"

        if refund > 0:
            print(f"Refund amount ({refund_percent}): ${refund:.2f}")
        else:
            print("No refund applicable due to late cancellation.")

    def save_data(self):
        data = {
            'rooms': [room.to_dict() for room in self.rooms],
            'bookings': [booking.to_dict() for booking in self.bookings],
            'guests': {email: guest.to_dict() for email, guest in self.guests.items()}
        }
        with open('hotel_data.json', 'w') as file:
            json.dump(data, file, indent=4)


    def generate_guest_history_report(self, email):
        if email not in self.guests:
            print("Guest not found.")
            return

        guest = self.guests[email]
        print(f"\nGuest History Report for {guest.name}")
        print("-" * 50)
        print(f"Email: {guest.email}")
        print(f"Phone: {guest.phone_number}")
        print(f"Total Stays: {len(guest.stay_history)}")
        print("\nStay Details:")

        for stay in guest.stay_history:
            print(f"\nBooking Reference: {stay['booking_reference']}")
            print(f"Room Type: {stay['room_type']}")
            print(f"Check-in: {stay['check_in_date']}")
            print(f"Check-out: {stay['check_out_date']}")
            print(f"Payment: ${stay['total_payment']}")

    def generate_occupancy_report(self, start_date, end_date):
        print(f"\nOccupancy Report ({start_date} to {end_date})")
        print("-" * 50)


        occupancy = defaultdict(lambda: {'total_days': 0, 'booked_days': 0})
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        date_range = (end - start).days


        for room in self.rooms:
            occupancy[room.room_type]['total_days'] += date_range


        for booking in self.bookings:
            booking_start = datetime.strptime(booking.check_in_date, '%Y-%m-%d')
            booking_end = datetime.strptime(booking.check_out_date, '%Y-%m-%d')

            if booking_start <= end and booking_end >= start:
                overlap_start = max(start, booking_start)
                overlap_end = min(end, booking_end)
                overlap_days = (overlap_end - overlap_start).days
                occupancy[booking.room.room_type]['booked_days'] += overlap_days


        for room_type, data in occupancy.items():
            occupancy_rate = (data['booked_days'] / data['total_days'] * 100
                              if data['total_days'] > 0 else 0)
            print(f"\n{room_type} Rooms:")
            print(f"Occupancy Rate: {occupancy_rate:.1f}%")
            print(f"Booked Days: {data['booked_days']}")
            print(f"Available Days: {data['total_days'] - data['booked_days']}")

    def generate_revenue_report(self, start_date, end_date):
        print(f"\nRevenue Report ({start_date} to {end_date})")
        print("-" * 50)

        revenue_by_type = defaultdict(float)
        total_revenue = 0

        for booking in self.bookings:
            if (booking.check_in_date >= start_date and
                    booking.check_out_date <= end_date):
                revenue_by_type[booking.room.room_type] += booking.total_payment
                total_revenue += booking.total_payment

        for room_type, revenue in revenue_by_type.items():
            print(f"{room_type} Rooms: ${revenue:,.2f}")
        print(f"\nTotal Revenue: ${total_revenue:,.2f}")

    def book_room(self):
        print("\nEnter Guest Details:")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        # Check if returning guest
        guest = self.guests.get(email)
        if guest:
            print(f"\nWelcome back, {guest.name}!")
            guest.phone_number = phone  # Update phone number in case it changed
        else:
            guest = Guest(name, phone, email)
            self.guests[email] = guest

        print("\nAvailable Room Types:")
        print("1. Single - $100/night")
        print("2. Double - $150/night")
        print("3. Suite - $250/night")
        room_type = input("Select room type (1-3): ")
        room_types = ['Single', 'Double', 'Suite']
        selected_type = room_types[int(room_type) - 1]

        available_room = next((room for room in self.rooms
                               if room.room_type == selected_type and room.is_available), None)

        if not available_room:
            print(f"No {selected_type} rooms available.")
            return

        check_in = input("Check-in date (YYYY-MM-DD): ")
        check_out = input("Check-out date (YYYY-MM-DD): ")
        festive = input("Is it a festive period? (y/n): ").lower() == 'y'

        booking = Booking(guest, available_room, check_in, check_out)
        booking.total_payment = booking.calculate_payment(festive)

        available_room.is_available = False
        self.bookings.append(booking)
        guest.add_stay(booking)
        self.save_data()

        print(f"\nBooking confirmed! Reference: {booking.booking_reference}")
        print(f"Total payment: ${booking.total_payment}")

    def main_menu(self):
        while True:
            print("\n=== Hotel Management System ===")
            print("1. View Available Rooms")
            print("2. Book Room")
            print("3. Cancel Booking")
            print("4. Guest History Report")
            print("5. Occupancy Report")
            print("6. Revenue Report")
            print("7. Exit")

            choice = input("\nEnter your choice (1-7): ")

            if choice == '1':
                self.view_available_rooms()
            elif choice == '2':
                self.book_room()
            elif choice == '3':
                self.cancel_booking()
            elif choice == '4':
                email = input("Enter guest email: ")
                self.generate_guest_history_report(email)
            elif choice == '5':
                start = input("Enter start date (YYYY-MM-DD): ")
                end = input("Enter end date (YYYY-MM-DD): ")
                self.generate_occupancy_report(start, end)
            elif choice == '6':
                start = input("Enter start date (YYYY-MM-DD): ")
                end = input("Enter end date (YYYY-MM-DD): ")
                self.generate_revenue_report(start, end)
            elif choice == '7':
                print("Thank you for using the Hotel Management System!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    hotel = HotelSystem()
    hotel.main_menu()