# python-simple-port-scanner
<h2>USAGE</h2>

`python3 port-scan.py [flag] {target address} [threads]`

**flag options**:
`-R`: runs default mode using TCP socket to attempt connection to each port in the scan
`-H`: Displays a help menu

**threads**: suggested value is from [50-200]

<h2>About The Project</h2>

This scanner is built in python using a few notable libraries (socket, threading, and queue among others). It works by attempting to establish a connection using a socket while iterating through a list of ports that are being used to connect to the socket. It used these connections successes list and compares it to a library of known services and used this to print to the user.
This process would have been far too slow without the use of threading and queues this allowed to run a function in x amount of threads and pull and remove from the queue meaning they are not completing the same jobs as each other.

NOTE: I am aware any IDS, IPS, or firewall will drop these requests but this project was for learning and experimenting with sockets and threading processes.

<h2>Running port-scan.py</h2>

![ezgif-2-c4cbce8ace](https://user-images.githubusercontent.com/90014630/175423311-77491b52-bda6-402d-80fe-55b8e59e0df0.gif)
