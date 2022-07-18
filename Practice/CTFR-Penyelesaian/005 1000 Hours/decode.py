# open file
func=open("func.txt","r")
# split it with \n
func_list=func.read().split("\n")
new_list=[]
# remove len 0 to 31 and store it in new list
for a in range(len(func_list)):
    b=func_list[a][36:]
    if len(b)>0:
        new_list.append(b)
# short it with sorting algorithm
new_list=sorted(new_list)
# sorting the number behind ')' and print new_list[a]
for a in range(len(new_list)):
    b=new_list[a].split(")")
    new_list[a]=b[0]
# make new_list[a] to int
for a in range(len(new_list)):
    new_list[a]=int(new_list[a])
new_list=sorted(new_list)
#for i in range(len(new_list)):
#    print(str(new_list[i])+"\n")
file=open("func.txt","r")
file=file.read()
var_decode=[]
for i in new_list:
    # if there exist text i shomewhere in file_list
    if file.find(str(i))!=-1:
        # find the text and store it in var_decode
        print(file[file.find(str(i))+29:file.find(str(i))+30],end="")
#file_run=open("run.txt","r")
#file_run=file_run.read().replace("();","")
#file_run=file_run.split("\n")
#true_decode=[]
#for i in file_run:
#    # if there exist text i shomewhere in file_list
#    if file.find(str(i))!=-1:
#        # find the text and store it in var_decode
#        print(file[file.find(str(i)):file.find(str(i))+60])
#var_num=0
#for i in true_decode:
#    print(true_decode[var_num][true_decode[var_num].find("'")+1:true_decode[var_num].find(str("'"))+2],end="")
#    var_num+=1