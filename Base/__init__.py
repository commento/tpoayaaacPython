from enum import Enum
class StressLevel(Enum):
    RELAX = 0
    TENSE = 1
    
class Tool:
    def __init__(self, name, purposes):
        self.name = name
        self.purposes = purposes

class Language(Tool):
    def __init__(self, type, name, level, purposes):
        self.type = type
        self.level = level
        Tool.__init__(self, name + " language", purposes)

class Stress():
    def __init__(self, level):
        self.level = level

class Person():
    def __init__(self, name, age, location, language):
        self.name = name
        self.age = age
        self.language = [language]
        self.location = location
        self.job = None

        self.__mood = "ok"
        self.__peopleNotLiked = []
        self.__stress = None

    def isSad(self):
        return True if "sad" or "depressed" in self.mood else False

    def hasAJob(self):
        return False if self.job is None else True

    def findAJob(self, job):
        self.job = job

    def dontLike(self, person):
        return True if person in self.__peopleNotLiked else False

    def hasStress(level):
        self.stress = Stress.__init__(level)

    def isStressed():
        return True if self.stress else False

    def increaseStress():
        if self.stress:
            self.stress.level +=1
        else:
            self.stress = Stress.__init__(1)

    def decreaseStress():
        if self.stress:
            self.stress.level -=1

class Relationship:
    def __init__(self, kind, members):
        self.kind = kind
        self.members = members

    def isBrokenBetween(self, member1, member2):
        if member1 in members and member2 in members:
            return True if member1.dontlike(member2) or member2.dontLike(member1) else False
        else:
            return "Not in a Relationship"