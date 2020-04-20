import os
import sys
import yaml
import subprocess
#try:

#f=open("D:\dev.yaml")
#a=subprocess.run(['cat','D:\dev.yaml'],capture_output=True,text=True,shell=True)
#a=subprocess.run(['dir'],capture_output=True,shell=True,text=True)
a=subprocess.run(['ls','ltr'],shell=True,capture_output=True)
#print(a.stdout)
#print(a.stderr)
if(a.returncode != 0):
    print("happy")
else:
    print("false")
    #f.close()
#except FileNotFoundError as f:
    #print(repr(f))

#abc=yaml.load(f)
#a1=abc['app_name']
    #print(a1)
#f.close()
#dir(os)
