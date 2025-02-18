class Tv:
    def __init__(self):
        self.__channel = 1
        self.__is_on = False
        self.__previous_volume = 0
        self.__volume = self.__previous_volume
        self.__is_muted = False

    def get_volume(self):
        if self.__is_on:
            return self.__volume


    def status(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False


    def increase_volume(self):
        if 10 > self.__volume >= 0 and self.__is_on and not self.__is_muted:
            self.__volume += 1

    def decrease_volume(self):
        if 10 >= self.__volume > 0 and self.__is_on and not self.__is_muted:
            self.__volume -= 1

    def mute(self):
        if self.__is_on:
            self.__previous_volume = self.__volume
            self.__volume = 0
            self.__is_muted = True

    def un_mute(self):
        if self.__is_on:
            self.__volume = self.__previous_volume
            self.__previous_volume = 0
            self.__is_muted = False

    def channel_up(self):
        if 50 > self.__channel >= 0 and self.__is_on:
            self.__channel += 1

    def get_channel(self):
        if self.__is_on:
            return self.__channel

    def channel_down(self):
        if self.__is_on and 50 >= self.__channel > 1:
            self.__channel -= 1

    def search_channel(self, channel):
        if 50 >= channel >= 1 and self.__is_on:
            self.__channel = channel