#!/usr/bin/env python3

import cgi
import subprocess
import json
from os import environ
from http.cookies import SimpleCookie

PATH_TO_MACHINE = "./etovucca"
PATH_TO_SQLITE = "./sqlite3"
PATH_TO_DB = "rtbb.sqlite3"
# PATH_TO_PASSWD = "./machine_passwd"


print("Content-Type: text/html")
print("Cache-Control: no-store, must-revalidate")
print()
print('<link rel="stylesheet" href="https://spar.isi.jhu.edu/teaching/443/main.css">')
print('<h2 id="dlobeid-etovucca-voting-machine">DLOBEID EtovUcca Voting Machine</h2>')
print('<h1 id="candidate">Candidate Interface</h1>')
form = cgi.FieldStorage()


print("<hr>")
print("<h3>[Candidate name]</h3>")
print("<form>")
print('<label for="intro">Introduction</label><br>')
print(
    '<input type="text" id="intro" name="intro" style="width: 500px; height:200px;"><br>'
)
print('<input type="submit" value="Save">')
print("</form>")
