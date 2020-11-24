#UTF-8
def stoper(x_object, y_object, side, stop_kords=False):
    if stop_kords != False:
        stop = True
        if side == 0:
            for i in stop_kords:
                temp = i.split(' ')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 48 >= x1 and x_object + 2 <= x2 and y_object + 52 >= y1 and y_object + 28 <= y2:
                    stop = False
                    
        if side == 1:
            for i in stop_kords:
                temp = i.split(' ')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 48 >= x1 and x_object + 2 <= x2 and y_object + 38 >= y1 and y_object + 24 <= y2:
                    stop = False


        
        if side == 2:
            for i in stop_kords:
                temp = i.split(' ')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 50 >= x1 and x_object + 40 <= x2 and y_object + 38 >= y1 and y_object + 28 <= y2:
                    stop = False



        if side == 3:
            for i in stop_kords:
                temp = i.split(' ')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 45 >= x1 and x_object <= x2 and y_object + 38 >= y1 and y_object + 28 <= y2:
                    stop = False       
        return stop
    else: return True


    
    
    
    
    
    
    
    
    