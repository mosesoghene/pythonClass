import unittest
from src.mytv import Tv


class TestTv(unittest.TestCase):

    def test_that_tv_class_exists(self):
        tv = Tv()

    def test_that_tv_is_switched_off(self):
        tv = Tv()
        self.assertFalse(tv.status())

    def test_that_tv_is_on_when_switched_on(self):
        tv = Tv()
        tv.turn_on()
        self.assertTrue(tv.status())

    def test_that_tv_is_off_when_turned_off_after_being_on(self):
        tv = Tv()
        tv.turn_on()
        tv.turn_off()
        self.assertFalse(tv.status())

    def test_that_when_turn_on_volume_is_zero_when_first_turned_on(self):
        tv = Tv()
        tv.turn_on()
        self.assertEqual(0, tv.get_volume())

    def test_that_when_turn_off_you_cant_get_volume(self):
        tv = Tv()
        self.assertEqual(None, tv.get_volume())
        tv.turn_on()
        self.assertEqual(0, tv.get_volume())

    def test_to_increase_volume(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        self.assertEqual(1, tv.get_volume())
        tv.increase_volume()
        tv.increase_volume()
        self.assertEqual(3, tv.get_volume())

    def test_that_increase_volume_doesnt_exceed_ten(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        self.assertEqual(10, tv.get_volume())

    def test_to_increase_tv_volume_when_its_off(self):
        tv = Tv()
        tv.increase_volume()
        tv.turn_on()
        self.assertEqual(0, tv.get_volume())

    def test_to_decrease_volume(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.decrease_volume()
        self.assertEqual(9, tv.get_volume())

    def test_to_decrease_volume_while_being_off(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.turn_off()
        tv.decrease_volume()
        tv.turn_on()
        self.assertEqual(10, tv.get_volume())

    def test_to_decrease_volume_lower_than_zero(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.decrease_volume()
        tv.decrease_volume()
        tv.decrease_volume()
        self.assertEqual(0, tv.get_volume())

    def test_to_mute_tv(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.mute()
        self.assertEqual(0, tv.get_volume())

    def test_to_increase_volume_then_mute_tv_then_unmute_tv_and_have_the_previous_volume_before_unmute(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.mute()
        self.assertEqual(0, tv.get_volume())
        tv.un_mute()
        self.assertEqual(2, tv.get_volume())

    def test_that_tv_will_not_be_muted_and_unmuted_while_it_is_off(self):
        tv = Tv()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.turn_off()
        tv.mute()
        tv.turn_on()
        self.assertEqual(2, tv.get_volume())
        tv.mute()
        tv.turn_off()
        tv.un_mute()
        tv.turn_on()
        self.assertEqual(0, tv.get_volume())

    def test_that_channel_can_be_changed_upward(self):
        tv = Tv()
        tv.turn_on() 
        tv.channel_up()
        tv.channel_up()
        self.assertEqual(3, tv.get_channel())

    def test_that_channel_wont_change_when_its_off(self):
        tv = Tv()
        tv.channel_up()
        tv.channel_up()
        tv.turn_on()
        self.assertEqual(1, tv.get_channel())

    def test_that_channel_can_be_changed_downward(self):
        tv = Tv()
        tv.turn_on()
        tv.channel_up()
        tv.channel_up()
        self.assertEqual(3, tv.get_channel())

        tv.channel_down()
        tv.channel_down()
        self.assertEqual(1, tv.get_channel())

    def test_that_you_can_move_to_a_channel(self):
        tv = Tv()
        tv.turn_on()
        tv.search_channel(46)
        self.assertEqual(46, tv.get_channel())

    def test_that_you_cant_move_to_invalid_channels(self):
        tv = Tv()
        tv.turn_on()
        tv.search_channel(56)
        self.assertEqual(1, tv.get_channel())



if __name__ == '__main__':
    unittest.main()