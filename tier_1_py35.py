class Colour(object):  # Python 3.5
    def __init__(self, rgb):
        self.rgb = rgb

    def describe(self):
        return "#{0}".format(self.rgb)

class Yellow(Colour):
    def __init__(self):
        super().__init__("FFFF00")

print(Yellow().describe())
