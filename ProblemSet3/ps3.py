#File Name: ps3.py
#Author: Chaitra Kothari
#Date: Oct 29th, 2015
#Description: This problem set will introduce you to using functions and recursion, as well as string operations in Python.


from string import *


#==============================================Problem1=============================
def countSubStringMatch(target, key):
    """Function counts the number of instances of key in target
    target and key arguments should be strings"""
    assert (type(target) == str and type(key) == str), 'Please provide string values for target and key'
    curIndex = find(target, key)
    count = 0
    if curIndex == -1:
        print 'No match found'
        return count
    while curIndex != -1:
        print 'Match found'
        print 'curIndex =', curIndex
        count += 1
        curIndex = find(target, key, curIndex + 1)
    print 'Number of matches found:', count
    return count


def countSubStringMatchRecursive(target, key):
    """Function counts the number of instances of key in target
    target and key arguments should be strings""" 
    assert (type(target) == str and type(key) == str), 'Please provide string values for target and key'
    curIndex = find(target, key)
    count = 0
    #base case
    if curIndex == -1:
        if count == 0:
            print 'No match found'
        else:
            print 'Number of matches found:', count
        return count
    else: 
        count += 1
        print 'Match found'
        print 'curIndex = ', curIndex
        count = countSubStringMatchRecursive(target[curIndex + 1:], key)
        print 'Number of matches found:', count + 1
        return count + 1


def testCountSubString():
    target1 = 'atgacatgcacaagtatgcat'
    target2 = 'atgaatgcatggatgtaaatgcag'

    # key strings

    key10 = 'a'
    key11 = 'atg'
    key12 = 'atgc'
    key13 = 'atgca'

    countSubStringMatch(target1, key10)
    countSubStringMatchRecursive(target1, key10)
    raw_input()
    countSubStringMatch(target1, key11)
    countSubStringMatchRecursive(target1, key11)
    raw_input()
    countSubStringMatch(target1, key12)
    countSubStringMatchRecursive(target1, key12)
    raw_input()
    countSubStringMatch(target1, key13)
    countSubStringMatchRecursive(target1, key13)
    raw_input()
    countSubStringMatch(target2, key10)
    countSubStringMatchRecursive(target2, key10)
    raw_input()
    countSubStringMatch(target2, key11)
    countSubStringMatchRecursive(target2, key11)
    raw_input()
    countSubStringMatch(target2, key12)
    countSubStringMatchRecursive(target2, key12)
    raw_input()
    countSubStringMatch(target2, key13)
    countSubStringMatchRecursive(target2, key13)
    raw_input()


#================================================Problem2=========================================
def subStringMatchExact(target, key):
    """returns a tuple of the starting points of matches of the key string in the target string, when indexing starts at 0
    target and key should be strings"""
    assert (type(target) == str and type(key) == str), 'Please provide string values for target and key'
    curIndex = find(target, key)
    allIndex = (find(target, key), )
    if curIndex == -1:
        print 'Match not found'
    else:
        while curIndex != -1:
            curIndex = find(target, key, curIndex + 1)
            #print 'current Index:', curIndex
            if curIndex != -1:
                allIndex += (curIndex, )
    # if -1 in allIndex:
    #     lst = list(allIndex)
    #     lst.remove(-1)
    #     allIndex = tuple(lst)
    return allIndex


def testSubStringMatchExact():
    target1 = 'atgacatgcacaagtatgcat'
    target2 = 'atgaatgcatggatgtaaatgcag'

    # key strings

    key10 = 'a'
    key11 = 'atg'
    key12 = 'atgc'
    key13 = 'atgca'

    print substringMatchExact(target1, key10)
    raw_input()
    print substringMatchExact(target1, key11)
    raw_input()
    print substringMatchExact(target1, key12)
    raw_input()
    print substringMatchExact(target1, key13)
    raw_input()
    print substringMatchExact(target2, key10)
    raw_input()
    print substringMatchExact(target2, key11)
    raw_input()
    print substringMatchExact(target2, key12)
    raw_input()
    print substringMatchExact(target2, key13)
    raw_input()




#=================================================Problem3========================================
        
def constrainedMatchPair(firstMatch, secondMatch, length):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for index in firstMatch:
        if (index + length + 1) in secondMatch:
            allAnswers += (index, )
    print 'all answers from constrainedMatchPair:', allAnswers
    return allAnswers

def testConstrainedMatchPair(target, key):
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
        print
    return tuple(set(allAnswers))


target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'  

testConstrainedMatchPair(target1, key10)
raw_input()
testConstrainedMatchPair(target1, key11)
raw_input()
testConstrainedMatchPair(target1, key12)
raw_input()
testConstrainedMatchPair(target1, key13)
raw_input()
testConstrainedMatchPair(target2, key10)
raw_input()
testConstrainedMatchPair(target2, key11)
raw_input()
testConstrainedMatchPair(target2, key12)
raw_input()
testConstrainedMatchPair(target2, key13)
raw_input()

#===========================================Problem4=========================================
def subStringMatchExactlyOneSub(target, key):
    """returns tuple of indices representing matches with only one substitution
    target and key should be strings"""
    result = ()
    approxMatches = testConstrainedMatchPair(target, key)
    print 'approx matches from last function:', approxMatches
    exactMatches = subStringMatchExact(target, key)
    print 'exact matches from last function:', exactMatches
    for index in approxMatches:
        if index not in exactMatches:
            result += (index, )
    return result

def test_subStringMatchExactlyOneSub():
    target1 = 'atgacatgcacaagtatgcat'
    target2 = 'atgaatgcatggatgtaaatgcag'

    # key strings
    key12 = 'atgc'
    key13 = 'atgca'

    print subStringMatchExactlyOneSub(target1, key12)
    raw_input()
    print subStringMatchExactlyOneSub(target1, key13)
    raw_input()
    print subStringMatchExactlyOneSub(target2, key12)
    raw_input()
    print subStringMatchExactlyOneSub(target2, key13)
    raw_input()


            


