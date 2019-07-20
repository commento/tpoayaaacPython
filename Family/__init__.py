from Job import Job
from Base import Person, Language

class Parent(Job, Person):
    def __init__(self, name, age, location):
        Person.__init__(self, name, age, location, Language("human-human", "italian", "mother tongue", ["communicative", "informative", "educational"]))
        Job.__init__(self, "VDU operator", "manager", ["money", "family well-being", "personal fulfillment"])

        self.hasChildren = True

class Siblings:
    def __init__(self, names):
        # TODO: to be extended, only for completness but not part of this scenario
        self.names = names

class Family:
    def __init__(self, members):
        self.members = members

    def discuss(self):
        for member in members:
            pass

    def memberLeave(self, memberName):
        for idx, member in self.members.items():
            if member.name == memberName:
                member.hasLeftFamily = True
            elif idx == "mother":
                member.mood = "little depressed"
            else:
                member.mood = "little sad"

