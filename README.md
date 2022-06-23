# python-simple-port-scanner
**USAGE**
python3 port-scan.py [flag] {target address} [threads]
             OPTIONS:
             **-R**: runs default mode using TCP socket to attempt connection to each port in the scan
             **-H**: Displays a help menu

This scanner is built in python using a few notable libraries (socket, threading, and queue among others). It works by attempting to establish a connection using a socket while iterating through a list of ports that are being used to connect to the socket. It used these connections successes list and compares it to a library of known services and used this to print to the user.
This process would have been far too slow without the use of threading and queues this allowed to run a function in x amount of threads and pull and remove from the queue meaning they are not completing the same jobs as each other.

NOTE: I am aware any IDS, IPS, or firewall will drop these requests but this project is for learning and experimenting with sockets and threading processes.


![image](https://user-images.githubusercontent.com/90014630/175179778-caadbe13-c3a9-4dbf-a363-e999925836b7.png)
