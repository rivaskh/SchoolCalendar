import pytest
from source.schoolcalendar import SchoolAnalyzer

    




@pytest.fixture
def SA():
    return SchoolAnalyzer()

class TestReader:
    def read(self):
        return "TestData"

class TestGetInputs:
    def test_Get_Inputs_From_User(self, SA):
        SA.read_user_data()

    def test_Read_Input_From_TestReader(self, SA):
        data = SA.read_user_data(source=TestReader())
        assert data == "TestData"


class TestParser():
    def __init__(self, expected):
        self.expected = expected

    def parse(self, *args):
        return self.expected

testdata = [
        ("",""),
        ("if teacher teaches math, he should also teach science","teach(math).teach(science) + ~teach(math).teach(science) + ~teach(math).~teach(science)")
        ]
@pytest.mark.parametrize("statement, expected", testdata)
def test_Parse_Statements(statement, expected, SA):
    testparser = TestParser(expected)
    data = SA.parse(statement, parser=testparser)
    assert data == expected

