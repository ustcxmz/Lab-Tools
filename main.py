from linearreg import linear_reg
from mean_std_uncertainty import mean_std_uncertainty
from relative_error import relative_err
from polynomial_reg import polynomial_reg

choice = 0
print("Welcome to the lab helper!")
q = (
    "What do you want to do?\n"
    "1. mean & std & uncertainty\n"
    "2. linear regression\n"
    "3. polynomial regression\n"
    "4. relative error\n"
    "5. exit\n"
    "Enter your choice:\n"
)
while True:
    choice = int(input(q))
    if choice == 1:
        mean_std_uncertainty()
    elif choice == 2:
        linear_reg()
    elif choice == 3:
        polynomial_reg()
    elif choice == 4:
        relative_err()
    elif choice == 5:
        break
    else:
        print("Invalid input!")
