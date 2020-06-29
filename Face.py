import pyscreenshot
import datetime
import time

time.sleep(3)  #Why Delay??
im = pyscreenshot.grab()
im.save('screenshot-' + str(datetime.datetime.now()) + '.png')
im.show()
