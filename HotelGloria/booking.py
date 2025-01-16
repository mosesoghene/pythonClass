from datetime import datetime, timedelta
import uuid

class Booking:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.booking_reference = str(uuid.uuid4())[:8]
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_payment = self.calculate_payment()
        self.status = "upcoming"  # upcoming, active, completed, or cancelled

    def calculate_payment(self, festive_period=False):
        days = (datetime.strptime(self.check_out_date, '%Y-%m-%d') -
                datetime.strptime(self.check_in_date, '%Y-%m-%d')).days
        total = self.room.price_per_night * days
        if festive_period:
            total *= 1.5
        return total

    def to_dict(self):
        return {
            'booking_reference': self.booking_reference,
            'guest': self.guest.to_dict(),
            'room': self.room.to_dict(),
            'check_in_date': self.check_in_date,
            'check_out_date': self.check_out_date,
            'total_payment': self.total_payment,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data, guest, room):
        booking = cls(guest, room, data['check_in_date'], data['check_out_date'])
        booking.booking_reference = data['booking_reference']
        booking.total_payment = data['total_payment']
        booking.status = data.get('status', 'upcoming')
        return booking
