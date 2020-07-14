class Person:
    department = "School of Technology , ADBU"  # class variable

    def __init__(self, name, location):
        self.name = name
        self.location = location


person = Person("Christopher Brooks", "Ann Arbor, MI, USA")

print(person.department)

print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))


class Engineer(Person):
    college = "ADBU"


en = Engineer(name="kishor", location="Ghy")

print('{} worked in {}'.format(en.name, en.college))

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]


print(max(store1 + store2))

print(min(store2 + store1))

for item in store1:
    print("item in store 1 ", item)

for item in store2:
    print("item in store 2 ", item)
