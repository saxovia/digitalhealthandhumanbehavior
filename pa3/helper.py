import numpy as np
import pandas as pd
from functools import wraps
import seaborn as sns


# define the x-axis
x_axis = np.arange(0, 24, 1)


def bin_counter_validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            raise ValueError("no more than 1 parameter")

        return func(*args, **kwargs)

    return wrapper


def plot_subject_vs_average(data, ax, average):

    sns.lineplot(ax=ax, data=data, label="subject", linewidth=5)
    sns.lineplot(ax=ax, data=average, label="average", linewidth=5, linestyle="--")
    ax.fill_between(
        x_axis, data, average, alpha=0.3, where=(data >= average), interpolate=True
    )
    ax.fill_between(
        x_axis, data, average, alpha=0.3, where=(data < average), interpolate=True
    )
    # ax.fill_between(np.where(data<0)[0], data, np.zeros(shape=data.shape[1]), color="grey", alpha=0.3)

    ax.axvline(x=6, color="green", linewidth=2, alpha=0.5, linestyle="--")
    ax.axvline(x=8, color="green", linewidth=2, alpha=0.5, linestyle="--")
    
    ax.axvline(x=21, color="black", linewidth=2, alpha=0.5, linestyle="--")
    ax.axvline(x=23, color="black", linewidth=2, alpha=0.5, linestyle="--")
    ax.set_xticks(x_axis[0::2])
    # ax.xaxis.set_tick_params(rotation=60)
    ax.set_yticks([])
    ax.set_xlabel("Hours", labelpad=4)
    
