import threading
import time
import os  # for process id


def print_numbers():
    print("Child Thread Name:", threading.current_thread().name, "\n")
    print("Child Thread ID:", threading.get_ident(), "\n")
    print("Process ID:", os.getpid(), "\n")

    for i in range(5):
        print(i)
        time.sleep(1)


t = threading.Thread(target=print_numbers, name="Child-Worker")
t.start()

print("Main Thread Name:", threading.current_thread().name, "\n")
print("Main Thread ID:", threading.get_ident(), "\n")
print("Main Process ID:", os.getpid(), "\n")

for i in range(5):
    print("JAI SRIRAM")
