def mid(mo):
    count = len(mo)
    if (count % 2) != 0:
        for i,c in enumerate(mo):
            if i == (((len(mo) -1)/2)):
                return(c)
    else:
        print("")
        
print(mid("1 2 3 4 5"))