class gameObject:
    def __init__(self,name='object'):
        self.property ={'name':name,'health':100,'point':0}
        self.position = {'x':None,'y':None}
        self.velocity = {'vx':None,'y':None}
    
    def set_position(self,x=0,y=0):
        self.position['x'],self.position['y'] = x,y 
    
    def set_velocity(self,vx=0,vy=0):
        self.velocity['vx'],self.velocity['vy'] = vx,vy
