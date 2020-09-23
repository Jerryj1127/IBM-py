from subprocess import Popen, PIPE, run
import re
TOKEN = "1hYCOPDOiUDMSRJ1zhs02MKWlip_4KktQPqSx28d3yhMaBsX3"
pid = Popen(["ngrok", "authtoken", TOKEN], stdout=PIPE)
s = pid.communicate()
print(s)