import pytest
from sort_by_area import sort_by_area

def test_sort_by_area():
    data = [
        ["Ukraine", 603500, 41500000],
        ["USA", 9833520, 331000000],
        ["France", 551695, 67000000]
    ]
    result = sort_by_area(data)
    assert result[0][0] == "France"  # Найменша площа
    assert result[-1][0] == "USA"  # Найбільша площа