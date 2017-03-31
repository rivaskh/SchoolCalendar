import pytest
from source.resourcemanager import ResourceException, Resource

class TestResource:
    def test_Initialize_Resource_With_No_ResourceName(self):
        with pytest.raises(ResourceException) as excinfo:
            res = Resource()
        excinfo.match('No Resource Name')

    def test_Initialize_Resource_With_Teachers(self):
        res = Resource(resource_name="teacher")
        assert res

    def test_Possible_Values_To_Resources(self):
        teachers = ['A','B','C']
        res = Resource(resource_name = "teacher", resources=teachers)
        assert res.number_of_resources() == 3
