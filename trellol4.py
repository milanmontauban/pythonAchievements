import time
import webbrowser


for i in range(1, 1001):
    print(i)
    time.sleep(1 / 100)
    if i == 1000:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1')
