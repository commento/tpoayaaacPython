from Base import Tool

class Job(Tool):
    def __init__(self, type, name, purposes):
        self.type = type
        Tool.__init__(self, name + " job", purposes)

