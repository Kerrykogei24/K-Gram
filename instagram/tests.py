from django.test import TestCase
from .models import Profile,Image,Comments
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):

        self.name = User(username = 'kerry', email ='kerrykomar@gmail.com')
        self.name = Profile(user = self.name, user_id = 1, bio = 'joker', profile_pic = 'img.jpg')

    def test_instance(self):

        self.assertTrue(isinstance(self.name,Profile))

    def test_save_profile(self):

        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        '''
        Test to see if a profile can be deleted 
        '''
        self.mercy.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

class ImageTestCase(TestCase):
    def setUp(self):
        self.new_post = Image(ig_pic= 'img.jpg', name = 'image', caption= 'ma pictures tu', user = name)

    def test_save_image(self):
        self.picture.save_image()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.picture.save_image()
        self.picture.delete_image()
        picture_list = Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
        self.picture.save_image()
        all_pictures = Image.get_all_images()
        self.assertTrue(len(all_pictures) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_pic = Image.get_one_image(self.food.id)
        self.assertTrue(one_pic.name == self.picture.name)

class CommentTestCase(TestCase):
    def setUp(self):
        self.comment=Comment(body="So Nice",image_id=self.bmw.id,user = self.name)  

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_comment(self):
        self.comment.save_comment()
        comments = Comments.objects.all()
        self.assertEqual(len(comments),1)


    def test_delete_comment(self):
        self.comment.save_comment()
        self.comment.delete_comment()
        comment_list = Comments.objects.all()
        self.assertTrue(len(comment_list)==0)




