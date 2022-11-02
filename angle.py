
class Angle:
    def __init__(self, deg, minute, sec):
        all_sec = 3600* deg + 60 * minute + sec
        full_circles = int(all_sec/(360*60*60))
        all_sec -= full_circles * 360 * 60 * 60
        self.deg = int(all_sec/3600)
        self.minute = int((all_sec - 3600* self.deg)/60)
        self.sec = all_sec - self.deg * 3600 - self.minute * 60
    
    def __str__(self):
        return f'{self.deg}:{self.minute}:{self.sec}'    

    def __add__(self, other):
        return Angle(self.deg + other.deg, self.minute + other.minute, self.sec + other.sec)
    
    def __sub__(self, other):
        return Angle(self.deg - other.deg, self.minute - other.minute, self.sec - other.sec)  
    
    def __lt__(self, other):
        val1=3600* self.deg + 60 * self.minute + self.sec
        val2=3600* other.deg + 60 * other.minute + other.sec
        if val1 < val2:
            return True
        else:
            return False    
    
    def __gt__(self, other):
        val1=3600* self.deg + 60 * self.minute + self.sec
        val2=3600* other.deg + 60 * other.minute + other.sec
        if val1 > val2:
            return True
        else:
            return False
    
    def __le__(self, other):
        val1=3600* self.deg + 60 * self.minute + self.sec
        val2=3600* other.deg + 60 * other.minute + other.sec
        if val1 <= val2:
            return True
        else:
            return False
    
    def __ge__(self, other):
        val1=3600* self.deg + 60 * self.minute + self.sec
        val2=3600* other.deg + 60 * other.minute + other.sec
        if val1 >= val2:
            return True
        else:
            return False
    
    def __eq__(self, other):
        val1=3600* self.deg + 60 * self.minute + self.sec
        val2=3600* other.deg + 60 * other.minute + other.sec
        if val1 == val2:
            return True
        else:
            return False
    
    def __ne__(self, other):
        val1=3600* self.deg + 60 * self.minute + self.sec
        val2=3600* other.deg + 60 * other.minute + other.sec
        if val1 != val2:
            return True
        else:
            return False  
    def __abs__(self):
        all_sec=abs(3600* self.deg + 60 * self.minute + self.sec)
        self.deg = int(all_sec/3600)
        self.minute = int((all_sec - 3600* self.deg)/60)
        self.sec = all_sec - self.deg * 3600 - self.minute * 60
    
        return Angle(self.deg, self.minute, self.sec)
              
def up_culm(self, lat):  
    if abs(lat) < abs(self):
        return Angle(90, 0, 0) - self + lat
    else:
        return Angle(90, 0, 0) - lat + self     
    
def low_culm(self, lat):
    return lat+self - Angle(90, 0, 0)            
        
phi = Angle(59, 57, 71)
delta = Angle(-16, -42, -58)

print(str(up_culm(delta, phi)))
print(str(low_culm(delta, phi)))


