class Czechia(object):  # Both Pythons
    def whereami(self):
        print("I'm in Czechia")

class Slovakia(object):
    def whereami(self):
        print("I'm in Slovakia")
        super(Slovakia, self).whereami()

# Dash war begins
class Czechoslovakia(Czechia, Slovakia):
    def whereami(self):
        super(Czechoslovakia, self).whereami()
        print("I'm in Czechoslovak Republic")

# Dash war continues (I can't use dash in class name)
class Czecho_SlovakRepublic(Slovakia, Czechia):
    def whereami(self):
        super(Czecho_SlovakRepublic, self).whereami()
        print("I'm in Czecho-Slovak Republic")

Czechia().whereami()
print("---")
Czechoslovakia().whereami()
print("---")
Czecho_SlovakRepublic().whereami()
