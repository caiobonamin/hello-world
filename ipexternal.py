#  -*- coding: utf-8 -*-
import os
from urllib.request import urlopen

ext_ip = urlopen("https://api.ipify.org/").read()
print (ext_ip.decode())