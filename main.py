import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from linearreg import linear_reg
from mean_std_uncertainty import mean_std_uncertainty
from relative_error import relative_err

choice = 0
print("Welcome to the lab helper!")
q = "What do you want to do?\n1. mean & std & uncertainty\n2. linear regression\n3. relative error\n4. exit\n"
while True:
    choice = int(input(q))
    if choice == 1:
        mean_std_uncertainty()
    elif choice == 2:
        linear_reg()
    elif choice == 3:
        relative_err()
    elif choice == 4:
        break
    else:
        print("Invalid input!")
