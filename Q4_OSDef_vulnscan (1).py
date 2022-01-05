import os

def sysinfo():
    print(os.popen('cat /etc/os-release').read())
    print(os.popen('find . -perm /4000').read())
    print(os.popen('hostnamectl').read())
    print(os.popen('ls -al ~/.ssh').read())
    print(os.popen('ps aux').read())
    print(os.popen('crontab -l').read())
    print(os.popen('/proc/net/tcp -a').read())
    print(os.popen('/proc/net/udp -a').read())
    print(os.popen('/proc/net/raw -a').read())
sysinfo()

# cat /etc/os-release # kernel Version
# find . -perm /4000  # SetUID bits
# hostnamectl # OS Version
# ls -al ~/.ssh # Find SSH keys
# ps aux # Running Processes
# crontab -l # List cron jobs
# /proc/net/tcp -a # Current sockets
# /proc/net/udp -a # Current sockets
# /proc/net/raw -a # Current sockets