class OrgStructure:
  def __init__(self, name):
      self.name = name

  def show_info(self, indent=""):
      pass

class Employee(OrgStructure):
  def __init__(self, name, position):
      super().__init__(name)
      self.position = position

  def show_info(self, indent=""):
      print(f"{indent}{self.position}: {self.name}")

class Department(OrgStructure):
  def __init__(self, name):
      super().__init__(name)
      self.structure = []

  def add_employee(self, employee):
      self.structure.append(employee)

  def remove_employee(self, employee):
      self.structure.remove(employee)

  def add_department(self, department):
      self.structure.append(department)

  def remove_department(self, department):
      self.structure.remove(department)

  def show_info(self, indent=""):
      print(f"{indent}Department:{self.name}")
      for elem in self.structure:
          elem.show_info(indent + "   ")