class Hesabla:
    def list(self):
        return [2,4,6,8,10]


    def sum(self, num):
        listt = self.list()
        return [(i, j) for i in range(len(listt)) for j in range(i + 1, len(listt)) if listt[i] + listt[j] == num]



hesab = Hesabla()
lists = hesab.list()
print(f"List: {lists}")
num = int(input("Ededi daxil edin: ")) 
cut = hesab.sum(num)
if cut:
    for c in cut:
       print(f"{num} ededi listdeki {c[0]}, {c[1]} index'li ededlerin cemidir")
else:
    print(-1)