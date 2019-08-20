from tkinter import *
from tkinter import ttk
from database import Database

class Payout2PDF:
    def __init__(self):
        self.db = Database()
        w = Tk()
        w.wm_title("Payout2PDF")

        # Tab Setup
        tab_control = ttk.Notebook(w)
        reports_tab = ttk.Frame(tab_control)
        new_tab = ttk.Frame(tab_control)
        tab_control.add(reports_tab, text='Reports')
        tab_control.add(new_tab, text='Create New')
        tab_control.pack(expand=1, fill='both')

        # Reports Tab
        reports_tab.grid_rowconfigure(0, minsize=10)

        stmt_date_label = Label(reports_tab, text='Date Created', 
            font=('Arial', 10))
        stmt_date_label.grid(row=1, column=0, padx=5)

        reports_tab.grid_rowconfigure(2, minsize=1)

        self.date_text = StringVar()
        self.date_entry = ttk.Entry(reports_tab, textvariable=self.date_text)
        self.date_entry.grid(row=3, column=0, padx=5)

        owner_label = Label(reports_tab, text='Owner', 
            font=('Arial', 10))
        owner_label.grid(row=1, column=1)

        self.owner_text = StringVar()
        self.owner_entry = ttk.Entry(reports_tab, textvariable=self.owner_text, 
            width=28)
        self.owner_entry.grid(row=3, column=1)

        search_btn = ttk.Button(reports_tab, text='search', width=14, 
            command=self.search_command)
        search_btn.grid(row=3, column=2, padx=5)

        clear_btn = ttk.Button(reports_tab, text='X', width=3,
            command=self.__view_all_payout_records)
        clear_btn.grid(row=3, column=3)

        reports_tab.grid_rowconfigure(4, minsize=10)

        self.listbox = Listbox(reports_tab, height=25, width=72)
        self.listbox.grid(row=5, column=0, rowspan=6, columnspan=4, padx=5)
        self.listbox.bind('<<ListboxSelect>>', self.__get_selected_row)

        sb = ttk.Scrollbar(reports_tab)
        sb.grid(row=5, column=4, rowspan=6)
        self.listbox.configure(yscrollcommand=sb.set)
        sb.configure(command=self.listbox.yview)

        reports_tab.grid_columnconfigure(5, minsize=10)
        reports_tab.grid_rowconfigure(11, minsize=15)

        delete_btn = ttk.Button(reports_tab, text='Delete', width=18,
            command=self.delete_command)
        delete_btn.grid(row=12, column=0)

        pdf_btn = ttk.Button(reports_tab, text='Generate PDF', width=20)
        pdf_btn.grid(row=12, column=1)

        close_btn = ttk.Button(reports_tab, text='Close', width=18, 
            command=w.destroy)
        close_btn.grid(row=12, column=2, columnspan=2)

        reports_tab.grid_rowconfigure(13, minsize=10)

        # Create New Tab
        

        self.__view_all_payout_records()
        w.mainloop()

    def search_command(self):
        self.listbox.delete(0, END)
        for row in self.db.search_payouts(self.owner_text.get(), 
            self.date_text.get()):
                self.listbox.insert(END, 
                    str(row[0]) + "     " + row[11] + "        " + row[5])
   
    def delete_command(self):
        self.db.delete(self.selected_tuple[0])
        self.__view_all_payout_records()

    def __get_selected_row(self, event):
        try:
            index = self.listbox.curselection()[0]
            self.selected_tuple = self.listbox.get(index)
            print(self.selected_tuple[0])
        except IndexError:
            pass

    def __view_all_payout_records(self):
        self.listbox.delete(0, END)
        for row in self.db.view_all():
            self.listbox.insert(END, 
                str(row[0]) + "     " + row[11] + "        " + row[5])


p = Payout2PDF()