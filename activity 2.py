class person():
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
    def display(self):
        print(self.name, self.id_num)

class employee(person):
    def __init__(self, name, id_num, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, id_num)

obj = employee("John", 12345, 40000, "intern")
obj.display()
