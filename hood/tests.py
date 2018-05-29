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

