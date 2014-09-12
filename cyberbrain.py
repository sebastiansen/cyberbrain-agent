#!/usr/bin/env python

# Add this line to your .bashrc
# PROMPT_COMMAND='/path/to/cyberbrain.py $(history | tail -1 | cut -c 8-)'

import sys
import httplib
import platform
import json
import socket

_platform = platform.system().lower()
os = ""

if _platform == "linux" or _platform == "linux2":
    os = "linux"
elif _platform == "darwin":
    os = "osx"
elif _platform == "win32" or _platform == "cygwin":
    os = "windows"

params = json.dumps({
    "cmd": " ".join(sys.argv[1:len(sys.argv)]),
    "metadata": {
        "os": {
            "name": os,
            "version": platform.release(),
        },
        "hostname": socket.gethostname()
    }
})

headers = {"Content-type": "application/json", "Accept": "application/json"}
conn = httplib.HTTPConnection("testpage.biz:3000")

conn.request("POST", "/commands", params, headers)
response = conn.getresponse()

conn.close()