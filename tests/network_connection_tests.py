from nose.tools import *
from models.host import Host
from services.db_connection import * 
import subprocess
import re
import paramiko
import time

db_name = 'hosts'
db_path = './db/' + str(db_name) + '.db'

host = Host('myhost','Linux',{'ip':'192.168.1.14','netmask':'255.255.255.0','gateway':'192.168.1.1'})

def test_host_info():
  host = Host('myhost','Linux',{'ip':'192.168.1.10','netmask':'255.255.255.0','gateway':'192.168.1.1'})
  assert_equal(host.name, "myhost")
  assert_equal(host.os, "Linux")
  assert_equal(host.net_info['ip'], "192.168.1.10")
  assert_equal(host.net_info['netmask'], "255.255.255.0")
  assert_equal(host.net_info['gateway'], "192.168.1.1")

def test_add_host():
  host.add_to_db()
  db_host = db_show(db_name, db_path,'name',host.name)
  assert_equal(db_host[0], host.name)
  assert_equal(db_host[1], host.os)
  assert_equal(db_host[2], host.net_info['ip'])
  assert_equal(db_host[3], host.net_info['netmask'])
  assert_equal(db_host[4], host.net_info['gateway'])

def test_remove_host():
  column = 'name'
  hostname = 'myhost'
  remove_from_db(db_name, db_path,column,hostname)
  db_host = db_show(db_name, db_path,column,host.name)
  assert_equal(db_host, None)

def test_ping():
  ipaddress = host.net_info['ip']
  pattern = 'bytes from ' + str(ipaddress)

  output = subprocess.check_output(["ping", "-c", "2","-W","2",ipaddress])
  match = re.search(pattern, output)

  assert_equal(match.group(0), pattern)
  
def test_ssh_connection():
  ipaddress = host.net_info['ip']
  pattern= 'Last login'
  connection = paramiko.SSHClient() 
  connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  connection.connect(ipaddress, username='root', password='mipase77')
  s = connection.invoke_shell()
  s.send("uptime\n")
  time.sleep(3)
  output = s.recv(5000)
  
  match = re.search(pattern, output)
  assert_equal(match.group(0), pattern)
