#question 1 vulnerability scanning
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ports = [1,5,7,18,20,21,22,23,25,29,37,42,43,49,53,59,70,79,80,103,108,109,10,115,118,119,137,139,143,150,156,161,179,190,194,197,389,396,443,444,445,458,546,547,563,569,1080]

openportlist = []
for port in range(1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("10.12.0.30",port))
        print(f'Port {port} Open')
        openportlist.append(port)
        print(openportlist)
    except Exception as e:
        print(f'Port {port} Closed')
    s.close()
    print(openportlist)
###above part works and ports 21,22,and 80 are open
