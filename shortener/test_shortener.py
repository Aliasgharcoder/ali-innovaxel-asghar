# test_shortener.py
import unittest
from shortener.views import ShortenURLView  # update this path

class TestShortener(unittest.TestCase):
    def test_generate_short_url(self):
        original_url = "https://www.google.com"
        short_url = ShortenURLView(original_url)
        self.assertTrue(len(short_url) <= 8)
        self.assertNotEqual(original_url, short_url)

if __name__ == "__main__":
    unittest.main()
