from Base import Tool, Relationship

class Job(Tool):
    def __init__(self, type, name, purposes):
        self.type = type
        Tool.__init__(self, name + " job", purposes)

class WorkEnvironment(Relationship):
    def __init__(self, members):
        Relationship.__init__(self, "work", members)
