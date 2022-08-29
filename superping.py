"""
thread basics: start 5 copies of a function running in parallel;
uses time.sleep so that the main thread doesn't die too early--
this kills all other threads on some platforms; stdout is shared:
thread outputs may be intermixed in this version arbitrarily.
"""
import os
import sys
import _thread as thread, time
from pingtmp.conf.grabber import *
#ddir -> grabber modules
#mydir -> grabber modules

#Packets size
try:
    razmer = sys.argv[4]
except IndexError:
    razmer = '1440'

#quantity packets
packets = sys.argv[1]

#Interval
try:
    ttim = sys.argv[5]
except IndexError:
    ttim = '0.001'
# IP ADDRESS
ip = sys.argv[3]

#threads
pthr = int(sys.argv[2])
loops = 1 #loops
interfacess = 'eth0'
stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * pthr
cleartemp = 0
historysave = 0
allhistory = 0

#try :
#    zzz = sys.argv[4]
#except IndexError:
#    zzz = '123456'


os.system ('rm -f /home/'+mydir+'/pingtmp/*.ttmp')
def counter(myId, count):                        # function run in threads
    for i in range(count):
        #time.sleep(1)                            # simulate real work
        stdoutmutex.acquire()
        print('START ============================================= [%s] => %s' % (myId, i))
        stdoutmutex.release()
        os.system ('ping -s %s -c %s -i %s %s | tee %s/ping%s.ttmp' % (razmer, packets, ttim, ip, ddir, myId))
        stdoutmutex.acquire()
        print ('END ############################################## [%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId] = True

#mutex = thread.allocate_lock()
os.system('iftop -t -i %s -f \'host %s\' > %s/iftop.ttmp &' % (interfacess, ip, ddir))
#os.system ('IFTOP_PID=$!')
start_time = time.time()

for i in range(pthr):                               # spawn 5 threads
    thread.start_new_thread(counter, (i, loops))     # each thread loops 5 times

#time.sleep(10)
while False in exitmutexes: pass


print ('.............collect statistics...................................')
for iii in range(pthr):
    os.system ('tail -n 2 %s/ping%s.ttmp | tee -a %s/stat.ttmp'% (ddir, iii, ddir))
print ('.............collect statistics END...............................')

os.system('killall iftop') #kill iftop


#os.system('kill $IFTOP_PID')
print('             Main thread exiting')                    # don't exit too early

print("============ ALL TIME: %s seconds ============" % (time.time() - start_time))
os.system ('echo \'\n============ ALL TIME: %s seconds ============\' > %s/time.ttmp' % (time.time() - start_time, ddir))
timenow = time.ctime()
os.system ('echo \'Time %s\' >> %s/time.ttmp' % (timenow, ddir))
os.system ('echo \'IP %s, Threading %s, Packets on thread %s\' >> %s/time.ttmp' % (ip, pthr, packets, ddir))
os.system ('echo \'Packets size %s, Interval %s \' >> %s/time.ttmp' % (razmer, ttim, ddir))
###################################################################################
# sobiraem itogovoe srednee
grepper()
sedder()
stolber()
rTX, rRX, rminTX, rmaxTX, rminRX, rmaxRX = griftop()
if checker() == 1:
    ssprinter(0, rTX, rRX, rminTX, rmaxTX, rminRX, rmaxRX)
else:
    scheter()
    ssprinter(1, rTX, rRX, rminTX, rmaxTX, rminRX, rmaxRX)
####################################################################################
while True:
    alist = [ii for ii in range(0,pthr)]
    print ('Process:', end="" ), print (alist)
    print ('---------------------------------------------------------------------')
    print ('| Exit: q | Stat: S | IfTop: I | View process ENTER 0..%s | Help: H |' % (pthr-1))
    print ('---------------------------------------------------------------------')
    inputflag = input("Insert:")
    if inputflag == 'Q' or inputflag == 'q': #quit
        break
    elif inputflag == 's' or inputflag == 'S': #statistiks
        os.system ('cat -T %s/stat.ttmp %s/time.ttmp %s/ssprinter.ttmp | less' % (ddir, ddir, ddir))
    elif inputflag == 'i' or inputflag == 'I': #iftop
        os.system ('cat -T /home/'+mydir+'/pingtmp/iftop.ttmp | less')
    elif inputflag == 'H' or inputflag == 'h': #help
        os.system ('cat -T /home/'+mydir+'/pingtmp/conf/.help | less')
    elif inputflag == 'q!' or inputflag == 'Q!': #clear temp
        cleartemp = 1
        break
    elif inputflag == 's!' or inputflag == 'S!': #save history
        historysave = 1
        os.system ('cat -T %s/time.ttmp %s/ssprinter.ttmp >> %s/history.tmpp' % (ddir, ddir, ddir))
    elif inputflag == 'sc' or inputflag == 'SC': #clear history
        historysave = 2
        os.system ('rm -f /home/'+mydir+'/pingtmp/*.tmpp')
    elif inputflag == 'e' or inputflag == 'E':
        os.system ('cat -T %s/history.tmpp | less' %(ddir))
    elif inputflag == 'al!': # save all history
        allhistory = 1
        os.system ('cat -T %s/time.ttmp %s/ssprinter.ttmp %s/stat.ttmp >> %s/histall.atmp' % (ddir, ddir, ddir, ddir))
    elif inputflag == 'al': #view all history
        os.system ('cat -T %s/histall.atmp | less' %(ddir))
    elif inputflag == 'alc' : #clear all history
        allhistory = 2
        os.system ('rm -f /home/'+mydir+'/pingtmp/*.atmp')
    elif not inputflag.isdigit( ):
        print ('!Read Help!')
    elif int(inputflag) in alist:
        digit = inputflag
        os.system ('cat -T %s/ping%s.ttmp | less' %(ddir, digit))
    elif inputflag.isdigit( ):
        print ('Read Help - No process!')
    else:
        break

if cleartemp == 1:
    os.system ('rm -f /home/'+mydir+'/pingtmp/*.ttmp')
    print ('Clear Temporary files...')

if historysave == 1:
    print ('History SAVE...')

if historysave == 2:
    print ('History CLEAN...')

if  allhistory == 1:
    print ('ALL History SAVE...')

if  allhistory == 2:
    print ('ALL History CLEAN...')

print ('GoodBay')
