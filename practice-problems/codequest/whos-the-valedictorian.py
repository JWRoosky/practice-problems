cases = int(input())
for i in range(cases):
    schls = []
    stdnts = []
    schl = input()
    numStudents = int(input())
    valedictorians = []
    for j in range(numStudents):
        studentInfo = input()
        stdnts.append(studentInfo)
    for j in range(len(stdnts)):
        colon = stdnts[j].index(':')
        name = stdnts[j][0:colon]
        grades = stdnts[j][colon:-1]
        grds = grades.split(',')
        for k in range(len(grds)):
            grds[k]
