import sqlite3
from root_path import db_path


class DatabaseManager:
  def __init__(self, db):
    self.db = db
    
  def connect(self):
    self.conn = sqlite3.connect(self.db)
    self.cursor = self.conn.cursor()

  def query_all(self, table_name):
    self.cursor.execute('''SELECT * from SENSOR_DEFINITIONS''')
    result = self.cursor.fetchall()
    self.commit()
    return result

  def print_query_results(self, result):
    for row in result: 
      print(row)
    
  def insert_entry(self, table, entry):
    self.cursor.execute('''INSERT INTO SENSOR_DEFINITIONS VALUES(?, ?, ?)''', entry) 
    self.commit()

  def commit(self):
    self.conn.commit()

  def close(self):
    self.conn.close()

dm = DatabaseManager(db_path)
dm.connect()
dm.insert_entry("SENSOR_DEFINITIONS",["hexcode-c", "smell", "describes actions through smell"])
result = dm.query_all(["SENSOR_DEFINITIONS"])
dm.print_query_results(result)
dm.close()
