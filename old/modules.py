#UTF-8
def objects_data(map_number, mode, save_meta1):
    if mode == 'stoper':
        adres = 'data/stoper_old/stoper' + str(map_number[0]) + '_' + str(map_number[1]) + '.frls'
        try: file = open(adres)
        except FileNotFoundError:
            return ['']
        else:
            file = open(adres, 'rb')
            stop_cords = save_meta1.decrypt(file.read()).decode('utf8').strip().split('+')
            return stop_cords
        
        
    elif mode == 'objects':
        adres = 'data/objects_old/objects' + str(map_number[0]) + '_' + str(map_number[1]) + '.frls'
        try: file = open(adres)
        except FileNotFoundError:
            return [['']]
        else:
            file = open(adres, 'rb')
            objects = []
            temp1 = save_meta1.decrypt(file.read()).decode('utf8').strip().split('+')
            for temp2 in temp1:
                objects.append(temp2.split('_'))
        return objects
    
    



def stoper(x_object, y_object, side, stop_cords=False):
    if stop_cords != False and stop_cords != ['']:
        stop = True
        if side == 0:
            for i in stop_cords:
                if i == '': continue
                temp = i.split('_')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 50 >= x1 and x_object + 10 <= x2 and y_object + 59 >= y1 and y_object + 33 <= y2:
                    stop = False
                    
        if side == 1:
            for i in stop_cords:
                if i == '': continue
                temp = i.split('_')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 50 >= x1 and x_object + 10 <= x2 and y_object + 50 >= y1 and y_object + 30 <= y2:
                    stop = False


        
        if side == 2:
            for i in stop_cords:
                if i == '': continue
                temp = i.split('_')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 53 >= x1 and x_object + 10 <= x2 and y_object + 50 >= y1 and y_object + 33 <= y2:
                    stop = False



        if side == 3:
            for i in stop_cords:
                if i == '': continue
                temp = i.split('_')
                x1 = int(temp[0])
                y1 = int(temp[1])
                x2 = int(temp[2])
                y2 = int(temp[3])
                if x_object + 50 >= x1 and x_object + 7 <= x2 and y_object + 50 >= y1 and y_object + 33 <= y2:
                    stop = False       
        return stop
    else: return True


    
    
    
    
    
    
    
    
    