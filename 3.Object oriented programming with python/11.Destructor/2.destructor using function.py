# Python program to illustrate destructor
class Employee:
  
    # Initializing
    def __init__(self):
        print('Employee created.')
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
def func():
  obj = Employee()

def function1():
  obj1 = Employee()

func()
function1() 