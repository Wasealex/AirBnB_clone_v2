#!/usr/bin/python3
"""script that deploys to webserver
"""
from fabric.api import *
from datetime import datetime
import os


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Uploads the archive to the /tmp/ directory of the web servers.
    Uncompresses the archive to the folder /data/web_static/releases/<archive
    filename without extension> on the web servers.
    Deletes the archive from the web servers.
    Deletes the symbolic link /data/web_static/current from the web servers.
    Creates a new symbolic link /data/web_static/current on the web servers,
    linked to the new version of the code.
    Returns True if all operations have been done correctly,
    otherwise returns False.
    """
    if os.path.exists(archive_path) is False:
        return False

    try:
        #archive_path='versions/web_statics_{datetime.now}.tgz'
        put(archive_path, '/tmp/')

        archivename = archive_path.split('/')[-1]
        d_name = archivename.split('.')[0]
        d_path= '/data/web_static/releases/'
        archivefolder = f'{d_path}{d_name}'
        run('mkdir -p {}'.format(archivefolder))
        run('tar -xzf /tmp/{} -C {}'.format(archivename, archivefolder))
        run('rm /tmp/{}'.format(archivename))

        run('mv {}/web_static/* {}'.format(archivefolder, archivefolder))
        run('rm -rf {}/web_static'.format(archivefolder))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(archivefolder))

        return True
    except Exception as e:
        return False
