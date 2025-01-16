class HugeInteger:
    def __init__(self, value):
        self._LIMIT = 40
        self.numbers = self.parse(value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return HugeInteger(self.value + other.value)

    def parse(self, value: str):
        numbers = []
        if len(str(value)) > self._LIMIT:
            raise ValueError("value too long")

        for char in str(value):
            if char.isdigit():
                numbers.append(int(char))
            else:
                raise ValueError(f"value {char} is not a number")

        return numbers

    def __str__(self):
        return int("".join(self.numbers))

    def get_value(self):
        return int("".join(self.numbers))
