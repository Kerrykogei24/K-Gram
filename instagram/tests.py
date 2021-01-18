from django.test import TestCase
from .models import Profile,Image,Comments
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):

        self.name = User(username = 'kerry', email ='kerrykomar@gmail.com')
        self.name = Profile(user = self.name, user_id = 1, bio = 'joker', profile_pic = 'img.jpg')

    def test_instance(self):
        
        self.assertTrue(isinstance(self.mercy,Profile))