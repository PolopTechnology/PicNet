import im2ascii
import time

frames = int(input("Frames?"))
speed = int(input("Speed of the animation"))
i = 0
frame_values = []

while i < frames:
    qi = input("choose a path for frame " + str(i))
    frame_values.append(qi)
    i += 1

c = 0
j = len(frame_values)

while c < j:
    ff = frame_values[c]
    hola = im2ascii.asciify(ff)
    print(hola)
    c += 1
    time.sleep(speed)

