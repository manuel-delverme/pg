import sys

import experiment_buddy
import torch

RUN_SWEEP = 10
REMOTE = 1
NUM_PROCS = 10

sweep_yaml = "sweep_seeds.yaml" if RUN_SWEEP else False
HOST = "mila" if REMOTE else ""  # in host
DEBUG = '_pydev_bundle.pydev_log' in sys.modules.keys()

eval_runs = 5
pi_lr = 1e-3
v_lr = 1e-3
gamma = 0.99
eps_clip = 0.1
opt_epochs = 10
horizon = 256 if DEBUG else 2048
batch_size = 32
eta = 0.1
grid_size = 8
agent = "pg"
save_interval = 10
max_steps = int(300)
seed = 984
h_dim = 32
# wandb_mode = "online" if DEBUG else "offline"

use_cuda = False

experiment_buddy.register(locals())
device = torch.device("cuda" if use_cuda else "cpu")

################################################################
# Derivative parameters
################################################################
# esh = """
# #SBATCH --mem=24GB
# """
tb = experiment_buddy.deploy(host=HOST, sweep_yaml=sweep_yaml, proc_num=NUM_PROCS)
