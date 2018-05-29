from django.test import TestCase
from .models import Neighborhood
from django.contrib.auth.models import User


# Create your tests here.
class NeighborhoodTestClass(TestCase):
    #setup method
    def setUp(self):
        #set up user class
        self.new_user = User(username='nish',email='nish@gmail.com')
        self.new_user.save()
        #set up neighborhood class
        self.thome = Neighborhood(name='nyati',location='thome',occupants_count=5,admin=self.new_user)
        self.thome.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.thome,Neighborhood))

    def test_save_neighborhood(self):
        self.thome.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)>0)

    def test_delete_neighborhood(self):
        self.thome.save_neighborhood()
        self.thome.delete_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)<1)

    def test_find_neighborhood(self,pk):
        self.thome.save_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(pk=Neighborhood.pk)
        self.assertEqual(len(neighborhood),1)

class BusinessTestClass(TestCase):
    def setUp(self):
        #set up a user class
        self.new_user=User(username="nish",email="nish@gmail.com")
        self.new_user.save()
        #set up neighborhood class
        self.thome = Neighborhood(name='nyati',location='thome',occupants_count=5,admin=self.new_user)
        self.thome.save_neighborhood()
        #set up business class
        self.kinyozi = Business(name='kinyozi',email='kinyozi@gmail.com',user=self.new_user,neighborhood=self.thome)
        self.kinyozi.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.kinyozi,Business))

    def test_save_business(self):
        self.kinyozi.save_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)>0)

    def test_delete_business(self):
        self.kinyozi.save_business()
        self.kinyozi.delete_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)<1)



class PostTestClass(TestCase):
    def setUp(self):
        #set up a user class
        self.new_user=User(username="nish",email="nish@gmail.com")
        self.new_user.save()
        #set up neighborhood class
        self.thome = Neighborhood(name='nyati',location='thome',occupants_count=5,admin=self.new_user)
        self.thome.save_neighborhood()
        #set up author class
        self.nish = Userm(name="Mary Wairimu Mbugua",idnum="34487520",user=self.new_user,neighborhood=self.thome)
        self.nish.save_user()
        #set up post class
        self.new_post=Post(post='Test testtttyyy post',author=self.nish)

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        Userm.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_post(self):
        self.new_post.save_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)>0)

    def test_delete_post(self):
        self.kinyozi.save_post()
        self.kinyozi.delete_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)<1)
