class Oil_point():


    def __init__(self, mass, start_coordinates):
        self.mass = mass
        # coordinates relative to the starting point
        # in km from starting point
        self.relatives_coordinates = [0,0]
        # coordinates of cell to with oil point is assigned
        self.assigned_cell = start_coordinates
        self.current_emulsification_rate = 1.0 # zakładam że 100% ropa bo nie mogę nigdzie znaleźć info :/
        self.density = 900 #[kg/m^3]
        self.oil_volume =self.density * self.mass


    # def compute_evaporation(self):
    #     K = 1.25 * pow(10, -3)  # [m/s] - mass transfer coefficient
    #     R = 8.314  # [J/(mol*K] - gas constant
    #     delta_t = 60  # [s] - iteration step
    #     MI = 0.25 #[kg/mol] - molecular weight
    #
    #     P0I =
    #
    #     x1 =
    #
    #     delta_mI = K *MI *P0I * x1 * A *delta_t / (R * T)

    def compute_emulsification(self, wind_speed):
        #wind speed [m/s]
        delta_emulsification_rate = 2.0*pow(10,-6)*pow((wind_speed+1),2)*(1-self.current_emulsification_rate/0.7)*60
        self.current_emulsification_rate += delta_emulsification_rate
        return delta_emulsification_rate