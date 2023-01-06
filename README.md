# python-simple-port-scanner
<h2>USAGE</h2>

`python3 port-scan.py {target address} [threads]`

**threads**: suggested value is from [50-200]

The script scans the specified target address for open ports using the specified number of threads.

Arguments:
  target address: The IP address or hostname of the target to scan.
  threads: The number of threads to use for the scan. Suggested value is between 50 and 200.

<h2>About The Project</h2>
This port scanner is built in Python using the socket, threading, and queue libraries. It establishes connections using sockets and iterates through a list of ports, recording successes and comparing them to a library of known services. Threading and queues are used to speed up the process and prevent duplicate work.
Note: This project is for learning and experimentation purposes only. IDS, IPS, and firewalls may drop these requests.

<h2>Running port-scan.py</h2>

![ezgif-2-c4cbce8ace](https://user-images.githubusercontent.com/90014630/175423311-77491b52-bda6-402d-80fe-55b8e59e0df0.gif)
