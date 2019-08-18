import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = self.__create_conn(db_file)
        if self.conn is not None:
            self.c = self.conn.cursor()
            self.__create_table(self.c, self.__payout_table())
            self.__create_table(self.c, self.__well_data_table())
            self.conn.commit()
        else:
            print("Error! Cannot connect to the database.")

    def __create_conn(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Exception as e:
            print(e)
        return None

    def __create_table(self, c, create_table_statement):
        try:
            c.execute(create_table_statement)
        except Exception as e:
            print(e)

    def __payout_table(self):
        return ("CREATE TABLE IF NOT EXISTS payouts ("
                    "id INTEGER PRIMARY KEY, "
                    "current_stmt_date TEXT, "
                    "prior_stmt_date TEXT, "
                    "operator TEXT, "
                    "type TEXT, "
                    "owner TEXT, "
                    "idc REAL, "
                    "equip REAL, " 
                    "loe REAL, "
                    "wo REAL, "
                    "mkt REAL, "
                    "timestamp TEXT NOT NULL)")

    def __well_data_table(self):
        return ("CREATE TABLE IF NOT EXISTS wells ("
                        "id INTEGER PRIMARY KEY, "
                        "name TEXT, "
                        "well_id INTEGER, "
                        "api TEXT, "
                        "beg_gas_vol REAL, "
                        "pd_gas_vol REAL, "
                        "end_gas_vol REAL, "
                        "beg_cond_vol REAL, "
                        "pd_cond_vol REAL, "
                        "end_cond_vol REAL, "
                        "beg_ngl_vol REAL, "
                        "pd_ngl_vol REAL, "
                        "end_ngl_vol REAL, "
                        "beg_gas_rev REAL, "
                        "pd_gas_rev REAL, "
                        "end_gas_rev REAL, "
                        "beg_cond_rev REAL, "
                        "pd_cond_rev REAL, "
                        "end_cond_rev REAL, "
                        "beg_ngl_rev REAL, "
                        "pd_ngl_rev REAL, "
                        "end_ngl_rev REAL, "
                        "beg_rev_total REAL, "
                        "pd_rev_total REAL, "
                        "end_rev_total REAL, "
                        "beg_royalty REAL, "
                        "pd_royalty REAL, "
                        "end_royalty REAL, "
                        "beg_tax REAL, "
                        "pd_tax REAL, "
                        "end_tax REAL, "
                        "beg_net_rev REAL, "
                        "pd_net_rev REAL, "
                        "end_net_rev REAL, "
                        "beg_idc_icc REAL, "
                        "pd_idc_icc REAL, "
                        "end_idc_icc REAL, "
                        "beg_equip REAL, "
                        "pd_equip REAL, "
                        "end_equip REAL, "
                        "beg_loe REAL, "
                        "pd_loe REAL, "
                        "end_loe REAL, "
                        "beg_wo REAL, "
                        "pd_wo REAL, "
                        "end_wo REAL, "
                        "beg_mkt REAL, "
                        "pd_mkt REAL, "
                        "end_mkt REAL, "
                        "beg_exp_total REAL, "
                        "pd_exp_total REAL, "
                        "end_exp_total REAL, "
                        "payout REAL, "
                        "payout_id INTEGER NOT NULL, "
                        "timestamp TEXT NOT NULL, "
                        "FOREIGN KEY (payout_id) REFERENCES payouts (id))")

db = Database("payouts.db")