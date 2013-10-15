import unittest
import pyherd

class Test(unittest.TestCase):
    """Unit tests for googlemaps."""

    def test_local_search(self):
        """Test pyherd search()."""
        herd = pyherd.herd()
        run = herd.run("/usr/portage/", "foo/foo", "/metadata.xml")
        result = run['responseData']['results'][0]
        self.assertEqual(result['titleNoFormatting'], 'grobian@gentoo.orgnet-mail@gentoo.org')

if __name__ == "__main__":
    unittest.main()
