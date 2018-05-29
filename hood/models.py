from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name =  models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    occupants_count = models.PositiveIntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def get_neighborhood(cls):
        hood = Neighborhood.objects.all()
        return hood

    @classmethod
    def find_neighborhood(cls,pk):
        neighborhood=Neighborhood.objects.filter(pk=Neighborhood.pk)
        return neighborhood

    @classmethod
    def update_neighborhood(cls,id,name):
        updated = Neighborhood.objects.filter(id=Neighborhood.id).update(name=name)
        return updated

    @classmethod
    def update_occupants(cls,id,occupants_count):
        occupied = Neighborhood.objects.filter(id=Neighborhood.id).update(occupants_count=occupants_count)
        return occupied