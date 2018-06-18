import time 
import threading
class gameEngine(threading.Thread):
    def __init__(self,frame=24):
        threading.Thread.__init__(self)
        self.current_status=None 
        self.frame = frame
    
    def update(self):
        
        pass 

    def run(self):
        t1 = t2 = time.time()
        max_time = 1/ self.frame
        while self.current_status != 'stop':
            t2=time.time()
            dt = t2-t1 
            if dt >= max_time:
                self.update()