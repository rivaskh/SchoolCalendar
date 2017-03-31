class ResourceException(Exception):
    pass

class Resource:
    def __init__(self, **kwargs):
        if "resource_name" not in kwargs:
            raise ResourceException("No Resource Name")
        self.resource = kwargs['resource_name']

        self.resources = []
        if "resources" in kwargs:
            self.resources = kwargs['resources']

    def number_of_resources(self):
        return len(self.resources)
