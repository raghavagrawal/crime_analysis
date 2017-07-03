import csv
f=open("guns.csv","r")
read=csv.reader(f)
view = list(read)
for elem in view[:20]:
    print(elem,"\n") 
