class employee:   # A high-level class
    def __init__(self):
        self.developers=Developer()

    def develop(self):
        return self.developers.develops()

class Developer:   # Abstract class
    def __init__(self):
        self.front=frontend()
        self.back=backend()

    def develops(self):
        self.front.develop()
        self.back.develop()

class frontend:    # A low-level class
    def develop(self):
        self.display()

    def display(self):
        print("I am a Frontend Developer")


class backend:    # a low-level class
    def develop(self):
        self.display()

    def display(self):
        print("I am a Backend developer")


developer=employee()
developer.develop()

