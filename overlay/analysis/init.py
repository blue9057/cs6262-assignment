#!/usr/bin/env python

import os

print("Type your GT login ID")
gtid = raw_input()

os.system("wget https://ironhide.gtisc.gatech.edu/id/download.php?gtid=%s -O ~/shared/complex.exe --no-check-certificate" % gtid)
