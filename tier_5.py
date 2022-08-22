class Human(object):  # Both Pythons
    @classmethod
    def mynameis(cls):
        print("Human said: I'm {0}".format(cls.__name__))

class Pepa(Human):
    @classmethod
    def mynameis(cls):
        print("Pepa said: I'm {0}".format(cls.__name__))
        cls.__super.mynameis()

Pepa._Pepa__super = super(Pepa, Pepa)

class Josef(Pepa):
    pass

Josef._Josef__super = super(Josef)

Human().mynameis()
Pepa().mynameis()
Josef().mynameis()
