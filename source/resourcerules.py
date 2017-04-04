def Map_One_To_Many(res1, res2):
    pass

class RulesManager:
    def __init__(self, *args):
        self.resources = args

    def empty(self):
        if self.resources:
            return False
        return True

    def add_rule(self, *args):
        pass

    def assign(self, *args):
        pass 

class Resource:
    def __init__(self, *args):
        self.name = args[0]
        self.items = dict()
        for item in args[1]:
            self.items[item] = []
    
    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key].append(value)
        
