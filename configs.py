# Directories
TENSORBOARD_DIR = "/home/oliver/GitHub/a3c_trading/tb/"
MODEL_DIR = "/home/oliver/GitHub/a3c_trading/model/"
DATA_DIR = "/home/oliver/GitHub/a3c_trading/data/"
PLOTS_DIR = "/home/oliver/GitHub/a3c_trading/plots/"

# Data files
POSTFIX = "['RTS-12.15']w5k"
TEST_POSTFIX = "['RTS-3.16', 'RTS-6.16']w5k"
POSTFIX_REAL = "['RTS-12.15']"
TEST_POSTFIX_REAL = "['RTS-3.16', 'RTS-6.16']"


# Network architecture
EXTRA_DENSE = False
N_HIDDEN = 64
DROPOUT = True
TRAINING = False
COOL_V = True
COOL_A = False
DEP = 1
GAMMA = 0.8
LOAD_MODEL = False
LR = 1e-4
COMISSION = 20  # rubls
PRICE_MAG = 1 / 5000  # среднне различие между макс и мин ценой за 5000 шагов

# stuff I needed to define to make it run
FRAMES_STACKED = 1
TRAIN_DATA = DATA_DIR + "[_RTS-9.15_, _RTS-12.15_, _RTS-3.16_]"
NUM_WORKERS = 1
