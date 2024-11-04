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
# PATH_TO_PASSWD = "./machine_passwd"
redirectURL = "./candidate.cgi"


def candidate_login(failure=False, logout=False):
    print("Content-Type: text/html")
    if logout:
        print("Set-Cookie: user=LOGGEDOUT; expires=Thu, 01 Jan 1970 00:00:00 GMT")
    print()
    print(
        '<link rel="stylesheet" href="https://spar.isi.jhu.edu/teaching/443/main.css">'
    )
    print(
        '<h2 id="dlobeid-etovucca-voting-machine">DLOBEID EtovUcca Voting Machine</h2>'
    )
    print('<h1 id="cand-interface-login">Candidate Interface Login</h1><br>')
    if failure:
        print("<b>Login Failed.</b>")
    print('<form method="post">')
    print('<label for="usrname">User Name:</label>')
    print('<input type="username" id="usrname" name="usrname"><br><br>')
    print('<label for="passwd">Candidate Password:</label>')
    print('<input type="password" id="passwd" name="passwd"><br><br>')
    print('<input type="submit" value="Login">')
    print("</form>")
    print("<a href='./home.cgi'>Return to Homepage</a>")


form = cgi.FieldStorage()

try:

    json_candidate = subprocess.check_output([PATH_TO_MACHINE, "get-candidate"]).decode(
        "utf-8"
    )
    candidates = json.loads(json_candidate)

    if len(form) != 0:
        ids = form.getvalue("candidate").split("_")
        unqiue_candidate_id = str(candidates[int(ids[0])]["id"])
        subprocess.check_output(
            [PATH_TO_MACHINE, "get-candidate", form.getvalue("id"), unqiue_candidate_id]
        )
        # subprocess.check_output([PATH_TO_MACHINE, 'get-candidate', form.getvalue('password'), 'passwd'])

        print("<ul>")

    if "passwd" in form:

        subprocess.check_output(
            [PATH_TO_MACHINE, "get-candidate", form.getvalue("password"), "passwd"]
        )
        print("<b>Sucessfully login.</b>")
        print("Content-Type: text/html")
        print("Location: %s" % redirectURL)
        # CGI Redirect: https://stackoverflow.com/a/6123179%s' % redirectURL)
        C = SimpleCookie()
        C["user"] = h.hexdigest()  # U+1F914
        print(C)
        print("")
        print("<html>")
        print("<head>")
        print(
            '<link rel="stylesheet" href="https://spar.isi.jhu.edu/teaching/443/main.css">'
        )
        print('<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL)
        print("<title>You are going to be redirected</title>")
        print("</head>")
        print("<body>")
        print(
            'Redirecting... <a href="%s">Click here if you are not redirected</a>'
            % redirectURL
        )
        print("</body>")
        print("</html>")

    elif "logout" in form:
        candidate_login(logout=True)
    else:
        candidate_login()
except Exception:
    candidate_login(failure=True)
