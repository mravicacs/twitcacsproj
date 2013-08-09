from twython import Twython
import codecs
import os, resource
import csv

datacontainer= []  #declared for containing data in csv, remains in memory

def openfile():  #function to pull file
  with open('rawdata.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar="|")
    for row in spamreader:
      datacontainer.append(row)
  csvfile.close()

def cleanfile():  #joins skipped lines with one another
  counterloopcleanfile = 1
  while (counterloopcleanfile < (int (len(datacontainer)) - 1 ) ):
    try:  #Try, check to see if things have printed properly
      valuecheck = datacontainer[counterloopcleanfile][6] #For testing/printing purposes only, hide this line later
    except: #If Cell 1 of row is an 'enter' and needs to be cleaned and added to end of previous row, change 
      #print 'Found Cell 1 Incorrect' , datacontainer[counterloopcleanfile-1][4], datacontainer[counterloopcleanfile][0]  #displays invalid values
      testervariable = datacontainer[counterloopcleanfile-1][6] + datacontainer[counterloopcleanfile][0]
      datacontainer[counterloopcleanfile-1][6] = str(testervariable)
      datacontainer.pop(counterloopcleanfile)
      # print  datacontainer[counterloopcleanfile-1][5] #print this to check validity of combiner
    counterloopcleanfile+=1
      
def bodyprint():  #runs function to print cleaned array of CSV
  counterloopbodyprint = 0
  for x in datacontainer:
    print str(counterloopbodyprint).rjust(3), 
    print x[0].ljust(20),  x[1].ljust(20), x[2].ljust(15), x[3].ljust(8), x[4].ljust(25), x[5].ljust(25), x[6][0:60].ljust(60) #Sample of printout on screen, justifies for use with .ljust
    counterloopbodyprint+=1

def removeduplicates(datacontainer):
    found = set()
    for item in datacontainer:
        if item[0] not in found:
            yield item
            found.add(item[0])

def rewritefile():
  wr = csv.writer(open('rawdata.csv', 'wb'), delimiter=',', quotechar='', quoting=csv.QUOTE_NONE)
  wr.writerows(datacontainer)
            
openfile()  
cleanfile()
removeduplicates(datacontainer)
datacontainer = list(removeduplicates(datacontainer)) 
bodyprint()   
rewritefile()

print 'KB RAM Used', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

'''        
for items in x:    #Prints full array - use for testing
  print items
'''