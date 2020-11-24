#UTF-8
def objects(map_number, mode):
    if mode == 'stoper':
        adres = 'data/stoper/stoper' + str(map_number[0]) + '_' + str(map_number[1]) + '.txt'
        try: file = open(adres)
        except FileNotFoundError:
            return False
        else:
            stop_kords = file.read().split('_')
            return stop_kords