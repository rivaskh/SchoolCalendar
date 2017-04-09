class SchoolAnalyzer:
    def read_user_data(self, **kwargs):
        if 'source' not in kwargs:
            return ""
        self.source = kwargs['source']
        return self.source.read()

    def parse(self, *args, **kwargs):
        if 'parser' not in kwargs:
            return None
        self.parser = kwargs['parser']
        return self.parser.parse(*args) 
