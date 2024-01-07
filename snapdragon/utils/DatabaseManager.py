import sqlite3
from root_path import db_path

"""
This class is used to manage interactions with the Snapdragon database.
"""
class DatabaseManager:
  """
  Constructor.

  db(str): Database file with path.
  """
  def __init__(self, db):
    self.db = db

  """
  Connect to the database and create a cursor for interactions.
  """
  def connect(self):
    self.conn = sqlite3.connect(self.db)
    self.cursor = self.conn.cursor()

  """
  Print results of a query.

  result(list): List with results from a previously executed query.
  """
  def print_query_results(self, result):
    for row in result: 
      print(row)

  """
  Query all data from the sensor_definition table.

  return: list of tuples with each sensory database entry.
  """
  def query_all_sensor_definitions(self):
    self.cursor.execute('''SELECT * from SENSOR_DEFINITIONS''')
    result = self.cursor.fetchall()
    self.commit()
    return result

  """
  Add a new sensor.

  entry(list): Values for the new sensor.
  """
  def insert_entry_sensor_definition(self, entry):
    try:
      self.cursor.execute('''INSERT INTO SENSOR_DEFINITIONS VALUES(?, ?, ?)''', entry) 
      self.commit()
    except sqlite3.IntegrityError:
      print("This sensor already exists.")

  """
  Commit the changes to the datasbase.
  """
  def commit(self):
    self.conn.commit()

  """
  Close the connection with the database.
  """
  def close(self):
    self.conn.close()

"""
# Test the database
dm = DatabaseManager(db_path)
dm.connect()
dm.insert_entry_sensor_definition(["hexcode-c", "smell", "describes actions through smell"])
result = dm.query_all_sensor_definitions()
dm.print_query_results(result)
dm.close()
print("Database test complete.")
"""
