

def install_ngrok(TOKEN):
    import os
    from zipfile import ZipFile
    from urllib.request import urlretrieve
    from subprocess import Popen, PIPE, run
        
    url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
    urlretrieve(url, 'ngrok-amd64.zip')
        
    with ZipFile('ngrok-amd64.zip', 'r') as zip_ref:
        zip_ref.extractall('/usr/local/bin/')
    os.chmod('/usr/local/bin/ngrok', 0o755)
    os.unlink('ngrok-amd64.zip')


    if TOKEN != "":
            pid = Popen(["ngrok", "authtoken", TOKEN], stdout=PIPE)
            s = pid.communicate()
    return s

