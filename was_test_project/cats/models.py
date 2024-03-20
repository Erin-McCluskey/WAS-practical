from django.db import models

# Create your models here.
class Student(models .Model): 
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128) 
	num_cats = models.IntegerField(default=0)
	
	class Meta:
		verbose_name_plural = 'Student'
		
	def __str__(self): 
		return f"{self.first_name} {self.last_name}"

class Cat(models.Model): 
	owner = models.ForeignKey(Student, on_delete=models.CASCADE) 
	name = models.CharField(max_length=128) 

	def __str__(self): 
		return self.name