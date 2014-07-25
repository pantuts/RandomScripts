#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Dependecy: notify2
# sudo pip install notify2
# for cron run: crontab -e
# then add this
# */1 * * * * export DISPLAY=:0.0 && /home/username/path/to/script.py > /dev/null
# This cron job will run every minute
 
import notify2
import shlex
from subprocess import Popen, PIPE
 
upower = shlex.split('upower -i /org/freedesktop/UPower/devices/battery_BAT0')
grp = shlex.split('grep percentage')
ak = shlex.split("awk -F '[^0-9]*' '$0=$2'")
 
proc1 = Popen(upower, stdout=PIPE)
proc2 = Popen(grp, stdin=proc1.stdout, stdout=PIPE)
proc3 = Popen(ak, stdin=proc2.stdout, stdout=PIPE)
proc1.stdout.close()
out = int(proc3.communicate()[0].decode('ascii').rstrip())
# print(out)
 
notify2.init('bat_check')
 
# edit this
# if battery is less than 15%
if out < 15:
    note = notify2.Notification('Battery Check', 'CHARGE CHARGE CHARGE CHARGE CHARGE')
    note.set_category('device')
    note.set_timeout(5000)
    note.show()
