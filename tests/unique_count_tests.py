from server import app
import unittest
import io
import json


class UniqueCountTestCase(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_unique_count(self):
        data = dict(
            file=(io.BytesIO(b'hello hello world'), "file.txt")
        )
        result = self.app.post('/unique-count',
                                content_type='multipart/form-data',
                                data=data)
        json_resp = json.loads(result.data.decode('utf8'))
        self.assertEqual(json_resp['unique_count'], 2)

    def test_empty_file(self):
        data = dict(
            file=(io.BytesIO(b''), "file.txt")
        )
        result = self.app.post('/unique-count',
                                content_type='multipart/form-data',
                                data=data)
        json_resp = json.loads(result.data.decode('utf8'))
        self.assertEqual(json_resp['unique_count'], 0)

if __name__ == '__main__':
    unittest.main()
