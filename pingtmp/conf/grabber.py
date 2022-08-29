import os
import sys
import string

ddir = '/home/YouDIR/pingtmp'
mydir= 'YouDIR'
stack = []


def grepper ():
    os.system ('grep packets %s/stat.ttmp > %s/st1.ttmp' % (ddir,ddir))
    os.system ('grep min/avg/max/mdev %s/stat.ttmp > %s/st2.ttmp' % (ddir,ddir))

def sedder():
    os.system ('sed -i \'s/packets transmitted, //\' /home/%s/pingtmp/st1.ttmp' % (mydir))
    os.system ('sed -i \'s/received, //\' /home/%s/pingtmp/st1.ttmp' % (mydir))
    os.system ('sed -i \'s/% packet loss, time//\' /home/'+mydir+'/pingtmp/st1.ttmp')
    os.system ('sed -i \'s/ms//\' /home/%s/pingtmp/st1.ttmp' % (mydir))

    os.system ('sed -i \'s/rtt min//\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/avg//\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/max//\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/mdev = //\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/ms//\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/pipe//\' /home/%s/pingtmp/st2.ttmp' % (mydir))

    os.system ('sed -i \'s/\///\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/\///\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/\///\' /home/%s/pingtmp/st2.ttmp' % (mydir))

    os.system ('sed -i \'s/\// /\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/\// /\' /home/%s/pingtmp/st2.ttmp' % (mydir))
    os.system ('sed -i \'s/\// /\' /home/%s/pingtmp/st2.ttmp' % (mydir))

def stolber():
    os.system ('cut -d \" \" -f 1 %s/st1.ttmp > %s/cllmt1.ttmp' % (ddir,ddir))
    os.system ('cut -d \" \" -f 2 %s/st1.ttmp > %s/cllmt2.ttmp' % (ddir,ddir))
    os.system ('cut -d \" \" -f 3 %s/st1.ttmp > %s/cllmt3.ttmp' % (ddir,ddir))
    os.system ('cut -d \" \" -f 4 %s/st1.ttmp > %s/cllmt4.ttmp' % (ddir,ddir))

    os.system ('cut -d \" \" -f 1 %s/st2.ttmp > %s/cllmt5.ttmp' % (ddir,ddir))
    os.system ('cut -d \" \" -f 2 %s/st2.ttmp > %s/cllmt6.ttmp' % (ddir,ddir))
    os.system ('cut -d \" \" -f 3 %s/st2.ttmp > %s/cllmt7.ttmp' % (ddir,ddir))
    os.system ('cut -d \" \" -f 4 %s/st2.ttmp > %s/cllmt8.ttmp' % (ddir,ddir))
    #os.system ('cat -t /home/alex/pingtmp/cllmt.ttmp')

#cut -d " " -f 0 st2.ttmp
#sudo sed -i 's/\// /' st2.ttmp
#sudo sed -i 's/, pipe//' st2.ttmp

def scheter():
    for nn in range (1,9):
        fdescr = open("%s/cllmt%s.ttmp" % (ddir,nn))
        arg = []
        for line in fdescr:
            lines = line.strip(' ')
            findex = lines.find('.')
            if findex ==-1:
                arg.append(int(lines))
            else:
                arg.append(float(lines))
        colelm = len(arg)
        summa = sum(arg)
        try:
            srednee = summa/colelm
        except ZeroDivisionError:
            srednee = 0

        if nn == 1 or nn == 2 :
            stack.append(summa)
        else:
            stack.append(srednee)
        #print ('list: ', arg)
        #print ('kolichestvo el: ', colelm)
        #print('summa:', summa)
        #print ('srednee: ', srednee)
        #print ('st: ',  stack)
    #print (stack)
    return stack

