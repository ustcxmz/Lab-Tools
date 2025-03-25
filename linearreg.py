import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def linear_red(
    x=[8.214, 7.408, 6.879, 5.490, 5.196],
    y=[1.610, 1.270, 1.062, 0.478, 0.358],
    xlabel="v(10^14Hz)",
    ylabel="U(V)",
    title="U vs v",
    text_position_x=0,
    text_position_y=0.87,
):
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


# Input x values here as a list
# Input y values here as a list
# Input x label here as a string
# Input y label here as a string
# Input title here as a string
# Input x position of text here as a float in range [0, 1]
# Input y position of text here as a float in range [0, 1]
# 0 means in the left/bottom, 1 means in the right/top
