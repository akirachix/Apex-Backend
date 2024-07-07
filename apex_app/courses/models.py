from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length= 20)
    course_id = models.PositiveSmallIntegerField()
    course_description = models.CharField(max_length=255, default='')
    
    def __str__(self) :
        
        return f"{self.course_name}  {self.course_id}"
 


