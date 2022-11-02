class Robot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = [[x, y]]
        
    
    def move_up(self, shift):
        self.y += shift
        self.path.append([self.x, self.y])
    
    def move_down(self, shift):
        self.y -= shift
        self.path.append([self.x, self.y])
    
    def move_left(self, shift):
        self.x -= shift
        self.path.append([self.x, self.y])    
    def move_right(self, shift):    
        self.x += shift
        self.path.append([self.x, self.y])
    def show(self):
        return [print(i) for i in self.path]
    def load(self):
        f= open('curr_posit.txt', 'r+')
        self.x=f.readline()
        self.y=f.readline()
        self.path = [[self.x, self.y]]

        f.close
    def save(self):   
        f= open('curr_posit.txt', 'w+')
        x = self.path[-1][0]
        y = self.path[-1][1]
        f.writelines(str(x) \n)
        f.writelines(str(y))
        f.close
cat = Robot(-1, 5)
cat.move_down(7)
cat.move_left(5)
cat.move_up(1)
cat.move_right(4)
cat.show()
cat.save()
