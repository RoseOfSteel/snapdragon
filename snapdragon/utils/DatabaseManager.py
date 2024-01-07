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
  Get the sensor commands to needed describe an object.

  name(str): The object to search for.
  sensor_type(str): The type of sensor action (e.g., smell or touch).
  return: List with the object name and definition.
  """
  def query_sensor_data(self, name, sensor_type):
    self.cursor.execute('''SELECT code FROM sensor_definitions WHERE name = (?) AND type = (?)''', [name, sensor_type])
    result = self.cursor.fetchall()
    self.commit()
    return result

  """
  Retrieve the instructions to deliver a particular product.

  name(str): Name of the object you need instructions for.
  software(bool): True if you want the software deliverable instructions. False if not.
  hardware(bool): True if you want the hardware deliverable instructions. False if not.
  documentation(bool): True if you want the documentation deliverable instructions. False if not.
  
  return: List with the delivery instructions.
  """
  def query_delivery_instructions(self, name, software, hardware, documentation):
    
    # TODO: Is there a smarter way to do this query if some of the deliverable types are False or if they're all True?
    # Is it better to do one search to see if the item is there and then do a second query if it is?

    # Keep track of the retrieved instructions
    instructions = []

    if software:
      self.cursor.execute('''SELECT software FROM delivery_definitions WHERE name = (?)''', [name])
      result = self.cursor.fetchall()
      instructions.append(self.clean_query_result(result))

    if hardware:
      self.cursor.execute('''SELECT hardware FROM delivery_definitions WHERE name = (?)''', [name])
      result = self.cursor.fetchall()
      instructions.append(self.clean_query_result(result))

    if documentation:
      self.cursor.execute('''SELECT documentation FROM delivery_definitions WHERE name = (?)''', [name])
      result = self.cursor.fetchall()
      instructions.append(self.clean_query_result(result))
      
    self.commit()
    return self.remove_nested_lists(instructions)

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

  return: List of query results. Returns the empty list if nothing is there.
  """
  def clean_query_result(self, result):

    # Only clean up the result assuming there is something there
    if len(result) == 0:
      return result
            
    # Remove the original list
    result = result[0]

    # Iterate over the tuple and put the results in a fresh list
    fresh_list = []
    for item in result:
      fresh_list.append(item)

    return fresh_list

  """
  Remove nested lists and put them into one list.

  result: List of lists that needs to be cleaned.
  
  return: List of query results. Returns the empty list if nothing is there.
  """
  def remove_nested_lists(self, result):
    fresh_list = []

    for item in result:
      if len(item) > 0:
        fresh_list.append(item[0])
      
    return fresh_list
   
# Test the database
dm = DatabaseManager(db_path)
dm.connect()
dm.insert_entry_sensor_definition(["hexcode-c", "smell", "describes actions through smell"])
result = dm.query_all_sensor_definitions()
dm.print_query_results(result)
dm.close()
print("Database test complete.")

