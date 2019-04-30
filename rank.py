#!/bin/python3

import math
import os
import random
import re
import sys
global expenditureTrack
def counting_sort(expenditure, max_val):
    m = max_val + 1
    count = [0] * m                
    for a in expenditure:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for _ in range(count[a]):
            expenditure[i] = a
            i += 1
    return expenditure

def counting_sort_median(expenditure, max_val, d):
    print('array was:', expenditure)
    m = max_val + 1
    count = [0] * m                
    medianPosition = d//2
    isEven = (d % 2) == 0
    median = 0
    otherEvenNumber = 0
    for a in expenditure:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for _ in range(count[a]):
            if i == medianPosition-1:
                otherEvenNumber = a
            if i == medianPosition:
                if isEven:
                    median = a + otherEvenNumber
                else:
                    median = a
            expenditure[i] = a
            i += 1
    print('the sorted array is now:', expenditure)
    return median

def activityNotifications(expenditure, d):
    notice = 0
    expenditureTrack = []
    trailingExpenditures = []
    previousMedian = None

    for todaysExpenditureIndex in range(d, len(expenditure)):
        firstLook = False
        if todaysExpenditureIndex == d:
            firstLook = True
            expenditureTrack = getTrailingExpense(expenditure, d, todaysExpenditureIndex, firstLook, previousMedian)
            trailingExpenditures = expenditureTrack
        else:
             trailingExpenditures = getTrailingExpense(expenditure, d, todaysExpenditureIndex, firstLook, previousMedian, expenditureTrack)
        todaysExpenditure = expenditure[todaysExpenditureIndex]
        medianValues = getMedianValue(trailingExpenditures, d, firstLook, previousMedian)
        medianValue = medianValues[0]
        previousMedian = medianValues[1]
        if todaysExpenditure >= medianValue:
            notice +=1
    return notice

def getTrailingExpense(expenditure, d, todaysExpenditureIndex, firstLook, previousMedian, expenditureTrack=[]):
    if firstLook:
        expenditureTrack = expenditure[todaysExpenditureIndex - d : todaysExpenditureIndex]
    else:
        del expenditureTrack[0]
        half_list = d//2
        if expenditure[todaysExpenditureIndex - 1] < previousMedian:
            sort_half_list = expenditureTrack[0:half_list]
            otherHalf = expenditureTrack[half_list:d]
            sort_half_list.append(expenditure[todaysExpenditureIndex - 1])
            expenditureTrack = counting_sort(sort_half_list, 10000)
            print('this is the previous median:', previousMedian)

            print('todays exp index:', expenditure[todaysExpenditureIndex - 1])
            expenditureTrack.extend(otherHalf)
        else:
            sort_half_list = expenditureTrack[half_list:d]
            otherHalf = expenditureTrack[0:half_list]
            sort_half_list.append(expenditure[todaysExpenditureIndex - 1])
            expenditureTrack = counting_sort(sort_half_list, 10000)
            print(expenditureTrack, otherHalf)
            expenditureTrack.extend(otherHalf)
    print(expenditureTrack, firstLook)
    return expenditureTrack

    

def getMedianValue(expenditure, d,  firstLook, previousMedian):
    medianPosition = d//2
    isEven = (d % 2) == 0
    if firstLook:
        median = counting_sort_median(expenditure, 100000, d)
        previousMedian = median
    else:
        if isEven:
            median = expenditure[medianPosition] + expenditure[medianPosition-1]
        else:
            median = expenditure[medianPosition]

    return (median * 2, previousMedian)
