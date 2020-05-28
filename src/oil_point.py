from src.simulation_parameters import *
import math
class Oil_point():


    def __init__(self, mass, start_coordinates):
        self.mass = mass
        # coordinates relative to the starting point
        # in km from starting point
        self.relatives_coordinates = [0,0] #[km]
        # coordinates of cell to with oil point is assigned
        self.assigned_cell = start_coordinates
        self.current_emulsification_rate = INIT_EMULSIFICATION_RATE
        self.density = INIT_OIL_DENSITY #[kg/m^3]
        self.oil_volume =self.density * self.mass
        self.boiling_temp = INIT_CRUDE_OIL_BOILING_TMEP#[K]


    def compute_evaporation(self,temp, op_in_cell):
        # some draft of implementing evaporation
        K = 1.25 * pow(10, -3)  # [m/s] - mass transfer coefficient
        R = 8.314  # [J/(mol*K] - gas constant
        delta_t = SIMULATION_STEP_TIME  # [s] - iteration step
        MI = 0.25 #[kg/mol] - molecular weight

        P0I = 1000*math.exp(-1*(4.4+math.log(self.boiling_temp))*(1.803*(self.boiling_temp/temp - 1)-0.803*math.log(self.boiling_temp/temp)))

        #MI = 2.410*pow(10,-6)*(pow(self.boiling_temp, 2.847)*pow(self.density/SEA_WATER_DENSITY,-2.130))
        #print(MI)
        x1 = 1/NUMBER_OF_OIL_POINTS #przyjmuje bardzo mocne prybliżenie, że w każdym oil poincie stosunek masy moleowej jest taki sam

        A = CELL_LENGTH*CELL_LENGTH/op_in_cell

        delta_mI = K *MI *P0I * x1 * A *delta_t / (R * temp)

        self.mass -= delta_mI
        #print(self.mass)

    def compute_emulsification(self, wind_speed):
        #wind speed [m/s]
        delta_t = SIMULATION_STEP_TIME  # [s] - iteration step time
        delta_emulsification_rate = 2.0*pow(10,-6)*pow((wind_speed+1),2)*(1-self.current_emulsification_rate/0.7)*delta_t
        self.current_emulsification_rate += delta_emulsification_rate
        print(delta_emulsification_rate)