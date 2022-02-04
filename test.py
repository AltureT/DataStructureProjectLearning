import unittest
import global_val


class MyTestCase(unittest.TestCase):
    def test_globalval(self):
        global_val._init()
        global_val.get_user_array()

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
