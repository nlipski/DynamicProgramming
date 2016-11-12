class project:
    def __init__(self, num, start,dur,val):
        self.num=num
        self.start=start
        self.end=dur+start
        self.val=val

    def output(self):
        print(self.num,"    ",self.start,"    ",self.end,"    ",self.val)

def read(filename):
    projects=[]
    numofweeks=0
    numofprojects=0
    file=open(filename, 'r')
    i=0
    for line in file:
        if i==0:
            numofweeks=int(line.replace('\n',''))
        elif i==1:
            numofprojects=int(line.replace('\n',''))
        else:
            x1,x2,x3,x4 = line.replace('\n','').split('\t')
            projects.append(project(int(x1),int(x2),int(x3),int(x4)))
        i+=1
    return projects, numofprojects, numofweeks

def maximize(projects, numofprojects):
    projects.sort(key=lambda p: p.end, reverse=False)
    prlist = [0]*numofprojects
    prlist[0]=projects[0].val
    i=1
    for p in projects[1:]:
        prlist[i]=max(p.val,prlist[i-1])
        for n in range(i-1,0,-1):
            if projects[n].end <= p.start:
                prlist[i]=max(prlist[i],p.val+prlist[n])
                break
        i+=1
    MaxVal=max(prlist)
    return MaxVal

projects, numofprojects, numofweeks = read('test1.txt')
maxVal=maximize(projects, numofprojects)
print("Test1.txt results: ",maxVal)

projects, numofprojects, numofweeks = read('test2.txt')
maxVal=maximize(projects, numofprojects)
print("Test2.txt results: ",maxVal)

projects, numofprojects, numofweeks = read('test3.txt')
maxVal=maximize(projects, numofprojects)
print("Test3.txt results: ",maxVal)

projects, numofprojects, numofweeks = read('test4.txt')
maxVal=maximize(projects, numofprojects)
print("Test4.txt results: ",maxVal)










