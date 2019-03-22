import math
def total_rulons(room_lenght, room_width, room_hight):

    """
    >>> total_rulons(5, 6, 2.75)
    7
    
    :param room_lenght:
    :param room_width:
    :param room_hight:
    :return:
    """
    reserv = 0.1
    widht_of_rulon = 1.06
    perimetr = int((room_width * 2) + (room_lenght * 2))
    pieces_in_one_rulon = int(10 / (room_hight + reserv))
    all_pieces = int(perimetr / widht_of_rulon)

    total_rulons = (math.ceil(all_pieces / pieces_in_one_rulon))
    return total_rulons
