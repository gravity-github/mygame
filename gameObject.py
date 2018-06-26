class gameObject:
    def __init__(self,name='object',health=100):
        self.property = {'name':name,'health':health}
    
    def add_property(self,property,value):
        self.property[property] = value
        