def ssprinter(xx, txr, rxr, tmin, tmax, rmin, rmax):
    srTX = txr; srRX = rxr
    txmin = tmin; txmax = tmax; rxmin = rmin; rxmax = rmax
    if xx == 1:
        rttmdev = stack.pop()
        rttmax = stack.pop()
        rttavg = stack.pop()
        rttmin = stack.pop()
        timeosy = stack.pop()
        lossosy = stack.pop()
        obratosy = stack.pop()
        packetosy = stack.pop()
        print ('.....................................................................')
        print ('ALL packets transmitted: %s, ALL packets received: %s' % (packetosy, obratosy))
        print ('AVG loss: %s, AVG time: %s ms' % (lossosy, timeosy))
        print ('AVG RTT ms:  min %s, avg %s ' % (rttmin, rttavg))
        print ('AVG RTT ms:  max %s, mdev %s' % (rttmax, rttmdev))
        print ('RATE AVG IfTop: tx %s Mb, rx %s Mb' % (srTX, srRX))
        print ('RATE TX IfTop: min %s Mb, max %s Mb' % (txmin, txmax))
        print ('RATE RX IfTop: min %s Mb, max %s Mb' % (rxmin, rxmax))
        print ('.....................................................................')
        #print (stack.pop())
        ffdescr = open("%s/ssprinter.ttmp" % (ddir), 'w')
        ffdescr.write('.....................................................................\n')
        ffdescr.write('ALL packets transmitted: %s, ALL packets received: %s \n' % (packetosy, obratosy))
        ffdescr.write('AVG loss: %s, AVG time: %s ms\n' % (lossosy, timeosy))
        ffdescr.write('AVG RTT ms:  min %s, avg %s \n' % (rttmin, rttavg))
        ffdescr.write('AVG RTT ms:  max %s, mdev %s \n' % (rttmax, rttmdev))
        ffdescr.write('RATE AVG IfTop: tx %s Mb, rx %s Mb \n' % (srTX, srRX))
        ffdescr.write('RATE TX IfTop: min %s Mb, max %s Mb \n' % (txmin, txmax))
        ffdescr.write('RATE RX IfTop: min %s Mb, max %s Mb \n' % (rxmin, rxmax))
        ffdescr.write('.....................................................................\n')
        ffdescr.close()
    else:
        print ('###################################################################')
        print ('Ping BAD - LOSS and Errors and DUP')
        print ('See Statistiks and Process')
        print ('###################################################################')
        #print (stack.pop())
        ffdescr = open("%s/ssprinter.ttmp" % (ddir), 'w')
        ffdescr.write('###################################################################\n')
        ffdescr.write('Ping BAD - LOSS and Errors and DUP \n')
        ffdescr.write('See Statistiks and Process\n')
        ffdescr.write('###################################################################\n')
        ffdescr.close()

def poisk(filename, stringa):
    fstack = []
    fddescr = open (filename)
    for line in fddescr:
        #print (line)
        indd = line.find(stringa)
        if indd != -1:
            #print('OK')
            fstack.append(1)
        else:
            #print ('no')
            fstack.append(0)

    #print(fstack)
    if sum(fstack) == 0:
        #print('Err NO')
        return 0
    else:
        #print ('Err YES')
        return 1

def checker():
    pstack = []
    #---------------------------------------------#
    if poisk ('%s/st1.ttmp' % (ddir), 'err') == 0:
        pstack.append(0) #print ('pst: OK')
    else:
        pstack.append(1) #print('pst: NO')
    #---------------------------------------------#
    if poisk ('%s/st2.ttmp' % (ddir),'err') == 0:
        pstack.append(0) #print ('pst1 OK')
    else:
        pstack.append(1) #print('pst1 NO')
    #---------------------------------------------#
    if poisk ('%s/st1.ttmp' % (ddir), 'dup') == 0:
        pstack.append(0) #print ('pst2: OK')
    else:
        pstack.append(1) #print('pst2: NO')
    #---------------------------------------------#
    if poisk ('%s/st2.ttmp' % (ddir),'dup') == 0:
        pstack.append(0) #print ('pst3 OK')
    else:
        pstack.append(1) #print('pst3 NO')
    #---------------------------------------------#
    #print ('pstack:', pstack)
    if sum(pstack) == 0:
        #print('ERr NO Vse OK')
        return 0
    else:
        #print ('STOP')
        return 1

