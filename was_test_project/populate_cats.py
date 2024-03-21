import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
					'was_test_project.settings')

import django 
django.setup() 
from cats.models import Student, Cat

def populate():
	students = Student.objects.order_by('last_name')
	cats = Cat.objects.order_by('name')

	students_list = []
	cats_list = {}

	for student in students:
		students_list.append({"first_name": student.first_name, "last_name": student.last_name})

	population_data = [
		{'first_name': 'Alyssa', 'last_name': 'Croft','cats':['Alex', 'Luna', 'Mittens']},
		{'first_name': 'John', 'last_name': 'Doe', 'cats':['Muffins']},
		{'first_name': 'Azam', 'last_name': 'Khan', 'cats':['Jill', 'Joe']},
	]
	
	for fake_student in population_data:
		if fake_student in students_list:
			continue
		else:
			fake_student.update({"num_cats":len(fake_student['cats'])})
			students_list.append(fake_student)

	for student in students_list:
		for key, val in student.items():
			s = add_student(student)
			if "cats" in student.keys():
				for cat in student['cats']:
					add_cat(s, cat)

def add_cat(owner, name): 
		c = Cat.objects.get_or_create(owner=owner, name=name)[0] 
		c.save() 
		return c 				
				
def add_student(student): 
	s = Student.objects.get_or_create(first_name = student['first_name'], last_name = student['last_name'])[0]
	s.save() 
	return s

# Start execution here! 
if __name__ == '__main__': 
	print('Starting cats population script...') 
	populate()