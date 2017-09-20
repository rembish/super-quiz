class Reptile(object):  # Both Pythons
    def describe(self):
        return "Reptile"

class Snake(Reptile):
    def describe(self):
        return "Snake"

class Python(Snake):
    def describe(self):
        return "Python"

print(super(Python, Python()).describe())
print(super(Snake, Snake).describe(Python()))
