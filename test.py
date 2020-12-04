import threading
def foo(num):
    print(num)
    threading.Timer(0.05, foo, args=(num+1,)).start()
    return "de"
try:
    foo(1)
except:
    print("end")
