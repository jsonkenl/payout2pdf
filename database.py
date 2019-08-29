import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = self.__create_conn('payouts.db')

        if self.conn is not None:
            self.__create_table(self.__payout_table())
            self.__create_table(self.__well_data_table())
        else:
            print("Error! Cannot connect to the database.")
    
    def view_all(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM payouts')
        return c.fetchall()
    
    def insert_payout(self, payout_tuple):
        sql = ''' INSERT INTO payouts(c_stmt_date,p_stmt_date,operator,type,
                  owner,idc,equip,loe,wo,mkt,timestamp)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?) '''

        c = self.conn.cursor()
        c.execute(sql, payout_tuple)
        self.conn.commit()
        return c.lastrowid

    def insert_well(self, well_touple):
        sql = ''' INSERT INTO wells(name,well_id,api,beg_gas_vol,pd_gas_vol,
                  end_gas_vol,beg_cond_vol,pd_cond_vol,end_cond_vol,beg_ngl_vol,
                  pd_ngl_vol,end_ngl_vol,beg_gas_rev,pd_gas_rev,end_gas_rev,
                  beg_cond_rev,pd_cond_rev,end_cond_rev,beg_ngl_rev,pd_ngl_rev,
                  end_ngl_rev,beg_rev_total,pd_rev_total,end_rev_total,
                  beg_royalty,pd_royalty,end_royalty,beg_tax,pd_tax,end_tax,
                  beg_net_rev,pd_net_rev,end_net_rev,beg_idc_icc,pd_idc_icc,
                  end_idc_icc,beg_equip,pd_equip,end_equip,beg_loe,pd_loe,
                  end_loe,beg_wo,pd_wo,end_wo,beg_mkt,pd_mkt,end_mkt,
                  beg_exp_total,pd_exp_total,end_exp_total,payout,payout_id,
                  timestamp)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                  ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

        c = self.conn.cursor()
        c.execute(sql, well_touple)
        self.conn.commit()

    def search_payouts(self, owner="", timestamp=""):
        timestamp = '%'+timestamp+'%' if timestamp != "" else timestamp
        owner = '%'+owner+'%' if owner != "" else owner
        c = self.conn.cursor()
        c.execute('SELECT * FROM payouts WHERE owner LIKE ? OR timestamp LIKE ?', 
            (owner, timestamp))
        return c.fetchall()

    def search_payout(self, id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM payouts WHERE id=?', (id,))
        return c.fetchall()

    def search_wells_by_payout(self, payout_id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM wells WHERE payout_id=?', (payout_id,))
        return c.fetchall()
    
    def delete(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM payouts WHERE id=?', (id,))
        c.execute('DELETE FROM wells WHERE payout_id=?', (id,))
        self.conn.commit()

    def __create_conn(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except:
            return None

    def __create_table(self, create_table_statement):
        c = self.conn.cursor()
        c.execute(create_table_statement)

    def __payout_table(self):
        return ('CREATE TABLE IF NOT EXISTS payouts ('
                    'id INTEGER PRIMARY KEY, '
                    'c_stmt_date TEXT, '
                    'p_stmt_date TEXT, '
                    'operator TEXT, '
                    'type TEXT, '
                    'owner TEXT, '
                    'idc REAL, '
                    'equip REAL, ' 
                    'loe REAL, '
                    'wo REAL, '
                    'mkt REAL, '
                    'timestamp TEXT NOT NULL)')

    def __well_data_table(self):
        return ('CREATE TABLE IF NOT EXISTS wells ('
                        'id INTEGER PRIMARY KEY, '
                        'name TEXT, '
                        'well_id INTEGER, '
                        'api TEXT, '
                        'beg_gas_vol REAL, '
                        'pd_gas_vol REAL, '
                        'end_gas_vol REAL, '
                        'beg_cond_vol REAL, '
                        'pd_cond_vol REAL, '
                        'end_cond_vol REAL, '
                        'beg_ngl_vol REAL, '
                        'pd_ngl_vol REAL, '
                        'end_ngl_vol REAL, '
                        'beg_gas_rev REAL, '
                        'pd_gas_rev REAL, '
                        'end_gas_rev REAL, '
                        'beg_cond_rev REAL, '
                        'pd_cond_rev REAL, '
                        'end_cond_rev REAL, '
                        'beg_ngl_rev REAL, '
                        'pd_ngl_rev REAL, '
                        'end_ngl_rev REAL, '
                        'beg_rev_total REAL, '
                        'pd_rev_total REAL, '
                        'end_rev_total REAL, '
                        'beg_royalty REAL, '
                        'pd_royalty REAL, '
                        'end_royalty REAL, '
                        'beg_tax REAL, '
                        'pd_tax REAL, '
                        'end_tax REAL, '
                        'beg_net_rev REAL, '
                        'pd_net_rev REAL, '
                        'end_net_rev REAL, '
                        'beg_idc_icc REAL, '
                        'pd_idc_icc REAL, '
                        'end_idc_icc REAL, '
                        'beg_equip REAL, '
                        'pd_equip REAL, '
                        'end_equip REAL, '
                        'beg_loe REAL, '
                        'pd_loe REAL, '
                        'end_loe REAL, '
                        'beg_wo REAL, '
                        'pd_wo REAL, '
                        'end_wo REAL, '
                        'beg_mkt REAL, '
                        'pd_mkt REAL, '
                        'end_mkt REAL, '
                        'beg_exp_total REAL, '
                        'pd_exp_total REAL, '
                        'end_exp_total REAL, '
                        'payout REAL, '
                        'payout_id INTEGER NOT NULL, '
                        'timestamp TEXT NOT NULL, '
                        'FOREIGN KEY (payout_id) REFERENCES payouts (id))')
