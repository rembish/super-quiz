class Colour(object):  # Python 2.7
    def __init__(self, rgb):
        self.rgb = rgb

    def describe(self):
        return "#{0}".format(self.rgb)

class Blue(Colour):
    def __init__(self):
        super().__init__("0000FF")

print Blue().describe()
