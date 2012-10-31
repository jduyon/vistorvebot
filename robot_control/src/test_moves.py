import create
import time


r = create.Create("/dev/ttyS0")

r.go(5)
time.sleep(0.5)
r.go(10)
time.sleep(0.5)
r.stop()
r.go(-10)
time.sleep(0.5)
r.go(-5)
time.sleep(0.5)
r.stop()
