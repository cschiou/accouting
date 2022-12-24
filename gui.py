import tkinter as tk
from tkinter.ttk import Notebook
from tkinter import filedialog as fd
from ahorro_csv import read_csv
from output_csv import output_csv
from Account_ds import Account
from plt import plot_stack_plots


def select_file(entry_text, read=True):
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    if read:
        func = fd.askopenfilename
    else:
        func = fd.asksaveasfilename
    entry_text.set(func(
        title='Select a file',
        initialdir='/',
        filetypes=filetypes))


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Home Accounting')
        self.geometry("700x600+250+150")

        self.notebook = Notebook(self)
        # self.notebook.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.notebook.grid(row=2, column=0, columnspan=7)
        self.notebook_page_1_tab = tk.Frame(self.notebook)
        self.init_notebook_page_1()

        self.account = Account()
        self.load_write_button()

    def init_notebook_page_1(self):
        self.notebook.add(self.notebook_page_1_tab, text="Trend")

    def load_data(self, file_name, write_button):
        read_csv(file_name, self.account)
        self.account.build_date_to_account_value()
        write_button['state'] = tk.NORMAL
        plot_stack_plots(self.notebook_page_1_tab, self.account)

    def load_write_button(self):
        label = tk.Label(self, text='Ahorro csv file: ')
        label.grid(row=0, column=0)
        entry_text = tk.StringVar()
        entry1 = tk.Entry(self, textvariable=entry_text, width=60)
        entry1.grid(row=0, column=1, columnspan=4)
        button_browse = tk.Button(self, text='Browse', command=lambda: select_file(entry_text))
        button_browse.grid(row=0, column=5)
        button_read = tk.Button(self, text='Load',
                                command=lambda: self.load_data(entry1.get(), button_write))
        button_write = tk.Button(self, text='Write', command=lambda: output_csv(entry2.get(), self.account),
                                 state=tk.DISABLED)
        button_read.grid(row=0, column=6)

        label = tk.Label(self, text='Output csv file: ')
        label.grid(row=1, column=0)
        entry_text2 = tk.StringVar()
        entry2 = tk.Entry(self, textvariable=entry_text2, width=60)
        entry2.grid(row=1, column=1, columnspan=4)
        button_browse2 = tk.Button(self, text='Browse', command=lambda: select_file(entry_text2, False))
        button_browse2.grid(row=1, column=5)

        button_write.grid(row=1, column=6)




