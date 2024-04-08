import pytest

# Comment out this line to run the parametrize tests
@pytest.skip(allow_module_level=True)

@pytest.mark.parametrize(
   ('n', 'expected'), [
       (1, 2),
       (2, 3),
       (3, 4),
       (4, 5),
   ]
)
def test_increment(n, expected):
   assert n + 1 == expected
