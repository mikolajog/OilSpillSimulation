class Cell():
    def __init__(self, type):
        self.cell_type = type
        self.oil_points = []
        self.wind = (8, 90) #[m/s]
        self.concurrent = (0.12, 45) #[m/s]
        self.temp = 288#[K]

    def update_cell_type(self, new_type):
        self.cell_type = new_type

    def oil_mass_in_cell(self):
        mass = 0
        for op in self.oil_points:
            mass += op.mass

        return mass
    def oil_volume_in_cell(self):
        volume = 0
        for op in self.oil_points:
            volume +=op.oil_volume
        return volume