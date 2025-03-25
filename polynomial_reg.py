import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def polynomial_reg(
    power=2,
    x=[8.214, 7.408, 6.879, 5.490, 5.196],
    y=[1.610, 1.270, 1.062, 0.478, 0.358],
    xlabel="v(10^14Hz)",
    ylabel="U(V)",
    title="U vs v",
):
    learning_rate = 0.01
    q1 = "Input the highest power of the polynomial you want to fit as an integer: "
    power = int(input(q1))
    q2 = "Input the x values as a list:\n"
    q3 = "Input the y values as a list:\n"
    x = np.array(eval(input(q2)))
    y = np.array(eval(input(q3)))
    if len(x) != len(y):
        print("Length of x and y must be equal")
        return
    q4 = "Input x label here as a string\n"
    xlabel = input(q4)
    q5 = "Input y label here as a string\n"
    ylabel = input(q5)
    q6 = "Input title here as a string\n"
    title = input(q6)
    
    # 数据标准化
    scaler_x = StandardScaler()
    scaler_y = StandardScaler()
    x_scaled = scaler_x.fit_transform(x.reshape(-1, 1)).flatten()
    y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()
    
    y_pred = np.zeros(len(x_scaled))
    X = np.zeros((power + 1, len(x_scaled)))
    X[0] = np.ones(len(x_scaled))
    for i in range(1, power + 1):
        X[i] = x_scaled**i
    W = np.random.rand(power + 1)
    grad = np.zeros(power + 1)
    count = 0
    while True:
        y_pred = W @ X
        for i in range(power + 1):
            grad[i] = np.mean((y_pred - y_scaled) * X[i])
        W -= grad * learning_rate
        if count > 2000:
            break
        count += 1
        if count % 100 == 0:
            print(f"Iteration {count}: W = {W}")
            print(f"Loss = {2 * np.mean((y_pred - y_scaled)**2)}")
    
    # 反标准化
    x_arr = np.linspace(min(x), max(x), 100)
    x_arr_scaled = scaler_x.transform(x_arr.reshape(-1, 1)).flatten()
    X_arr = np.zeros((power + 1, len(x_arr_scaled)))
    X_arr[0] = np.ones(len(x_arr_scaled))
    for i in range(1, power + 1):
        X_arr[i] = x_arr_scaled**i
    y_pred_arr_scaled = W @ X_arr
    y_pred_arr = scaler_y.inverse_transform(y_pred_arr_scaled.reshape(-1, 1)).flatten()
    
    sns.scatterplot(x=x, y=y, alpha=0.5, color="blue")
    sns.lineplot(x=x_arr, y=y_pred_arr, color="red")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
