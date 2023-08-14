from django.test import TestCase

class SanityCheck(TestCase):
    _TEST_STRING :str = b"Let there be light"
    def testCorrectInitialText(self) -> None:
        response = self.client.get('http://localhost:8080/')
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.content, SanityCheck._TEST_STRING)