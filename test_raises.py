import pytest

# Comment out this line to run the raises test
@pytest.skip(allow_module_level=True)


def insert_coins(quarters):
    if type(quarters) is not int:
        raise TypeError('quarters must be an integer')


def test_insert_coin_when_quarters_is_string_raises():
    with pytest.raises(TypeError):
        insert_coins('foobar')
