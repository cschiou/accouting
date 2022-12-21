import tkinter as tk
from tkinter import filedialog as fd
from ahorro_csv import read_csv
from output_csv import output_csv
from Account_ds import Account


def select_file(entry_text):
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    entry_text.set(fd.askopenfilename(
        title='Select a file',
        initialdir='/',
        filetypes=filetypes))


def start_gui():
    account = Account()
    window = tk.Tk()
    window.title('Home Accounting')
    window.geometry("300x100+250+150")

    label = tk.Label(window, text='Ahorro csv file: ')
    label.grid(row=0, column=0)
    entry_text = tk.StringVar()
    entry1 = tk.Entry(window, textvariable=entry_text, width=20)
    entry1.grid(row=0, column=1)
    button_browse = tk.Button(window, text='Browse', command=lambda: select_file(entry_text))
    button_browse.grid(row=0, column=2)

    button_read = tk.Button(window, text='Load csv', command=lambda: read_csv(entry1.get(), account))
    button_read.grid(row=1, column=0)

    label = tk.Label(window, text='Output csv file: ')
    label.grid(row=2, column=0)
    entry2 = tk.Entry(window, width=20)
    entry2.grid(row=2, column=1)
    button_write = tk.Button(window, text='Write', command=lambda: output_csv(entry2.get(), account))
    button_write.grid(row=2, column=2)

    window.mainloop()
