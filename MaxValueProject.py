from collections import defaultdict

"""Project object
    consists of number, start time, end time and value """
class project:
    def __init__(self, num, start,dur,val):
        self.num=num
        self.start=start
        self.end=dur+start
        self.val=val
# Outputs the project's information
    def output(self):
        print(self.num,"    ",self.start,"    ",self.end,"    ",self.val)


#Read function gets the name of the file
def read(filename):
    projects=[]
    numofweeks=0
    numofprojects=0
    #the file is opened and read
    file=open(filename, 'r')
    i=0
    #Its read line by line
    for line in file:
        # retrieves info from the first line
        if i==0:
            numofweeks=int(line.replace('\n',''))
        # retrieves info from the second line
        elif i==1:
            numofprojects=int(line.replace('\n',''))
        # gets the data about each project
        else:
            # splits it into 4 attributes and creates a project object
            x1,x2,x3,x4 = line.replace('\n','').split('\t')
            # which is stored in a list
            projects.append(project(int(x1),int(x2),int(x3),int(x4)))
        i+=1
    return projects, numofprojects, numofweeks


# maximize function finds the maximum value and the path of the projects sent
def maximize(projects, numofprojects):
    project_history = defaultdict(list)
    projects.sort(key=lambda p: p.end, reverse=False)
    prlist = [0]*numofprojects
    prlist[0]=projects[0].val
    i=1
    for p in projects[1:]:
        prlist[i]=max(p.val,prlist[i-1])
        for n in range(i-1,-1,-1):
            if projects[n].end <= p.start:
                prlist[i]=max(prlist[i], (p.val+prlist[n]))
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











