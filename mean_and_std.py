import numpy as np
import pandas as pd


def mean_and_std(r=6, labels=["L(cm)", "D(cm)", "T(s)"]):
    q1 = "Input the number of repetitions here as an integer\n"
    r = int(input(q1))
    q2 = "Input the quatities measured here as a list of string(e.g.['L(cm)', 'D(cm)', 'T(s)'])\n"
    labels = eval(input(q2))
    c = len(labels)
    df = df = pd.DataFrame(np.zeros((r, c)))
    df.columns = labels
    df.index += 1
    for i in range(r):
        for j in range(c):
            q3 = (
                "Input the value of "
                + labels[j]
                + " for repetition "
                + str(i + 1)
                + "\n"
            )
            df.iloc[i, j] = float(input(q3))
    df.loc["mean"] = df.mean(axis=0)
    df.loc["std"] = df.std(axis=0) # std in pandas is unbiased
    df.loc["uncertainty"] = df.drop(["mean", "std"], axis=0).std(axis=0) / np.sqrt(r)
    print("Processed dataframe is:")
    print(df)