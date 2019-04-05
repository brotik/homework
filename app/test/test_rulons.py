from app.lib_for_HW2 import total_rulons


def test_calculate_rulons():
    data = 7
    result = total_rulons(5, 6, 2.75)

    assert data == result
