import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
					'was_test_project.settings')

import django 
django.setup() 
from cats.models import Student, Cat

def populate():
	students = Student.objects.order_by('last_name')
	students_list = []

	for student in students:
		students_list.append({"first_name": student.first_name, "last_name": student.last_name, "num_cats": student.num_cats})
	
	population_data = [
		{'first_name': 'Alyssa', 'last_name': 'Croft', 'num_cats':3, 'cats':['Alex', 'Luna', 'Mittens']},
		{'first_name': 'John', 'last_name': 'Doe', 'num_cats':1, 'cats':['Muffins']},
		{'first_name': 'Azam', 'last_name': 'Khan', 'num_cats':2, 'cats':['Jill', 'Joe']},
	]
	
	for fake_student in population_data:
		if fake_student in students_list:
			continue
		else:
			students_list.append(fake_student)

	for student in students_list:
		for key, val in student.items():
			s = add_student(student)
			for cat in student['cats']:
				add_cat(s, cat)

def add_cat(owner, name): 
		c = Cat.objects.get_or_create(owner=owner, name=name)[0] 
		c.save() 
		return c 				
				
def add_student(student): 
	s = Student.objects.get_or_create(first_name = student['first_name'], last_name = student['last_name'], num_cats= student['num_cats'])[0]
	s.save() 
	return s

# Start execution here! 
if __name__ == '__main__': 
	print('Starting cats population script...') 
	populate()