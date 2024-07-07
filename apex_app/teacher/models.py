from django.db import models

# Create your models here.

class Teachers(models.Model):
    teacher_name = models.CharField(max_length= 20)
    email = models.EmailField()
    school_code = models.PositiveSmallIntegerField()
    teacher_id = models.PositiveSmallIntegerField()
    password = models.CharField(max_length= 20)
    user_name =  models.CharField(max_length= 20)
    phone_number = models.CharField(max_length= 20)
    
   

    def __str__(self):
         return f"{self.first_name} {self.last_name}"
