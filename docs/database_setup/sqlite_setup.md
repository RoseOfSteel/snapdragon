# SQLite Setup
This guide explains how to set up a SQLite database on Windows.

## Download and Install SQLite
Tutorial to Download and Install SQLite
https://www.sqlitetutorial.net/download-install-sqlite/

## Download and Install SQLiteStudio for Windows
https://sqlitestudio.pl/


## Create a database using the command line
*Note: Run the initial command from the Windows command line. That will open the SQLite interactive mode. There, you will type the commands to create the table. Once you have done that, exit the interactive mode. You will now see the created table. The database file does not get created as soon as you run that first command. You have to add a table first.*

```
	C:\project>C:\sqlite\sqlite3.exe snapdragon.db
	SQLite version 3.44.2 2023-11-24 11:41:44 (UTF-16 console I/O)
	Enter ".help" for usage hints.
	
	sqlite> create table identifiers(name text, definition text);
	sqlite> insert into identifiers values('building','protection from elements');
	sqlite> select * from identifiers;
	building|protection from elements
	
	sqlite> .exit
```
