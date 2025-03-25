import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def linear_reg(
    x=[8.214, 7.408, 6.879, 5.490, 5.196],
    y=[1.610, 1.270, 1.062, 0.478, 0.358],
    xlabel="v(10^14Hz)",
    ylabel="U(V)",
    title="U vs v",
    text_position_x=0,
    text_position_y=0.87,
):
    q1 = "Input x values here as a list(e.g. [8.214, 7.408, 6.879, 5.490, 5.196])\n"
    x = eval(input(q1))
    q2 = "Input y values here as a list(e.g. [1.610, 1.270, 1.062, 0.478, 0.358])\n"
    y = eval(input(q2))
    if len(x) != len(y):
        print("Length of x and y must be equal")
        return
    q3 = "Input x label here as a string\n"
    xlabel = input(q3)
    q4 = "Input y label here as a string\n"
    ylabel = input(q4)
    q5 = "Input title here as a string\n"
    title = input(q5)
    q6 = "0 means in the left/bottom while 1 means in the right/top\n"
    q7 = "Input x position of text here as a float in range [0, 1]\n" + q6
    text_position_x = float(input(q7))
    q8 = "Input y position of text here as a float in range [0, 1]\n" + q6
    text_position_y = float(input(q8))
    x = np.array(x)
    y = np.array(y)
    linregress = stats.linregress(x, y)
    slope = linregress.slope
    intercept = linregress.intercept
    r_value = linregress.rvalue
    p_value = linregress.pvalue
    stderr = linregress.stderr
    sns.scatterplot(x=x, y=y)
    sns.lineplot(
        x=[min(x), max(x)],
        y=[slope * min(x) + intercept, slope * max(x) + intercept],
        linestyle="--",
    )
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.text(
        x=text_position_x * min(x) + (1 - text_position_x) * max(x),
        y=text_position_y * min(y) + (1 - text_position_y) * max(y),
        s=f"Regression line: y = {slope:.4f}x + {intercept:.4f}\nr_value = {r_value:.4f}\np_value = {p_value:.4f}\nstderr = {stderr:.4f}",
    )
    plt.show()
