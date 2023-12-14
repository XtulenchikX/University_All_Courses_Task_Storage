from class_organization import Employee, Department

ne_frik = Employee("Safin Ramaz", "Uborshik")
boss = Employee("Maksim Stetsuk 777", "Big Boss")

prog1 = Employee("Andrey Malahov", "Programist")
prog2 = Employee("John Snow", "Programist")

des1 = Employee("Naruto", "designer")
des2 = Employee("Saske", "designer")

test1 = Employee("Gleb Baranov", "tesirovshik")
test2 = Employee("Sherlock Holmes", "testirovshik")

company = Department('IT company APPLE EATERS')
dep1 = Department('Rabotnichki')
dep2 = Department('Programisti')
dep3 = Department('Designeri')
dep4 = Department('Testirovshiki')

company.add_employee(ne_frik)
company.add_employee(boss)
company.add_department(dep1)

dep1.add_department(dep2)
dep1.add_department(dep3)
dep1.add_department(dep4)

dep2.add_employee(prog1)
dep2.add_employee(prog2)
dep3.add_employee(des1)
dep3.add_employee(des2)
dep4.add_employee(test1)
dep4.add_employee(test2)



company.show_info()
print('---------')

dep1.show_info()
print('---------')

dep3.show_info()
print('---------')

des1.show_info()



# developer1 = Employee("John Doe", "Developer")
# developer2 = Employee("Jane Doe", "Developer")

# manager1 = Employee("Alice Smith", "Manager")
# manager2 = Employee("Bob Johnson", "Manager")

# company = Department('Softs Scill')
# dep1 = Department('First')
# dep2 = Department('Second')
# dep3 = Department('Third')

# company.add_department(dep1)
# company.add_department(dep2)

# dep1.add_employee(manager1)
# dep2.add_employee(manager2)
# dep3.add_employee(developer1)
# dep3.add_employee(developer2)
# dep2.add_department(dep3)

# company.show_info()


