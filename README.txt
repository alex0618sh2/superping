������������� SUPER ���� ��� �������� ����������� ���������: �����, ���������� � Ethernet �������.

������: 
python3 superping.py 30000 30 10.1.43.2

�� ���� 10.1.43.2 ���������� 30 ������� �� 30000 �������
��� ������������� �������������� 100��
���� ������ �� ������� ����������� ����� - ����� 1�� �������, ����� ���������� � ������.

����� ��������� �������� ������ ����.
������� ����������� ���������, � ����� ����������� � ������������ ����������.
���� ������ ����� ����������� � ��� ����� �����������, ������, �������� �� �����������.
��������� ����������. ��� ������� � ��������� ����� ������������� � /pingtmp
�� ������������ ���������� iftop - ��� ����� �� ��������� �������� ����� ����������� �����.


30000 packets transmitted, 29941 received, 0% packet loss, time 116386ms
rtt min/avg/max/mdev = 1.371/4.491/100.024/2.209 ms, pipe 11
30000 packets transmitted, 29941 received, 0% packet loss, time 106237ms
rtt min/avg/max/mdev = 1.316/4.386/100.015/2.295 ms, pipe 11
30000 packets transmitted, 29935 received, 0% packet loss, time 111640ms
rtt min/avg/max/mdev = 1.329/4.494/100.023/2.271 ms, pipe 11
.............collect statistics END...............................
             Main thread exiting
============ ALL TIME: 119.37626528739929 seconds ============
.....................................................................
ALL packets transmitted: 900000, ALL packets received: 898098
AVG loss: 0.0, AVG time: 113989.03333333334 ms
AVG RTT ms:  min 1.3259333333333339, avg 4.452
AVG RTT ms:  max 99.20459999999999, mdev 2.2283333333333335
RATE AVG IfTop: tx 85.36724137931033 Mb, rx 85.21379310344828 Mb
RATE TX IfTop: min 68.2 Mb, max 89.6 Mb
RATE RX IfTop: min 68.2 Mb, max 89.6 Mb
.....................................................................
Process:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
---------------------------------------------------------------------
| Exit: q | Stat: S | IfTop: I | View process ENTER 0..29 | Help: H |
---------------------------------------------------------------------
Insert:

========================================================================================================================

����� ��������������: 
�������� � ���� ���������� /home/myName
� ����� grabber.py - ddir = '/home/YouDIR/pingtmp', YouDIR - �������� �� ����.
��� � � mydir= 'YouDIR'
� ����� superping.py ������� ���� ��������� - interfacess = 'eth0'

���� ��������� �� ��������� �� ����������, ����� ������� �� � ����� superping.py
������ �������: razmer = '1440'
��������: ttim = '0.001'
���� ��������� ���:
python3 superping.py 30000 30 10.1.43.2 1440 0.001


-----------------------------------------------------------------------------------


���������:

----------------------- HELP -------------------------------------
View process - Insert number process and press ENTER 0..XX
View statistics - Insert S and press ENTER:
View interface statistics IfTop - Insert I and press ENTER:
Exit - Insert Q or q and press ENTER:
Used for viewing program cat -T | less. Choose: q -to end viewing
..................................................................
Exit and clear ttmp files - Insert q! and press ENTER:

Save history - Insert s! or S!
Clear history - Insert sc or SC
View history - Insert e or E

Save ALL history - Insert al!
Clear ALL history - Insert alc
View ALL history - Insert al
----------------------- HELP -------------------------------------

������������� ��:
Operating System: Linux Mint 19.3
Kernel: Linux 4.15.0-134-generic
Architecture: x86-64

Iftop  - iftop/bionic,now 1.0~pre4-4
-------------------------------------------------------------------
�������������: ���������, �� ���� ����� � ����. 
���� ��� �� ��� �� ���� ������ ������, ��������������� �� ����.

�������: shurped82���������.�����.���


