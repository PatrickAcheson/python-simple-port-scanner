from socket import getservbyport
import socket
import sys
import threading
from queue import Queue
from colorama import Fore
from colorama import Style

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
                print(f"{port}/tcp   {Fore.GREEN}{services[port]['status']}{Style.RESET_ALL}    {services[port]['type']}")
            except:
                services.update({port:{"type":"unknown","status":"open"}})
                print(f"{port}/tcp   {Fore.GREEN}{services[port]['status']}{Style.RESET_ALL}    {services[port]['type']}")
                pass

if __name__ == "__main__":
    try:
        target_address, threads = str(sys.argv[1]), int(sys.argv[2])
    #Printing scan header
        print("----------------------------------")
        print(f"scan report for {target_address}  -bng-")
        print("----------------------------------")
        print("PORT      STATE      SERVICE")
        ports_open = []
        thread_list = []
        queue = Queue()
        services = {}
        ports_var = 1024 #To edit amount of a ports scanned edit this
        port_list = range(1, ports_var)
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
        print(f"scan complete: on address ({target_address})")
    except Exception as err:
        print(f"""
        Usage: python3 script.py [IP address] [port range]
        Example: python3 script.py 127.0.0.1 1000
        Scans the range of ports from 1 to 1000 on the IP address 127.0.0.1""")