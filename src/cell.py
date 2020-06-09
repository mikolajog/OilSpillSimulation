from src.simulation_parameters import CELL_LENGTH
class Cell():
    def __init__(self, type):
        self.cell_type = type
        self.oil_points = []
        self.wind = [1.67, 82] #[m/s]
        self.concurrent = [0.32, 8.0] #[m/s]
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

    def average_emulsion_density(self):
        cell_density = 0
        for op in self.oil_points:
            cell_density += op.emulsion_density
        return cell_density/len(self.oil_points)

    def average_cell_thickness(self):
        h = self.oil_mass_in_cell()/(CELL_LENGTH*CELL_LENGTH*self.average_emulsion_density())