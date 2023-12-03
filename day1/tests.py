import unittest
from src.main import run


class TestAdvent(unittest.TestCase):
    def test(self):
        self.assertEqual(run("./test.txt"), 81)


if __name__ == "__main__":
    unittest.main()
