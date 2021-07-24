import unittest
import requests
import tokens
import ya

YA_DISK = ya.YandexDisk(tokens.YANDEX_TOKEN, "")

class TestYandexDisk(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_create_dir(self):
        print('test_create_dir')

        path = 'testing'
        self.assertEqual(YA_DISK._send_request(requests.put, 'resources', path).status_code, 201)
        self.assertEqual(YA_DISK._send_request(requests.get, 'resources', path).status_code, 200)
        YA_DISK.delete(path)

    def test_dir_exists(self):
        print('test_create_dir')

        path = 'existing_path'
        YA_DISK.create_dir(path)
        self.assertEqual(YA_DISK._send_request(requests.get, 'resources', path).status_code, 200)
        YA_DISK.delete(path)

        path = 'not_existing_path'
        YA_DISK.delete(path)
        self.assertEqual(YA_DISK._send_request(requests.get, 'resources', path).status_code, 404)

