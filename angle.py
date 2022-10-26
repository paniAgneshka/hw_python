
class Angle:
    def __init__(self, deg, minute, sec):
        all_sec = 3600* deg + 60 * minute + sec
        full_circles = int(all_sec/(360*60*60))
        all_sec -= full_circles * 360 * 60 * 60
        if all_sec < 0:
            all_sec += 360 * 60 * 60
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
        
ang1 = Angle(361, 20, 71)
ang2 = Angle(1, 20, 81)
ang3 = ang1-ang2
ang1<ang2
print(str(ang1<ang2))
