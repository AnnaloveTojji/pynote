# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True

# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())

# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person( object ):	

		# __init__ is known as the constructor		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)

# child class
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				# invoking the __init__ of the parent class
				Person.__init__(self, name, idnumber)

				
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")	

# calling a function of the class Person using its instance
a.display()
