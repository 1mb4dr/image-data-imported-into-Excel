import csv

with open('data.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    list_of_list = []
    j=0
    lines = [line for line in spamreader]
    for i in range(len(lines)):
        list_ = []
        if(len(lines)<=i+j):
            break;
        first = lines[i+j][0]
        while(first == lines[i+j][0]):
            list_.append(lines[i+j][2])
            j+=1
            if(len(lines)<=i+j):
                break;
        j-=1
        list_of_list.append(list(map(float,list_)))

#maxlen = len(max(list_of_list))
#print("\t"+"\t".join([str(el) for el in range(1,maxlen+1)])+"\n")
#for i in range(len(list_of_list)):
 #   print(str(i+1)+"\t"+"\t".join([str(el) for el in list_of_list[i]])+"\n")
    
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list_of_list)