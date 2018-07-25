gpa = {15 : [98, 100], 14 : [94, 97], 13 : [92, 93], 12:[90, 91], 11:[86, 89], 10:[84, 85], 9:[82, 83], 8:[78, 81], 7:[76, 77], 6:[74, 75], 5:[72, 73], 4:[70, 71]}

def allappend(gradescores, appendlist):
    for i in gradescores:
        appendlist.append(i)
    return appendlist

def getgrades(subject):
    newgrade = None
    while newgrade == None:
        try:
            newgrade = int(input('Please enter your %s grade: ' % subject))
        except ValueError:
            print('\nNot valid\n')
            newgrade = None
    return newgrade

def testGPA(grade):
    curgpa = 0
    for i in range(4, 16):
        if gpa[i][0] <= grade <= gpa[i][1]:
            curgpa = i
    if curgpa == 0:
        raise ValueError('Your grade is too low or too high on the GPA Scale.')
    return curgpa

def roundnum(floatnum):
    intnum = int(floatnum)
    if floatnum - float(intnum) >= 0.5:
        return intnum + 1
    else:
        return intnum

# Get Averages and Calculate
print('Enter your final grades.\n')

reading = getgrades('literacy')
testread = testGPA(reading)
writing = getgrades('writing')
testwrite = testGPA(writing)
readwrite = testGPA(roundnum((reading+writing)/2))
math = testGPA(getgrades('math'))
ss = testGPA(getgrades('social studies'))
science = testGPA(getgrades('science'))

finals = (readwrite+math+ss+science)/4

print('Your total gpa is: ', finals)