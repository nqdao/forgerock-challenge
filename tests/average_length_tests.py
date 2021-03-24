from server import app
import unittest
import io
import json


class AverageLengthTestCase(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_average_length(self):
        data = dict(
            file=(io.BytesIO(b'I am god'), "file.txt")
        )
        result = self.app.post('/average-length',
                                content_type='multipart/form-data',
                                data=data)
        json_resp = json.loads(result.data.decode('utf8'))
        self.assertEqual(json_resp['average_length'], 2)

    def test_empty_file(self):
        data = dict(
            file=(io.BytesIO(b''), "file.txt")
        )
        result = self.app.post('/average-length',
                                content_type='multipart/form-data',
                                data=data)
        json_resp = json.loads(result.data.decode('utf8'))
        self.assertEqual(json_resp['average_length'], 0)

if __name__ == '__main__':
    unittest.main()
