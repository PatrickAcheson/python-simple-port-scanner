from socket import getservbyport
import socket
import sys
import threading
from queue import Queue
#https://github.com/PatrickAcheson

def scanner(port, target_address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_address, port))
        return True
    except:
        return False

def use_queue(port_list):
    for port in port_list:
        queue.put(port)

def process(target_address, ports_open):
    while not queue.empty():
        port = queue.get()
        if scanner(port, target_address) == True:
            try:
                port_type = getservbyport(port,"tcp")
                services.update({port:{"type":port_type,"status":"open"}})
                print(f"{port}       {services[port]['status']}       {services[port]['type']}")
            except:
                services.update({port:{"type":"unknown","status":"open"}})
                print(f"{port}       {services[port]['status']}       {services[port]['type']}")
                pass

def help_prnt():
    print("""Usage: python3 port-scan.py [flag] {target address} [threads]
             OPTIONS:
             -R: runs default mode using socket connection with TCP handshake
             -H: Displays this mode lol  
""")
    exit()

if __name__== "__main__":
    flag, target_address, threads = str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3])

    if flag =="-R" or flag =="-r":
        pass
    elif flag == "-h" or flag == "-H":
            help_prnt()          
    else:
        print("wrong syntax!")
        help_prnt()

    print("----------------------------------")
    print(f"scan report for {target_address}    -bng-")
    print("----------------------------------")
    print("PORT      STATE      SERVICE")

    ports_open = []
    thread_list = []
    queue = Queue()
    services = {}

    port_list = range(1, 1024)
    process(target_address, ports_open)
    use_queue(port_list)

    for t in range(threads):
        thread = threading.Thread(target=process,args=(target_address, ports_open))
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print("----------------------------------")
    print(f"hidden: {max(port_list) - len(services) + 1} closed tcp ports")
    print(f"scan complete: 1 IP address ({target_address})")