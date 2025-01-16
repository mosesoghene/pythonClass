class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True
        self.needs_maintenance = False

    def to_dict(self):
        return {
            'room_number': self.room_number,
            'room_type': self.room_type,
            'price_per_night': self.price_per_night,
            'is_available': self.is_available,
            'needs_maintenance': self.needs_maintenance
        }

    @classmethod
    def from_dict(cls, data):
        room = cls(data['room_number'], data['room_type'], data['price_per_night'])
        room.is_available = data['is_available']
        room.needs_maintenance = data['needs_maintenance']
        return room

