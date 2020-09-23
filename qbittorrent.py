import threading
import time
import requests
import json
import subprocess

class qbit:

    def __init__(self, port):
        self.port = port

    def torrent(self):
        command = subprocess.Popen(['qbittorrent-nox', f'--webui-port={self.port}'])

    def ngrok(self):
        
        ngrok_cmd = subprocess.Popen(['ngrok', 'http', str(self.port)])    
        localhost_url = "http://localhost:4040/api/tunnels"
        time.sleep(1)
        tunnel_url = requests.get(localhost_url).text
        json_data = json.loads(tunnel_url)

        tunnel_url = json_data['tunnels'][0]['public_url']
        tunnel_url = tunnel_url.replace("https", "http")
        print('Running at localhost: ' + str(self.port))
        print(tunnel_url)
        self.tun = tunnel_url


    def start(self):
        print(self.port)
        thread_torrent = threading.Thread(target = self.torrent(), args=(int(self.port),))
        thread_ngrok = threading.Thread(target = self.ngrok(), args=(int(self.port),))

        thread_torrent.start()
        print('Torrent server started!')

        time.sleep(5)
        print('Establishing secure connection!')
        
        thread_ngrok.start()
        print('Secure connection established...')
        
        thread_ngrok.join()
        thread_torrent.join()