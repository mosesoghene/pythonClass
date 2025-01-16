class Guest:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.stay_history = []  # List to track all stays

    def add_stay(self, booking):
        self.stay_history.append({
            'booking_reference': booking.booking_reference,
            'room_type': booking.room.room_type,
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date,
            'total_payment': booking.total_payment
        })

    def to_dict(self):
        return {
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'stay_history': self.stay_history
        }

    @classmethod
    def from_dict(cls, data):
        guest = cls(data['name'], data['phone_number'], data['email'])
        guest.stay_history = data.get('stay_history', [])
        return guest

