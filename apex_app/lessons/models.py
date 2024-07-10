from django.db import models
from courses.models import Courses
from teacher.models import Teachers
# Create your models here.
class Lessons(models.Model):
    lesson_level = models.PositiveSmallIntegerField()
    lesson_description = models.TextField()
    teacher_code = models.ForeignKey(Teachers, default=None, on_delete=models.CASCADE, related_name='teacher_code')
    course_code = models.ForeignKey(Courses, default=None, on_delete=models.CASCADE, related_name='course_code')
    
    def __str__(self) :
        
        return f"{self.lesson_level}  {self.lesson_description}"