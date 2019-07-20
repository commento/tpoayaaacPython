class Tool:
    def __init__(self, name, purposes):
        self.name = name
        self.purposes = purposes

class Language(Tool):
    def __init__(self, type, name, level, purposes):
        self.type = type
        Tool.__init__(self, name + " language", purposes)

class Person():
    def __init__(self, name, age, location, language):
        self.name = name
        self.age = age
        self.language = language
        self.location = location
        self.job = None

        self.__mood = "ok"

    def isSad(self):
        return True if "sad" or "depressed" in self.mood else False

    def hasAJob(self):
        return False if self.job is None else True

    def findAJob(self, job):
        self.job = job

class Relationship:
    def __init__(self, kind, members):
        self.kind = kind
        self.members = members

    def isBroken(self, member1, member2):
        if member1 in members and member2 in members:
            return True if member1.dontlike(member2) or member2.dontLike(member1)
        else:
            return "Not in a Relationship"