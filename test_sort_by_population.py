import pytest
from sort_by_population import sort_by_population

def test_sort_by_population():
    data = [
        ["Ukraine", 603500, 41500000],
        ["USA", 9833520, 331000000],
        ["France", 551695, 67000000]
    ]
    result = sort_by_population(data)
    assert result[0][0] == "Ukraine"  # Найменше населення
    assert result[-1][0] == "USA"  # Найбільше населення