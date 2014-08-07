import sqlite3 as sql
import os

def db_connect(database):
  db = sql.connect(database)
  return db

def db_create(db_path):
  db = db_connect(db_path)
  db_cursor = db.cursor()
  cmd = 'CREATE TABLE {db_name}(name TEXT,os TEXT,ip TEXT, netmask TEXT, gateway TEXT)'
  #cmd = 'CREATE TABLE ' + str(db_name) + '(name TEXT,os TEXT,ip TEXT, netmask TEXT, gateway TEXT)'
  #cmd = 'CREATE TABLE hosts(name TEXT,os TEXT,ip TEXT, netmask TEXT, gateway TEXT)'
  db_cursor.execute(cmd.format(db_name=db_name))
  db.commit()
  db.close()

def db_show(db_name, db_path, column, value):
  db = db_connect(db_path)
  db_cursor = db.cursor()
  #cmd = 'SELECT * FROM {db_name}' 
  db_cursor.execute('SELECT * FROM {db_name} WHERE {col}="{val}"'.format(db_name=db_name,col=column, val=value))
  row = db_cursor.fetchone()
  db.commit()
  db.close()
  return row 

def remove_from_db(db_name, db_path,column, value):
  db = db_connect(db_path)
  db_cursor = db.cursor()
  cmd = 'DELETE FROM {db} WHERE {col}="{val}"'
  db_cursor.execute(cmd.format(db=db_name,col=column, val=value))
  db.commit()
  db.close()

def print_db_cursor(cursor):
  for x in cursor:
    print x

