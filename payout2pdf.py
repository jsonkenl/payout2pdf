import datetime
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from database import Database
from data_manager import DataManager

class Payout2PDF:
    def __init__(self):
        self.db = Database()
        self.dm = DataManager()
        self.__create_GUI()        

    def search_command(self):
        self.listbox.delete(0, END)
        for row in self.db.search_payouts(self.owner_text.get(), 
            self.date_text.get()):
                self.listbox.insert(END, 
                    str(row[0]) + "     " + row[11] + "        " + row[5])
   
    def select_file_command(self):
        self.file_path = filedialog.askopenfilename()
        self.file_path_entry.configure(state='normal')
        self.file_path_entry.delete(0, END)
        self.file_path_entry.insert(END, self.file_path)
        self.file_path_entry.configure(state='disabled')

    def upload_command(self):
        payout_data = (
            self.current_date_text.get(),
            self.previous_date_text.get(),
            self.operator_text.get(),
            self.payout_type_text.get(),
            self.add_owner_text.get(),
            self.idc_text.get(),
            self.equipment_text.get(),
            self.loe_text.get(),
            self.wo_text.get(),
            self.mktg_text.get(),
            datetime.datetime.now(),
            self.file_path_text.get()
        )

        file_path = payout_data[-1]
        payout_tuple = payout_data[:-1]
        result = self.dm.create_payout_record(file_path, payout_tuple)

        if result == 'ok':
            self.tab_control.select(self.reports_tab)
            messagebox.showinfo("Upload Status", "File successfully uploaded.")
        else:
            messagebox.showerror(
                    "Upload Status", 
                    "There was an issue uploading your file: " + result
                ) 
   
    def cancel_upload_command(self):
        self.tab_control.select(self.reports_tab)

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

    def __create_GUI(self):
        w = Tk()
        w.wm_title("Payout2PDF")

        # Tab Setup
        self.tab_control = ttk.Notebook(w)
        self.reports_tab = ttk.Frame(self.tab_control)
        self.new_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.reports_tab, text='Reports')
        self.tab_control.add(self.new_tab, text='Create New')
        self.tab_control.pack(expand=1, fill='both')

        # Reports Tab
        self.reports_tab.grid_rowconfigure(0, minsize=10)

        stmt_date_label = Label(
                self.reports_tab, 
                text='Date Created', 
                font=('Arial', 10)
            )
        stmt_date_label.grid(row=1, column=0, padx=5)

        self.reports_tab.grid_rowconfigure(2, minsize=1)

        self.date_text = StringVar()
        self.date_entry = ttk.Entry(
                self.reports_tab, 
                textvariable=self.date_text
            )
        self.date_entry.grid(row=3, column=0, padx=5)

        owner_label = Label(
                self.reports_tab, 
                text='Owner', 
                font=('Arial', 10)
            )
        owner_label.grid(row=1, column=1)

        self.owner_text = StringVar()
        self.owner_entry = ttk.Entry(
                self.reports_tab, 
                textvariable=self.owner_text, 
                width=28
            )
        self.owner_entry.grid(row=3, column=1)

        search_btn = ttk.Button(
                self.reports_tab, 
                text='search', 
                width=14, 
                command=self.search_command
            )
        search_btn.grid(row=3, column=2, padx=5)

        clear_btn = ttk.Button(
                self.reports_tab, 
                text='X', 
                width=3,
                command=self.__view_all_payout_records
            )
        clear_btn.grid(row=3, column=3)

        self.reports_tab.grid_rowconfigure(4, minsize=10)

        self.listbox = Listbox(self.reports_tab, height=25, width=72)
        self.listbox.grid(row=5, column=0, rowspan=6, columnspan=4, padx=5)
        self.listbox.bind('<<ListboxSelect>>', self.__get_selected_row)

        sb = ttk.Scrollbar(self.reports_tab)
        sb.grid(row=5, column=4, rowspan=6)
        self.listbox.configure(yscrollcommand=sb.set)
        sb.configure(command=self.listbox.yview)

        self.reports_tab.grid_columnconfigure(5, minsize=5)
        self.reports_tab.grid_rowconfigure(11, minsize=15)

        delete_btn = ttk.Button(
                self.reports_tab, 
                text='Delete', 
                width=18,
                command=self.delete_command
            )
        delete_btn.grid(row=12, column=0)

        pdf_btn = ttk.Button(self.reports_tab, text='Generate PDF', width=20)
        pdf_btn.grid(row=12, column=1)

        close_btn = ttk.Button(
                self.reports_tab, 
                text='Close', 
                width=18, 
                command=w.destroy
            )
        close_btn.grid(row=12, column=2, columnspan=2)

        self.reports_tab.grid_rowconfigure(13, minsize=10)

        self.__view_all_payout_records()

        # Create New Tab
        self.new_tab.grid_rowconfigure(0, minsize=10)

        current_date_label = Label(
                self.new_tab, 
                text='Current Statement Date (MM/DD/YY)', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        current_date_label.grid(row=1, column=0, columnspan=2, padx=5)

        self.current_date_text = StringVar()
        self.current_date_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.current_date_text
            )
        self.current_date_entry.grid(row=1, column=2, padx=5)

        self.new_tab.grid_rowconfigure(2, minsize=10)

        previous_date_label = Label(
                self.new_tab, 
                text='Previous Statement Date (MM/DD/YY)', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        previous_date_label.grid(row=3, column=0, columnspan=2, padx=5)

        self.previous_date_text = StringVar()
        self.previous_date_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.previous_date_text
            )
        self.previous_date_entry.grid(row=3, column=2, padx=5)

        self.new_tab.grid_rowconfigure(4, minsize=10)

        operator_label = Label(
                self.new_tab, 
                text='Operator', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        operator_label.grid(row=5, column=0, columnspan=2, padx=5)

        self.operator_text = StringVar()
        self.operator_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.operator_text
            )
        self.operator_entry.grid(row=5, column=2, padx=5)

        self.new_tab.grid_rowconfigure(6, minsize=10)

        payout_type_label = Label(
                self.new_tab, 
                text='Payout Type', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        payout_type_label.grid(row=7, column=0, columnspan=2, padx=5)

        self.payout_type_text = StringVar()
        self.payout_type_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.payout_type_text
            )
        self.payout_type_entry.grid(row=7, column=2, padx=5)

        self.new_tab.grid_rowconfigure(8, minsize=10)

        add_owner_label = Label(
                self.new_tab, 
                text='Owner', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        add_owner_label.grid(row=9, column=0, columnspan=2, padx=5)

        self.add_owner_text = StringVar()
        self.add_owner_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.add_owner_text
            )
        self.add_owner_entry.grid(row=9, column=2, padx=5)

        self.new_tab.grid_rowconfigure(10, minsize=10)

        idc_label = Label(
                self.new_tab, 
                text='IDC/ICC Penalty', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        idc_label.grid(row=11, column=0, columnspan=2, padx=5)
        idc_percent_label = Label(
                self.new_tab, 
                anchor='w',
                width=10,
                text="%"
            )
        idc_percent_label.grid(row=11, column=3)

        self.idc_text = StringVar()
        self.idc_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.idc_text
            )
        self.idc_entry.grid(row=11, column=2, padx=5)

        self.new_tab.grid_rowconfigure(12, minsize=10)

        equipment_label = Label(
                self.new_tab, 
                text='Equipment Penalty', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        equipment_label.grid(row=13, column=0, columnspan=2, padx=5)
        equipment_percent_label = Label(
                self.new_tab, 
                anchor='w',
                width=10,
                text="%"
            )
        equipment_percent_label.grid(row=13, column=3)

        self.equipment_text = StringVar()
        self.equipment_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.equipment_text
            )
        self.equipment_entry.grid(row=13, column=2, padx=5)
    
        self.new_tab.grid_rowconfigure(14, minsize=10)

        loe_label = Label(
                self.new_tab, 
                text='LOE Penalty', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        loe_label.grid(row=15, column=0, columnspan=2, padx=5)
        loe_percent_label = Label(
                self.new_tab, 
                anchor='w',
                width=10,
                text="%"
            )
        loe_percent_label.grid(row=15, column=3)

        self.loe_text = StringVar()
        self.loe_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.loe_text
            )
        self.loe_entry.grid(row=15, column=2, padx=5)
        
        self.new_tab.grid_rowconfigure(16, minsize=10)

        wo_label = Label(
                self.new_tab, 
                text='Workover Penalty', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        wo_label.grid(row=17, column=0, columnspan=2, padx=5)
        wo_percent_label = Label(
                self.new_tab, 
                anchor='w',
                width=10,
                text="%"
            )
        wo_percent_label.grid(row=17, column=3)

        self.wo_text = StringVar()
        self.wo_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.wo_text
            )
        self.wo_entry.grid(row=17, column=2, padx=5)
        
        self.new_tab.grid_rowconfigure(18, minsize=10)

        mktg_label = Label(
                self.new_tab, 
                text='Marketing Penalty', 
                width=28,
                anchor='w',
                font=('Arial', 10)
            )
        mktg_label.grid(row=19, column=0, columnspan=2, padx=5)
        mktg_percent_label = Label(
                self.new_tab, 
                anchor='w',
                width=10,
                text="%"
            )
        mktg_percent_label.grid(row=19, column=3)

        self.mktg_text = StringVar()
        self.mktg_entry = ttk.Entry(
                self.new_tab, 
                textvariable=self.mktg_text
            )
        self.mktg_entry.grid(row=19, column=2, padx=5)
        
        self.new_tab.grid_rowconfigure(20, minsize=20)

        file_path_btn = ttk.Button(
                self.new_tab, 
                text=' Select Payout Worksheet ', 
                command=self.select_file_command
            )
        file_path_btn.grid(row=21, column=0, padx=5)

        self.file_path_text = StringVar()
        self.file_path_entry = Entry(
                self.new_tab,
                width=40,
                font=('Arial', 9),
                state='disabled',
                disabledbackground='white',
                textvariable=self.file_path_text
            )
        self.file_path_entry.grid(row=21, column=1, columnspan=3)

        self.new_tab.grid_rowconfigure(22, minsize=120)

        cancel_btn = ttk.Button(
                self.new_tab,
                text=' Cancel ',
                command=self.cancel_upload_command
            )
        cancel_btn.grid(row=23, column=3)

        upload_btn = ttk.Button(
                self.new_tab,
                text=' Upload Payout ',
                command=self.upload_command
            )
        upload_btn.grid(row=23, column=2)
        
        w.mainloop()

p = Payout2PDF()