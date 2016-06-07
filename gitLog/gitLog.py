import subprocess
import sys
from time import localtime, strftime

def osCheck(userPath):
	#print (userPath) 
	if sys.platform != 'win32': 
		userPath=userPath.replace('\\','/')
	return userPath
def makeCMD(userLoc):
	if sys.platform != 'win32': 
		userLoc=userLoc.replace('\\','/')
		cmd = ["cd", "%s" % userLoc, "|", "git", "log", "--stat", "--reverse" ]
		cmdFirstOnly = ["cd", "%s" % userLoc, "|", "git", "log", "--stat", "--log-size", "-1", "--pretty=fuller" ]
	else:
		cmd = ["cd", "%s" % userLoc, "&", "git", "log", "--stat", "--reverse" ]
		cmdFirstOnly = ["cd", "%s" % userLoc, "&", "git", "log", "--stat", "--log-size", "-1", "--pretty=fuller" ]
	cmd = [cmd,cmdFirstOnly]
	print (cmd)
	return cmd

#path of private repo
fileLoc= osCheck(str(sys.argv[1]))
#log file full
destLoc= osCheck(str(sys.argv[2]))
#log file first only
destLocFirst= osCheck(str(sys.argv[3]))

cmd = makeCMD(fileLoc)

logInfoFull = subprocess.Popen(cmd[0], stdout=subprocess.PIPE, shell=True)
logInfoFirst = subprocess.Popen(cmd[1], stdout=subprocess.PIPE, shell=True)


out, err = logInfoFull.communicate()
logInfoFull = out.decode("utf-8")

out, err = logInfoFirst.communicate()
logInfoFirst = out.decode("utf-8")

fileLoc = open(destLoc, 'w+')
fileLoc.write('Newest Revision as of {}:\n\n'.format(strftime("%Y-%m-%d %H:%M:%S", localtime())))
fileLoc.write(logInfoFirst)

fileLoc = open (destLocFirst, 'w+')
fileLoc.write(logInfoFull)

fileLoc.close()