def griftop():
    txstack = []; rxstack = []

    #os.system ('grep \'=>\' %s/iftop.ttmp > %s/tx.ttmp' % (ddir, ddir))
    #os.system ('grep \'<=\' %s/iftop.ttmp > %s/rx.ttmp' % (ddir, ddir))
    os.system ('grep \'Total send rate:\' %s/iftop.ttmp > %s/tx.ttmp' % (ddir, ddir))
    os.system ('grep \'Total receive rate:\' %s/iftop.ttmp > %s/rx.ttmp' % (ddir, ddir))
    with open('%s/tx.ttmp' % (ddir)) as ftx:
        LT = [lineftx.split() for lineftx in ftx]
    with open('%s/rx.ttmp' % (ddir)) as rtx:
        LR = [linertx.split() for linertx in rtx]

    #print (LT)
    #print (LR)
    #print (len(LT))
    #print (len(LR))

    for nlt in range(len(LT)):
        try:
            tmpLT = LT[nlt][3]
            #print ('tryLT', tmpLT)
        except IndexError:
            tmpLT = 0
        tmpLT = str(tmpLT)
        #print ('str', tmpLT)
        tmpLT = tmpLT.replace ('Mb','')
        #print ('replace', tmpLT)
        #print ('type-repl', type(tmpLT))

        #### del zpt in stringo
        if tmpLT.find(',') != -1:
            #z = tmpLT.find(',')
            #print ('ES', z)
            tmpLT = tmpLT.replace(',','.')
            #print(tmpLT)
        else:
            pass
            #print ('NO')
        #### end del zpt in stringo

        try:
            tmpLTdigit = float(tmpLT)
            #print ('tmpLT', tmpLT)
            #print ('type-tmpLT',type(tmpLT))
            #print ('type-tmpdigit', type(tmpLTdigit))
            #print('digit', tmpLTdigit)
        except ValueError:
            tmpLTdigit = 0
            #print ('EXC')
        txstack.append(tmpLTdigit)

    sumTxStack = sum(txstack)

    for nnt in range(len(LR)):
        try:
            tmpLR = LR[nnt][3]
            #print ('tryLR', tmpLR)
        except IndexError:
            tmpLT = 0
        tmpLR = str(tmpLR)
        tmpLR = tmpLR.replace ('Mb','')

        #### del zpt in stringo
        if tmpLR.find(',') != -1:
            #z = tmpLR.find(',')
            #print ('ES', z)
            tmpLR = tmpLR.replace(',','.')
            #print(tmpLR)
        else:
            pass
        #### end del xpt in stringo

        try:
            tmpLRdigit = float(tmpLR)
        except ValueError:
            tmpLRdigit = 0
        rxstack.append(tmpLRdigit)

    sumRxStack = sum(rxstack)

    colelmTX = len(txstack)
    try:
        sredneeTX = sumTxStack/colelmTX
    except ZeroDivisionError:
            sredneeTX = 0

    colelmRX = len(rxstack)
    try:
        sredneeRX = sumRxStack/colelmRX
    except ZeroDivisionError:
            sredneeRX = 0

    #print (txstack)
    #print (sumTxStack)
    #print (rxstack)
    #print (sumRxStack)
    #print  (sredneeTX)
    #print  (sredneeRX)
    try:
        minTX = min(txstack)
        maxTX = max(txstack)
    except ValueError:
        minTX = 0; maxTX = 0

    try:
        minRX = min(rxstack)
        maxRX = max(rxstack)
    except ValueError:
        minRX = 0; maxRX = 0

    #print (minTX, maxTX, minRX, maxRX)
    return sredneeTX, sredneeRX, minTX, maxTX, minRX, maxRX

if __name__ == "__main__":
    grepper()
    sedder()
    stolber()
    rTX, rRX, rminTX, rmaxTX, rminRX, rmaxRX = griftop()
    if checker() == 1:
        ssprinter(0, rTX, rRX, rminTX, rmaxTX, rminRX, rmaxRX)
    else:
        scheter()
        ssprinter(1, rTX, rRX, rminTX, rmaxTX, rminRX, rmaxRX)

