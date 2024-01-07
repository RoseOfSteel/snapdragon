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
  Find information on an object based on the haar cascade that was used to identify the image.

  cascade(str): The cascade used to identify the image.
  return: List with the object name and definition.
  """
  def query_identifier(self, cascade):
    self.cursor.execute('''SELECT name, definition FROM identifier_definitions WHERE cascade = (?)''', [cascade])
    result = self.cursor.fetchall()
    self.commit()
    return result

  """
  Find information on an object based on the haar cascade that was used to identify the image.

  cascade(str): The cascade used to identify the image.
  return: List with the object name and definition.
  """
  def query_sensor_data(self, name, sensor_type):
    self.cursor.execute('''SELECT code FROM sensor_definitions WHERE name = (?) AND type = (?)''', [name, sensor_type])
    result = self.cursor.fetchall()
    self.commit()
    return result

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
  Clean the query result (remove from the nested tuple in a list and put in a straight list).
  Ex: [('[(1,3,2,20)]',)] > [[(1,3,2,20)]]

  result(list): List with a tuple that contains the query results.

  return: A plain list with the query results.
  """
  def clean_query_result(self, result):
    # Remove the original list
    result = result[0]

    # Iterate over the tuple and put the results in a fresh list
    fresh_list = []
    for item in result:
      fresh_list.append(item)

    return fresh_list
    
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
