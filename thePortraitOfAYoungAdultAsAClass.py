from Family import Family, Parent
from Job import Job
from Base import Person, Language

class YoungAdult(Person):
    def __init__(self, name, age, location, mother, father, siblings = None):
        self.mother = mother
        self.father = father
        Person.__init__(self, "Riccardo", 31, location, Language("human", "italian", "mother tongue", ["communicative", "informative", "ironic", "sarcastic"]))
        self.siblings = siblings
        self.isOnlyChild = False
        if siblings is None:
            self.isOnlyChild = True

        self.hasLeftFamily = False

    def __repr__(self):
        pass



mother = Parent("Mariangela", 76, "Burago di Molgora")
father = Parent("Antonio", 75, "Burago di Molgora")
youngAdult = YoungAdult("Riccardo", 31, "Berlin", mother, father)

familyMembers = {"mother": mother, "father" : father, "youngAdult" : youngAdult}
family = Family(familyMembers)


youngAdultJob = Job("VDU operator", "software developer", ["money", "personal fulfillment", "be an adult"])
youngAdult.findAJob(youngAdultJob)

family.memberLeave("Riccardo")

print(youngAdult.language.name)
print(youngAdult.hasLeftFamily)
print(youngAdult.hasAJob())
print(mother.isSad())

