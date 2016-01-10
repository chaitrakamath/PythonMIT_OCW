# FileName: ps8.py
# Author: Chaitra Kothari
# Date: Nov 9th, 2015
# Description: Implement a dynamic programming algorithm and learn how to pass functions as arguments


import time
SUBJECT_FILENAME = "subjects-test.txt"
VALUE, WORK = 0, 1


#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    resDict = {}
    for line in inputFile:
        fields = line.strip().split(',')
        name = fields[0]
        value = int(fields[1])
        work = int(fields[2])
        resDict[name] = (value, work)
    return resDict

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    # print 'sorted subnames:', subNames
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
numCallsGreedy = 0
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    global numCallsGreedy
    numCallsGreedy += 1
    totalWork = 0
    res = {}
    subNames = subjects.keys()
    subNames.sort()
    print 'subject names, sorted:', subNames
    while totalWork < maxWork:
        for subj1 in subNames:
            cmpValue = []
            for subj2 in subNames:
                if subj1 != subj2 and subj2 not in res:
                    cmpValue.append(comparator(subjects[subj1], subjects[subj2]))
            if all(cmpValue) == True: #subj1 is best of all
                totalWork += subjects[subj1][1]
                if totalWork < maxWork:
                    res[subj1] = (subjects[subj1][0], subjects[subj1][1])
    return res

print 'Number of calls to greedy advisor:', numCallsGreedy


numCallsBruteForce = 0
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    global numCallsBruteForce
    numCallsBruteForce += 1
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    print 'bestSubset:', bestSubset
    print 'bestSubsetValue:', bestSubsetValue
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            print 'subset:', subset
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue


#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    for maxWork in range(0, 60, 5):
        print 'Testing for max work:', maxWork
        start = time.time()
        print bruteForceAdvisor(subjects, maxWork)
        stop = time.time()
        elapsed = stop - start #returns time elapsed in seconds
        if elapsed <= 60:
            print 'Elapsed time:', elapsed, 'seconds'
            print
        if elapsed > 60: #return result in minutes
            elapsed = elapsed / 60
            print 'Elapsed time:', elapsed, 'minutes'
            print
        if elapsed > 3600: #return result in hours
            elapsed = elapsed / 3600
            print 'Elapsed time:', elapsed, 'hours'
            print
# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
#As we can see in the output, time elapsed follows a exponential curve which
#initially increases as maxWork increases and then levels off when maxWork is 
#equal to or greater than sum of all work values. WHen we have a big file
#with lot of rows, and maxWork is a big number, it would take a long time to 
#reach optimal values using brute force method.
#
# Problem 4: Subject Selection By Dynamic Programming
#
numCallsDynamic = 0
def dpAdvisor(subjects, maxWork):
    global numCallsDynamic
    numCallsDynamic += 1
    memo = {}
    subj = subjects.keys()
    tupleList = subjects.values()
    value = [s[0] for s in tupleList]
    work = [s[1] for s in tupleList]
    i = len(subjects) - 1
    outputSubjects = {}
    totValue, subjList = dpAdvisorHelper(subj, work, value, i, maxWork, memo)
    # print 'totalValue:', totValue
    # print 'subj', subjList
    for index in subjList:
        outputSubjects[subj[index]] = tupleList[index]
    return outputSubjects


def dpAdvisorHelper(subj, work, value, i, maxWork, memo):
    try: return memo[(i, maxWork)]
    except KeyError: 
        if i == 0:
            if work[i] <= maxWork:
                memo[(i, maxWork)] = value[i], [i]
                return value[i], [i]
            else:
                memo[(i, maxWork)] = 0, []
                return 0, []
        #compute output without taking into account ith branch
        without_i, subj_list = dpAdvisorHelper(subj, work, value, i- 1, maxWork, memo)
        if work[i] > maxWork:
            memo[(i, maxWork)] = without_i, subj_list
            return without_i, subj_list
        else: 
            with_i, subj_with_i = dpAdvisorHelper(subj, work, value, i - 1, maxWork - work[i], memo)
            with_i += value[i]
        if with_i > without_i:
            subj_list = subj_with_i + [i]
            i_value = with_i
        else:
            i_value = without_i
        memo[(i, maxWork)] = i_value, subj_list
        return i_value, subj_list

print 'Number of calls to dpAdvisor:', numCallsDynamic
#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    for maxWork in range(0, 60, 5):
        print 'Testing for max work:', maxWork
        start = time.time()
        print dpAdvisor(subjects, maxWork)
        stop = time.time()
        elapsed = stop - start #returns time elapsed in seconds
        if elapsed <= 60:
            print 'Elapsed time:', elapsed, 'seconds'
            print
        if elapsed > 60: #return result in minutes
            elapsed = elapsed / 60
            print 'Elapsed time:', elapsed, 'minutes'
            print
        if elapsed > 3600: #return result in hours
            elapsed = elapsed / 3600
            print 'Elapsed time:', elapsed, 'hours'
            print

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.