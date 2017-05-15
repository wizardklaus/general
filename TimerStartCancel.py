import threading

count=0

def on_timer():
    global count
    count+=1
    print(count)

    timer=threading.Timer(1,on_timer)
    timer.start()

    if count==10:
        print('Canceling timer...')
        timer.cancel()

print('Starting timer...')
on_timer()