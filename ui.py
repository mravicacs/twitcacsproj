import os, sys, resource, time

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def printmenu():
  print "CACS Twitter   -  ",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, ' KB RAM Used' 
  print "1. Fetch & Clean"
  print "2. Settings"
  print "3. Exit"

def usrinput():
  global usrinputvar
  usrinputvar = int(raw_input("Enter Choice: "))
  if (usrinputvar == 1):
    fetchnclean()
  if (usrinputvar == 2):
    settingsmenu()
  if (usrinputvar == 3):
    sys.exit()

def fetchnclean():
  cls()
  print "Fetch & Clean Menu"
  time.sleep(3)
  runmenu()
  
def settingsmenu():
  cls()
  print "Settings Menu"
  time.sleep(3)
  runmenu()
     
def runmenu():
  cls()
  printmenu()
  usrinput()

runmenu()