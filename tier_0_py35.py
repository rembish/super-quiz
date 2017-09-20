class Language:
    def hello(self, name):
        return "Hello from {0}".format(name)


class Python35(Language):
    def hello(self):
        return super(Python35, self).hello("Python 3.5")


print(Python35().hello())
