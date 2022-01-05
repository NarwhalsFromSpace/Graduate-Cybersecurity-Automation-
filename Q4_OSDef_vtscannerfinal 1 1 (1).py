#malware scanning question
import requests, time, os


def vt(targetfile):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': '9a75b111a2a368d1fa3085c89ffa8f3e5968332fd7bbb90f0a7d03e54965b8b7'}
    
    files = {'file': ('targetfile',open(targetfile, 'rb').read())}
    try:
        response = requests.post(url, files=files, params=params)
        x = response.json()
        try:
            print('waiting for report!')
            time.sleep(120)
            scan_id = x['scan_id']
            repurl = 'https://www.virustotal.com/vtapi/v2/file/report'
            params2 = {'apikey': '9a75b111a2a368d1fa3085c89ffa8f3e5968332fd7bbb90f0a7d03e54965b8b7', 'resource': scan_id}
            response = requests.get(repurl, params=params2)
            y = response.json()
            scantotal = y['total']
            scanpositives = y['positives']
            posperc = (scanpositives/scantotal)*100
            if posperc >= 5:
                print('FILE',targetfile,'IS MALICOUS!')
                time.sleep(5)
            else:
                logtxt = 'FILE',targetfile,'is safe and was not deleted. Scan will continue.'
                print(logtxt)
        except requests.RequestException as e:
            print(e)
    except requests.RequestException as e:
        print(e)
        
def scanner():
    path_to_watch = input('Enter Filepath to watch i.e C:\\Users\\Desktop\\week8\\ScanMe')
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    for each in before:
        targetfile = path_to_watch + '\\' + each
        print(targetfile)
        vt(targetfile)
        time.sleep(100)
#     while True:
#         time.sleep (100)
#         after = dict ([(f, None) for f in os.listdir (path_to_watch)])
#         print(after)
#         added = [f for f in after if not f in before]
#         print(added, 'was added to the folder')
#         if added: 
#             targetfile = path_to_watch + '\\' + added[0]
#             print(targetfile)
#             vt(targetfile)
#         before = after
scanner()  
