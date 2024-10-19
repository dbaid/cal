import unittest
import json

from restdemo import create_app, db


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.uid =  "u_test12348"
        self.user_data = { 'name' : 'test',  'gender' :'F',   'age' : 20,  'weight' : 60,  'height': 160,  'activity_level' : 1.2 }
        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_create(self):
        url = '/user/{}'.format(self.uid)
        res = self.client().post(
            url,
            data=self.user_data
        )
        self.assertEqual(res.status_code, 201)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get('name'), self.user_data['name'])
        self.assertEqual(res_data.get('gender'), self.user_data['gender'])

        res = self.client().post(
            url,
            data=self.user_data
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get('message'), 'user already exist')