import pytest

# Comment out this line to run the fixture tests
@pytest.skip(allow_module_level=True)


@pytest.fixture()
def fixture_name():
    fixture_value = 'some data'
    return fixture_value

def test_something_with_fixture(fixture_name):
    assert fixture_name == 'some data'
