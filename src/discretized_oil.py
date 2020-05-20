from src.oil_point import Oil_point

class DiscretizedOil(object):

    def __init__(self,total_weight, start_coords):
        oil_points_list = []

        for i in range(40):
            oil_points_list.append(Oil_point(total_weight / 40, start_coords))

        self.oil_points_array = oil_points_list

