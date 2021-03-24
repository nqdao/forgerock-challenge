from server import app
import unittest
import io
import json


class LongestWordsTestCase(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_longest_words(self):
        data = dict(
            file=(io.BytesIO(b'file content youtube'), "file.txt")
        )
        result = self.app.post('/longest-words',
                                content_type='multipart/form-data',
                                data=data)
        self.assertTrue(b'content' in result.data and b'youtube' in result.data)

    def test_empty_file(self):
        data = dict(
            file=(io.BytesIO(b''), "file.txt")
        )
        result = self.app.post('/longest-words',
                                content_type='multipart/form-data',
                                data=data)
        json_resp = json.loads(result.data.decode('utf8'))
        # Assert that longest_words is empty
        self.assertFalse(json_resp['longest_words'])


if __name__ == '__main__':
    unittest.main()
