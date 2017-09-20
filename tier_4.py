class Meetup(object):  # Both Pythons
    name = "Meetup"

class PythonMeetup(Meetup):
    name = "Python Meetup"

class PyVo(PythonMeetup):
    name = "PyVo"
    type = super(PythonMeetup)

print(Meetup.name)
print(PythonMeetup().name)
print(PyVo().name)
print(PyVo().type.name)
print(PyVo.type.name)
