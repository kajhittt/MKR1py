import pytest
from read_and_sort import read_and_sort

@pytest.fixture
def file_data(tmpdir):
    file_path = tmpdir.join("countries.txt")
    file_path.write("Ukraine, 603500, 41500000\nUSA, 9833520, 331000000\nFrance, 551695, 67000000\n")
    return str(file_path)

def test_read_and_sort(file_data):
    sorted_by_area, sorted_by_population = read_and_sort(file_data)
    assert sorted_by_area[0][0] == "France"
    assert sorted_by_population[0][0] == "Ukraine"