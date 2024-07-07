from django.db import models

# Create your models here.
class Lessons(models.Model):
    lesson_id = models.PositiveSmallIntegerField()
    lesson_description = models.TextField()
    course_id = models.PositiveSmallIntegerField()
    teacher_id = models.PositiveSmallIntegerField()
    
    def __str__(self) :
        
        return f"{self.lesson_id}  {self.lesson_description}"