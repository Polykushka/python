from television import *
import unittest

class MyTestCase(unittest.TestCase):
    def test_init(self):
        tv1 = Television()
        self.assertEqual(tv1.get_status(), False)
        self.assertEqual(tv1.get_muted(), False)
        self.assertEqual(tv1.get_channel(), 0)
        self.assertEqual(tv1.get_volume(), 0)

    def test_power(self):
        tv1 = Television()
        tv1.power()
        self.assertEqual(tv1.get_status(), True)
        tv1.power()
        self.assertEqual(tv1.get_status(), False)

    def test_mute(self):
        tv1 = Television()
        tv1.power()
        tv1.mute()
        self.assertEqual(tv1.get_muted(), True)
        tv1.mute()
        self.assertEqual(tv1.get_muted(), False)
        tv1.power()
        tv1.mute()
        self.assertEqual(tv1.get_muted(), False)

    def test_channel_up(self):
        tv1 = Television()
        tv1.power()
        tv1.channel_up()
        self.assertEqual(tv1.get_channel(), 1)
        tv1.channel_up()
        tv1.channel_up()
        tv1.channel_up()
        self.assertEqual(tv1.get_channel(), 0)
        tv1.power()
        tv1.channel_up()
        self.assertEqual(tv1.get_channel(), 0)

    def test_channel_down(self):
        tv1 = Television()
        tv1.power()
        tv1.channel_down()
        self.assertEqual(tv1.get_channel(), 3)
        tv1.channel_down()
        tv1.channel_down()
        tv1.channel_down()
        self.assertEqual(tv1.get_channel(), 0)
        tv1.power()
        tv1.channel_down()
        self.assertEqual(tv1.get_channel(), 0)

    def test_volume_up(self):
        tv1 = Television()
        tv1.power()
        tv1.mute()
        tv1.volume_up()
        self.assertEqual(tv1.get_muted(), False)
        self.assertEqual(tv1.get_volume(), 1)
        tv1.volume_up()
        tv1.volume_up()
        self.assertEqual(tv1.get_volume(), 2)
        tv1.power()
        tv1.volume_up()
        self.assertEqual(tv1.get_volume(),2)

    def test_volume_down(self):
        tv1 = Television()
        tv1.power()
        tv1.mute()
        tv1.volume_down()
        self.assertEqual(tv1.get_muted(), False)
        self.assertEqual(tv1.get_volume(), 0)
        tv1.volume_up()
        tv1.volume_up()
        tv1.volume_down()
        self.assertEqual(tv1.get_volume(), 1)
        tv1.power()
        tv1.volume_down()
        self.assertEqual(tv1.get_volume(), 1)

    def test_str(self):
        tv1 = Television()
        tv1.power()
        tv1.channel_up()
        tv1.volume_up()
        tv1.volume_up()
        self.assertEqual(tv1.__str__(), "Power = True, Channel = 1, Volume = 2")

if __name__ == '__main__':
    unittest.main()
