class gameObject:
    def __init__(self):
        self.property = {'name':'object','health':100,'point':0} 
        self.position = {'x':None,'y':None} 
        self.velocity = {'vx':None,'vy':None} 

    def set_position(self,x=0,y=0):
        self.position['x'],self.position['y'] = x,y 
        