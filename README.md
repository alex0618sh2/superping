# superping
Multithreaded SUPER ping - Многопоточный Супер Пинг


Многопоточный SUPER пинг для проверки физического состояния: радио, оптических и Ethernet каналов.

Запуск: 
python3 superping.py 30000 30 10.1.43.2

На хост 10.1.43.2 отправляем 30 потоков по 30000 пакетов
Что соответствует приблизительно 100Мб
Если машина на которой запускается прога - имеет 1Гб сетевую, можно пропустить и больше.

Общий результат проверки канала ниже.
Выводит усредненный результат, а также минимальные и максимальные показатели.
Плюс каждый поток фиксируется и его можно просмотреть, потери, задержки по отдельности.
Сохранить результаты. Вся история и временные файлы распологаются в /pingtmp
Из зависимостей использует iftop - его вывод по окончанию проверки можно просмотреть также.


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

Перед использованием: 
Положить в свою директорию /home/myName
в файле grabber.py - ddir = '/home/YouDIR/pingtmp', YouDIR - изменить на свою.
как и в mydir= 'YouDIR'
В файле superping.py указать свой интерфейс - interfacess = 'eth0'

Если параметры по умолчанию не устраивают, можно поменть их в файле superping.py
Размер пакетов: razmer = '1440'
Тайминги: ttim = '0.001'
Либо запустить так:
python3 superping.py 30000 30 10.1.43.2 1440 0.001


-----------------------------------------------------------------------------------


Подсказки:

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

Тестировалась на:
Operating System: Linux Mint 19.3
Kernel: Linux 4.15.0-134-generic
Architecture: x86-64

Iftop  - iftop/bionic,now 1.0~pre4-4
-------------------------------------------------------------------
Использование: бесплатно, на свой страх и риск. 
Если кто то что то этой прогой сделал, ответственности не несу.

Вопросы: shurped82собакевич.гмаил.ком


