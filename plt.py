# import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Account_ds import Account
import tkinter as tk
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


def plot_stack_plots(root: tk.Frame, account: Account):
    date = account.get_date_list()

    fig, ax = plt.subplots()
    bar1 = FigureCanvasTkAgg(fig, root)
    bar1.get_tk_widget().grid(row=0)
    ax.stackplot(date, account.get_account_to_date_value_map().values(),
                 labels=account.get_account_to_date_value_map().keys(), alpha=0.8)
    ax.legend(loc='upper left')
    ax.set_title('Assets trend')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value (TWD)')

    # plt.show()
