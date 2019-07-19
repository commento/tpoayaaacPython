class Tool:
    def __init__(self, name, purposes):
        self.name = name
        self.purposes = purposes

class Language(Tool):
    def __init__(self, type, name, purposes):
        self.type = type
        Tool.__init__(self, name + " language", purposes)

class Job(Tool):
    def __init__(self, type, name, purposes):
        self.type = type
        Tool.__init__(self, name + " job", purposes)

class Person():
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
        self.mood = "good"

class Parent(Job):
    def __init__(self, name, age):
        Person.__init__(self, name, age, Language("human", "italian", ["communicative", "informative", "educational"]))
        Job.__init__(self, "VDU operator", "manager", ["money", "family well-being", "personal fulfillment"])

        self.hasChildren = True

class Siblings:
    def __init__(self, names):
        # TODO: to be extended, only for completness but not part of this scenario
        self.names = names

class YoungAdult():
    def __init__(self, mother, father, siblings = None):
        self.mother = mother
        self.father = father
        Person.__init__(self, "Riccardo", 31, Language("human", "italian", ["communicative", "informative", "ironic", "sarcastic"]))
        self.siblings = siblings
        self.isOnly = False
        if siblings is None:
            self.isOnlyChild = True

        self.job = None
        self.hasAJob = False

        self.hasLeftFamily = False

    def __repr__(self):
        pass

    def findAJob(self, job):
        self.hasAJob = True
        self.job = job

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



mother = Parent("Mariangela", "76")
father = Parent("Antonio", "75")
youngAdult = YoungAdult(mother, father)

familyMembers = {"mother": mother, "father" : father, "youngAdult" : youngAdult}
family = Family(familyMembers)


youngAdultJob = Job("VDU operator", "software developer", ["money", "personal fulfillment", "fill like an adult"])
youngAdult.findAJob(youngAdultJob)

family.memberLeave("Riccardo")

print(youngAdult.language.name)
print(youngAdult.hasLeftFamily)

