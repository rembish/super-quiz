class Language:
    def hello(self, name):
        return "Hello from {0}".format(name)


class Python27(Language):
    def hello(self):
        return super(Python27, self).hello("Python 2.7")


print Python27().hello()
