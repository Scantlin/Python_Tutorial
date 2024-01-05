class median:
    def mid(self, mo):
        self.mo = mo
        count = len(mo)
        if (count % 2) != 0:
            for i,c in enumerate(self.mo):
                if i == (((len(self.mo) -1)/2)):
                    return f"The median is {(c)}"
        else:
            return f"No median: {len(self.mo)}"
        
how_many =int(input("how many numbers in median: "))        
med = []
print("Enter all numbers: ")
for i in range(how_many):
    me = int(input())
    med.insert(i, me)

xe = median()
print((xe.mid(med)))