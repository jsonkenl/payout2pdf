import pandas
import datetime
from xlrd import XLRDError
from database import Database

class DataManager:
    def __init__(self):
        self.db = Database()

    def create_payout_record(self, file_path, payout_data):
        try: 
            payout_id = self.db.insert_payout(payout_data)
            self.__import_file_to_db(file_path, payout_id)
            return 'ok'
        except:
            return 'data_import_error'

    def __import_file_to_db(self, file_path, payout_id):
        try:
            data = pandas.read_excel(file_path, header=None, skiprows=9)

            for _index, row in data.iterrows():
                well_touple = (row[5], row[3], row[4], row[9], row[10], 
                               row[11], row[14], row[15], row[16], row[19],
                               row[20], row[21], row[25], row[26], row[27], 
                               row[30], row[31], row[32], row[35], row[36],
                               row[37], row[39], row[40], row[38], row[44], 
                               row[45], row[46], row[50], row[51], row[52], 
                               row[55], row[56], row[54], row[60], row[61], 
                               row[62], row[66], row[67], row[68], row[76], 
                               row[77], row[78], row[82], row[83], row[84], 
                               row[88], row[89], row[90], row[93], row[94], 
                               row[92], row[96], payout_id, 
                               datetime.datetime.now()) 
                
                self.db.insert_well(well_touple)
                return 'ok'

        except FileNotFoundError:
            return 'FileNotFoundError'
        except XLRDError:
            return 'XLRDError'
        except Exception as e:
            return e