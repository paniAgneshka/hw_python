import datetime

def date_time(s):
    date_time_str = s
    data_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M:%S')
   # if datetime.datetime.now().weekday() == 6:
    #    return "Today is Sunday"
    
    if data_time_obj.time() < datetime.time(9, 30, 0):
        return "Class have not started yet"
    
    elif (data_time_obj.time() > datetime.time(11, 5, 0) and data_time_obj.time() < datetime.time(11, 15, 0)) or (data_time_obj.time() > datetime.time(12, 50, 0) and data_time_obj.time() < datetime.time(13, 40, 0)) or (data_time_obj.time() > datetime.time(15, 15, 0) and data_time_obj.time() < datetime.time(15, 25, 0)) or (data_time_obj.time() > datetime.time(17, 0, 0) and data_time_obj.time() < datetime.time(17 ,10 ,0)): 
        return "Break time!"
    
    elif (data_time_obj.time() > datetime.time(9, 30, 0) and data_time_obj.time() < datetime.time(11, 5, 0)): 
        return f"Before the end of the pair {str(datetime.datetime(data_time_obj.year, data_time_obj.month, data_time_obj.day, 11, 5, 0) - data_time_obj)}" 
    
    elif (data_time_obj.time() > datetime.time(11, 15, 0) and data_time_obj.time() < datetime.time(12, 50, 0)): 
        return f"Before the end of the pair{str(datetime.datetime(data_time_obj.year, data_time_obj.month, data_time_obj.day, 12, 50, 0) - data_time_obj)}"
    
    elif (data_time_obj.time() > datetime.time(13, 40, 0) and data_time_obj.time() < datetime.time(15, 15, 0)): 
        return f"Before the end of the pair{str(datetime.datetime(data_time_obj.year, data_time_obj.month, data_time_obj.day, 15, 15, 0) - data_time_obj)}"
    
    elif (data_time_obj.time() > datetime.time(15, 25, 0) and data_time_obj.time() < datetime.time(17 ,0 ,0)):
        return f"Before the end of the pair{str(datetime.datetime(data_time_obj.year, data_time_obj.month, data_time_obj.day, 17, 0, 0) - data_time_obj)}" 
        
    elif (data_time_obj.time() > datetime.time(17, 10, 0) and data_time_obj.time() < datetime.time(18 ,45 ,0)): 
        return f"Before the end of the pair{str(datetime.datetime(data_time_obj.year, data_time_obj.month, data_time_obj.day, 18, 45, 0) - data_time_obj)}" 
            
    elif data_time_obj.time() > datetime.time(18, 45, 0):
        return "Classes are over"
 
print(date_time("15:45:00"))
