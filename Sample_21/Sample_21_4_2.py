import threading
import queue
import os


def fun_name():
    while True:
        print("PID:", os.getpid())
        value = queue_obj.get()
        print("Do{0}".format(value))
        queue_obj.task_done()
queue_obj = queue.Queue()

threading.Thread(target=fun_name, daemon=True).start()

data = ["coffee", "tea", "juice", "milk", "milk"]
for item in data:
    queue_obj.put(item)

queue_obj.join()
print("----Program end----")