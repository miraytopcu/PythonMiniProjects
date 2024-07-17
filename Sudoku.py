# her satırda 1 2 3 4 5 6 7 8 9
# her sütunda 1 2 3 4 5 6 7 8 9 
# her 9luk karede 1 2 3 4 5 6 7 8 9 

def tablo():
    for i in range(9):
        for j in range(9):
            print("{:3}".format("_"), end = " ")
        print()

tablo()