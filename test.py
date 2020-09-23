from subprocess import Popen, PIPE, run
import re
pid = Popen(["ngrok", "authtoken", TOKEN], stdout=PIPE)
s = pid.communicate()
print(s)