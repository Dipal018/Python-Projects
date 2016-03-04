import webbrowser
import time
break_count=0

print ("This program Started on: " + time.ctime())
while break_count < 3:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=4nd01DwuHwE")
    break_count+=1


