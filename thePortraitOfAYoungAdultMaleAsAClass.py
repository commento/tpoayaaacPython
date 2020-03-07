from Family import Family, Parent
from Job import Job
from Base import Person, Language, Time

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

        if location == "Berlin":
            self.language += [Language("human-human", "english", "upper intermediate", ["communicative", "informative"])] + [Language("human-human", "german", "basic", ["communicative", "informative"])]


    def __repr__(self):
        pass


time = Time(2012)
mother = Parent("M********", 76, "45°35'49.3\"N 9°22'15.8\"E", "employee")
father = Parent("A******", 75, "45°35'49.3\"N 9°22'15.8\"E", "manager")
youngAdult = YoungAdultMale("R*******", 25, "45°35'49.3\"N 9°22'15.8\"E", mother, father)

familyMembers = {"mother": mother, "father" : father, "youngAdult" : youngAdult}
family = Family(familyMembers)

youngAdultJob = Job("VDU operator", "software developer", "Agrate", ["money", "personal fulfillment", "be an adult"])
youngAdult.findAJob(youngAdultJob)

time.yearsHavePassed(1)
youngAdult.loseAJob()

youngAdultJob = Job("VDU operator", "software developer", "Rozzano", ["money", "personal fulfillment", "be an adult"])
youngAdult.findAJob(youngAdultJob)

time.yearsHavePassed(2)
family.memberLeave("R*******")

youngAdult.moveTo("45°28'57.2\"N 9°13'22.4\"E")

time.yearsHavePassed(2)
youngAdult.leaveAJob()
youngAdult.moveTo("52°32'26.2\"N 13°23'53.5\"E")

youngAdultJob = Job("VDU operator", "software developer internship / limited time contract", "Berlin", ["need"])
youngAdult.findAJob(youngAdultJob)
time.yearsHavePassed(1)
youngAdult.loseAJob()

youngAdultJob = Job("VDU operator", "software developer", "Berlin", ["money", "personal fulfillment", "be an adult"])
youngAdult.findAJob(youngAdultJob)
time.yearsHavePassed(1)
youngAdult.leaveAJob()

time.yearsHavePassed(1)
youngAdult.moveTo("45°28'55.7\"N 9°15'46.5\"E")

