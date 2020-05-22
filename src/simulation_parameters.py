#All parameters used in simulation (in future parameters provided by user)

#General parameters
SIMULATION_STEP_TIME = 3600 #[s] - 1 hour
X_START = 100
Y_START = 60
TOTAL_WEIGHT = 400 #[tonnes]
CELL_LENGTH = 10000 #[m] - 10km

# Oil initial parameters
INIT_EMULSIFICATION_RATE = 1.0 # # zakładam że 100% ropa bo nie mogę nigdzie znaleźć info :/
INIT_OIL_DENSITY = 900 #[kg/m^3]

#Advection parameters
ALPHA = 1.1
BETA = 0.03

#Spreading parameters

##Prameters needed to calculate D function
N = 3 # propagation factor - taken from main paper
G = 9.81 #[m/s^2] - gravitational acceleration
SEA_WATER_DENSITY = 1029 #[kg/m^3]
KINEMATIC_VISCOSITY = 1.1889 * pow(10, -6)  # [m^2/s] dla wody o zasoleniu 35g na 1kg wody
