from django.db import models

from course.models import BaseModel

from django.contrib.auth.models import User

class Instructor(BaseModel):

    Profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='instructors-images/')

    description = models.TextField()

    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name = 'Instructor'

        verbose_name_plural = 'Instructors'

        

