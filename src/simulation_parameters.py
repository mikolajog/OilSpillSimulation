#All parameters used in simulation (in future parameters provided by user)

#General parameters
SIMULATION_STEP_TIME = 3* 3600 #[s] - 1 hour
X_START = 56#70 *2
Y_START = 27#65 *2
TOTAL_WEIGHT = 400 * 1000 #[kg]
CELL_LENGTH = 10*1000 #[m] - 10km
NUMBER_OF_OIL_POINTS = 400

# Oil initial parameters
INIT_EMULSIFICATION_RATE = 0.3 # zakładam że 70% ropa bo nie mogę nigdzie znaleźć info :/
INIT_OIL_DENSITY = 900 #[kg/m^3]
INIT_CRUDE_OIL_BOILING_TMEP = 623.15 #[K]

#Advection parameters
ALPHA = 1.1
BETA = 0.03

#Spreading parameters

##Prameters needed to calculate D function
N = 10 # propagation factor - taken from main paper
G = 9.81 #[m/s^2] - gravitational acceleration
SEA_WATER_DENSITY = 1029 #[kg/m^3]
KINEMATIC_VISCOSITY = 1.1889 * pow(10, -6)  # [m^2/s] dla wody o zasoleniu 35g na 1kg wody
