#UTF-8
def stoper(map_number, x_hero, y_hero, side):
    stop = True
    adres = 'data/stoper/stoper' + str(map_number[0]) + '_' + str(map_number[1]) + '.txt'
    try: file = open(adres)
    except FileNotFoundError:
        return True
    else:
        for line in file:
            if side == 0:
                stop_kords = line.split('_')
                for i in stop_kords:
                    temp = i.split(' ')
                    x1 = int(temp[0])
                    y1 = int(temp[1])
                    x2 = int(temp[2])
                    y2 = int(temp[3])
                    if x_hero + 48 >= x1 and x_hero + 2 <= x2 and y_hero + 52 >= y1 and y_hero + 28 <= y2:
                        stop = False
                        
            if side == 1:
                stop_kords = line.split('_')
                for i in stop_kords:
                    temp = i.split(' ')
                    x1 = int(temp[0])
                    y1 = int(temp[1])
                    x2 = int(temp[2])
                    y2 = int(temp[3])
                    if x_hero + 48 >= x1 and x_hero + 2 <= x2 and y_hero + 38 >= y1 and y_hero + 24 <= y2:
                        stop = False
    
    
            
            if side == 2:
                stop_kords = line.split('_')
                for i in stop_kords:
                    temp = i.split(' ')
                    x1 = int(temp[0])
                    y1 = int(temp[1])
                    x2 = int(temp[2])
                    y2 = int(temp[3])
                    if x_hero + 50 >= x1 and x_hero - 2 <= x2 and y_hero + 38 >= y1 and y_hero + 28 <= y2:
                        stop = False
    
    
    
            if side == 3:
                stop_kords = line.split('_')
                for i in stop_kords:
                    temp = i.split(' ')
                    x1 = int(temp[0])
                    y1 = int(temp[1])
                    x2 = int(temp[2])
                    y2 = int(temp[3])
                    if x_hero + 45 >= x1 and x_hero - 2 <= x2 and y_hero + 38 >= y1 and y_hero + 28 <= y2:
                        stop = False
        file.close()        
        return stop
    
    
    
    
    
    
    
    
    
    
    