# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 11:19:47 2017

@author: Anjali Kumari
"""
    
numberOfQuestion= []  # to store total question in a contest
run= True

# to get minimum prime factor
def minPrime(N):
    for number in range(2,N):
        if N%number==0:
            return number
            break
        
    return N
 
while run:
    try:
        print "Input:"
        numberOfContest =int( raw_input())
        for i in range(numberOfContest):
            TotalQuestion= int(raw_input())
            numberOfQuestion.append(TotalQuestion)
        print "Output:"    
        for i in range(numberOfContest):
            value = numberOfQuestion[i]
            QuestionSolvedByHerbal= minPrime(value)
            print   value-QuestionSolvedByHerbal,QuestionSolvedByHerbal
            
    except ValueError:
        print "Not an integer"
    run=False


    
 
