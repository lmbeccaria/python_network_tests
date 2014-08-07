import sqlite3 as sql
import os
from services.db_connection import * 

db_name = 'hosts'
db_path = './db/' + str(db_name) + '.db'
if not (os.path.isfile(db_path)):
  db_create(db_path)
  
class Host(object):
  def __init__(self, name, os, net_info={}):
    self.name = name
    self.os = os
    self.net_info = net_info

  def add_to_db(self):
    db = db_connect(db_path)
    db_cursor = db.cursor()
    #check that the entry is not there
    row = db_show(db_name, db_path,'name',self.name)
    if row is not None and str(row).find(str(self.name)):
      return None 
    else:
      cmd = 'INSERT INTO {db}(name,os,ip,netmask,gateway) VALUES(?,?,?,?,?)'
    
      db_cursor.execute(cmd.format(db=db_name), (self.name, self.os, self.net_info['ip'], self.net_info['netmask'], self.net_info['gateway']))
      db.commit()
    db.close()






    

  

