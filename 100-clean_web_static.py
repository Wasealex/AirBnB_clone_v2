#!/usr/bin/python3
""" script that Delete all unnecessary archives
 (all archives minus the number to keep) in the versions folder
 Delete all unnecessary archives
 (all archives minus the number to keep) in the /data/web_static/releases
"""
from fabric.api import *


env.hosts = ['54.237.13.137', '54.87.235.212']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 0:
        return
    elif number == 0 or number == 1:
        number = 1
    else:
        number += 1

    with lcd("versions"):
        local("ls -1t | tail -n +{} | xargs -I {{}} rm -- {{}}".format(number))

    with cd("/data/web_static/releases"):
        run("ls -1t | tail -n +{} | xargs -I {{}} rm -rf -- {{}}".format(
            number))
