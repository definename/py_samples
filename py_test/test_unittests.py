import inc_dec
import unittest


class Test_TestIncrementDecrement(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 3)


if __name__ == "__main__":
    unittest.main()
