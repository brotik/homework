def calculate_remaining_distance(fuel_consumption_on_100km, fuel_volume):
    """
    >>> calculate_remaining_distance(10, 10)
    100.0

    >>> calculate_remaining_distance(10, 8)
    80.0

    :param fuel_consumption_on_100km:
    :param fuel_volume:
    :return:
    """
    total = 100 / fuel_consumption_on_100km * fuel_volume
    return total