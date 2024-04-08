import pytest

# Comment out this line to run the database test
@pytest.skip(allow_module_level=True)

class MyDatabase():
    def __init__(self):
        print("\n-- connect to database --")

    def close(self):
        print("\n-- disconnect from database --")

    def retrieve_answer(self):
        print("\n-- MyDatabase::some_action() --")
        return 42


@pytest.fixture()
def database():
    db = MyDatabase()  # setup
    yield db
    db.close()  # teardown


def test_database(database):
    result = database.retrieve_answer()
    assert result == 42