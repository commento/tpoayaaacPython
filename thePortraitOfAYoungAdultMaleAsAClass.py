from Family import Family, Parent
from Job import Job
from Base import Person, Language

class YoungAdultMale(Person):
    def __init__(self, name, age, location, mother, father, siblings = None):
        self.mother = mother
        self.father = father
        Person.__init__(self, name, age, location, Language("human-human", "italian", "mother tongue", ["communicative", "informative", "ironic", "sarcastic"]))
        self.code = None
        self.siblings = siblings
        self.isOnlyChild = False
        if siblings is None:
            self.isOnlyChild = True

        self.hasLeftFamily = False

    def startCoding(self):
        code = Language("human-machine", ["c/c++","python"], "average", ["prodedural", "informative"])

    def canCode(self):
        return code is not None

    def moveTo(location):
        self.location = location

        if location == "Berlin":
            self.language += [Language("human-human", "english", "upper intermediate", ["communicative", "informative"])] + [Language("human-human", "german", "basic", ["communicative", "informative"])]


    def __repr__(self):
        pass



mother = Parent("Mariangela", 76, "Burago di Molgora", "employee")
father = Parent("Antonio", 75, "Burago di Molgora", "manager")
youngAdult = YoungAdultMale("Riccardo", 25, "Burago di Molgora", mother, father)

familyMembers = {"mother": mother, "father" : father, "youngAdult" : youngAdult}
family = Family(familyMembers)

youngAdultJob = Job("VDU operator", "software developer", "Agrate", ["money", "personal fulfillment", "be an adult"])
youngAdult.findAJob(youngAdultJob)

family.memberLeave("Riccardo")

print(youngAdult.language[0].name)
print(youngAdult.hasLeftFamily)
print(youngAdult.hasAJob())
print(mother.isSad())

