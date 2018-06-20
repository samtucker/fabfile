from fabric.api import *

env.hosts = [
    'pi@192.168.1.10',
    'pi@192.168.1.11',
    'pi@192.168.1.12',
    'pi@192.168.1.13',
    'pi@192.168.1.14',
    'pi@192.168.1.16',
    'pi@192.168.1.17',
    'pi@192.168.1.18',
]

env.password = 'sgt-aturing'

def uptime():
    run("uptime")

def runPythonS():
    exec(open("./euler/sphere.py").read())


@parallel

def cmd(command):
    sudo(command)

def getTemp():
    sudo("/opt/vc/bin/vcgencmd measure_temp")

def runPythonP():
    exec(open("./euler/sphere.py").read())
