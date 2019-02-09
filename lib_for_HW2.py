import math
def total_rulons(room_lenght, room_width, room_hight):

    """
    >>> total(5, 6, 2.75)
    7
    
    :param room_lenght:
    :param room_width:
    :param room_hight:
    :return:
    """
    perimetr = int((room_width * 2) + (room_lenght * 2))
    pieces_in_one_rulon = int(10 / (room_hight + 0.1))
    all_pieces = int(perimetr / 1.06)

    total_rulons = (math.ceil(all_pieces / pieces_in_one_rulon))
    return total_rulons