#!/usr/bin/env python3

import cgi
import subprocess
import json
from os import environ
from http.cookies import SimpleCookie
import hashlib

PATH_TO_MACHINE = "./etovucca"
PATH_TO_SQLITE = "./sqlite3"
PATH_TO_DB = "rtbb.sqlite3"
#PATH_TO_PASSWD = "./machine_passwd"
redirectURL = "./candidate.cgi"

def candidate_login(failure=False, logout=False):
    print("Content-Type: text/html")
    if logout:
        print("Set-Cookie: user=LOGGEDOUT; expires=Thu, 01 Jan 1970 00:00:00 GMT")
    print()
    print('<link rel="stylesheet" href="https://spar.isi.jhu.edu/teaching/443/main.css">')
    print('<h2 id="dlobeid-etovucca-voting-machine">DLOBEID EtovUcca Voting Machine</h2>')
    print('<h1 id="cand-interface-login">Candidate Interface Login</h1><br>')
    if failure:
        print('<b>Login Failed.</b>')
    print('<form method="post">')
    print('<label for="usrname">User Name:</label>')
    print('<input type="username" id="usrname" name="usrname"><br><br>')
    print('<label for="passwd">Candidate Password:</label>')
    print('<input type="password" id="passwd" name="passwd"><br><br>')
    print('<input type="submit" value="Login">')
    print('</form>')
    print("<a href='./home.cgi'>Return to Homepage</a>")

form = cgi.FieldStorage()

try:
    #if 'usrname' in form:
    	# need usrname storage
    	
    	
    if 'passwd' in form:
    	
    	subprocess.check_output([PATH_TO_MACHINE, 'passwd', form.getvalue('office'), form.getvalue('passwd')])
    	
    	
    	
        # Please don't ever actually do this.
        h = hashlib.new('md5')  # U+1F914
        h.update(form.getvalue('passwd').encode('utf-8'))
        with open(PATH_TO_PASSWD) as f:
            stored_hash = f.read(32)
            if h.hexdigest() == stored_hash:
                # CGI Redirect: https://stackoverflow.com/a/6123179
                print('Content-Type: text/html')
                print('Location: %s' % redirectURL)
                C = SimpleCookie()
                C['user'] = h.hexdigest() # U+1F914
                print(C)
                print('')
                print('<html>')
                print('<head>')
                print('<link rel="stylesheet" href="https://spar.isi.jhu.edu/teaching/443/main.css">')
                print('<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL)
                print('<title>You are going to be redirected</title>')
                print('</head>')
                print('<body>')
                print('Redirecting... <a href="%s">Click here if you are not redirected</a>' % redirectURL)
                print('</body>')
                print('</html>')
            else:
                raise ValueError('incorrect hash')
    elif 'logout' in form:
        candidate_login(logout=True)
    else:
        candidate_login()
except Exception:
    candidate_login(failure=True)
    

