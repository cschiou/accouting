import tkinter as tk
from tkinter import filedialog as fd
from ahorro_csv import read_csv
from output_csv import output_csv
from Account_ds import Account


class GUI:
    def select_file(self, entry_text, read=True):
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

    def import_csv(self, file_name, account, write_button):
        read_csv(file_name, account)
        write_button['state'] = tk.NORMAL

    def start_gui(self):
        account = Account()
        window = tk.Tk()
        window.title('Home Accounting')
        window.geometry("400x100+250+150")

        label = tk.Label(window, text='Ahorro csv file: ')
        label.grid(row=0, column=0)
        entry_text = tk.StringVar()
        entry1 = tk.Entry(window, textvariable=entry_text, width=20)
        entry1.grid(row=0, column=1)
        button_browse = tk.Button(window, text='Browse', command=lambda: self.select_file(entry_text))
        button_browse.grid(row=0, column=2)
        button_read = tk.Button(window, text='Load',
                                command=lambda: self.import_csv(entry1.get(), account, button_write))
        button_write = tk.Button(window, text='Write', command=lambda: output_csv(entry2.get(), account),
                                 state=tk.DISABLED)
        button_read.grid(row=0, column=3)

        label = tk.Label(window, text='Output csv file: ')
        label.grid(row=1, column=0)
        entry_text2 = tk.StringVar()
        entry2 = tk.Entry(window, textvariable=entry_text2, width=20)
        entry2.grid(row=1, column=1)
        button_browse2 = tk.Button(window, text='Browse', command=lambda: self.select_file(entry_text2, False))
        button_browse2.grid(row=1, column=2)

        button_write.grid(row=1, column=3)

        window.mainloop()


