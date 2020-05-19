class Cell():
    def __init__(self, type):
        self.cell_type = type
        self.oil_points = [20]
        self.wind = 1
        self.concurrent = 1

    def update_cell_type(self, new_type):
        self.cell_type = new_type