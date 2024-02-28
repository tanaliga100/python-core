from teacher import Teacher

class Student(Teacher):
  def __init__(self, name, id_number, course, is_on_probi):
    self.name = name
    self.id_number = id_number
    self.course = course
    self.is_on_probi = is_on_probi
  
  def Hi(self):
    return ("HI "+ self.name)
  
  def Teach(self):
    return "Hello from teacher"
    
    
    