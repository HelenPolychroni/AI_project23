import random
import numpy as np
import math
from itertools import combinations
import operator
from collections import OrderedDict

def parents_pairs(list1):
    '''
    All possible pairs in list
    Using combinations()
    '''
    l = list(combinations(list1, 2))
    return(l)


def single_point_crossover(pairs, dict):
    '''
    Crossover 
    Single Point Crossover
    
    16 colors - > split the sequence in 8 and 8 colors
    '''
    
    num_of_children = len(pairs) * 2
    c = 16
    children_table = [[0] * c for _ in range(num_of_children)]
    
    l = 0
    for k in range(len(pairs)):
        t1 = dict[pairs[k][0]]
        t2 = dict[pairs[k][1]]
        children_table[l] = t1[:8] + t2[8:] 
        children_table[l+1] = t2[:8] + t1[8:]
        l+=2

    return(children_table)


def roulette_wheel_selection(scores, r): # with dictionary
    '''
    Selection
    Roulette-Wheel Selection for Partial Renewal
    '''
    
    # find the sum of dictionary's values
    print("Sum of all dictionary values is: ",sum(scores.values()))
    
    l = []
    for i in range(0,r):
        l.append(random.randint(0, sum(scores.values())))

    
    #print("\nl is: ",l)
    print("\n")
    
    keys = list(scores.keys())
    values = list(scores.values())
    
    l1 = [] 
    for i in range(0,r): # l list
        j = 0
        sum1 = 0
        if l[i] <= values[j]: 
            l1.append(keys[j])
        elif (l[i] > values[j]):
            sum1 = values[j] + values[j+1]
            
            j = 1
            while sum1 < l[i] and j < r-1:
                    sum1 += values[j+1]
                    j+=1
            l1.append(keys[j])
    
    # remove the duplicates elements
    res = [*set(l1)]

    return(res)


def find_scores(dict):
    scores = {}
    for i in range(0,p): # N adjacency matrix row 
        score = 0
        for j in range(0,16): # N adjacency matrix column
            for k in range(0,16): # dictionary
                if N[j][k] == 1:  # neighbor
                    if dict[i][j] != dict[i][k]: # different color neighbor
                        score+=1
                else:
                    continue
        scores[i] = score
    return(scores)


# ------------------------------------------------------------ MAIN -------------------------------------------------------------------------------   
'''
Adjacency Matrix
'''
N = [[0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1],
     [1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1],
     [1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
     [1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0],
     [0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0],
     [0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,0],
     [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0],
     [0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
     [0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0],
     [0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0],
     [0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0],
     [0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0],
     [1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0],
     [0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0],
     [1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
     [1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0]]


'''
Creating the population
'''
p = 20 # initial population
print("\nPopulation is: ", p)
colors = ['blue','red','green','yellow'] # 4 available colors
print("Available colors are: ", colors)

n = 16
dict = {}
for i in range(0,p):
    colors_list = []
    for j in range(0,n):
        colors_list.append(random.choice(colors))
    dict[i] = colors_list
    
print("\nRandom population in Dictionary: ")
for k, v in dict.items():
    print(k, v)



# counting the best score
best_score = 0
for i in range(n):
    for j in range(n):
        if N[i][j] == 1:
            best_score += 1

#print("\nBest score is: ", best_score)



# apo edw xekinaei to repeat!!!!!!!!!!!

repetitions = 0
flag1 = False

while (repetitions < 30 or flag1 == False):
    
    scores_d = find_scores(dict)
    print("\nScores of random population in dictionary:")
    print(scores_d)
    
    b = {}
    for i in range(p):
        if (best_score - scores_d[i]) <= 7:
            v = best_score - scores_d[i]
            b[i] = v
            flag1 = True
            break
    
    if flag1: 
        # print("\nTermination because of best score.")
        break
    
    
    '''
    Merikh Ananewsh
    Merikh ananewsh plhthismoy -> 30% diastavrwsh
    '''
    r = 0.3 * p  # partial population e.g 30% population
    print("\nPartial popluation r is ",int(r)) 
    
    d = {}
    for i in range(int(r)):
        flag = False
        while flag == False:
            # choose them randomly
            k = random.randint(0, p-1) # generate a number between 0 and p-1 (both included)
            if k not in d.keys():
                v = scores_d[k]
                d[k] = v
                flag = True
    
    print("\nPartial scores in dict are: ",d)
    # aytoi tha ginoun goneis, tha kanoun paidia kai tha enwthoun me toys allous -> thn previous generation
    
    
    keysList = list(d.keys())
    #print("Keys are: ",keysList)
    
    flag = False
    while (flag == False):
        parents = roulette_wheel_selection(d, int(r))
        if (len(parents) >= 1): 
            flag = True
    
    print("Parents are: ",parents)
    
    pairs = parents_pairs(parents) # pair of parents
    print("Pair of parents are: ",pairs)
    print("\nNumber of parents pairs is: ",len(pairs))

    
    flag = False
    while flag == False:
        if (len(pairs)//2 + 1) < r-1:
            num_of_p_pairs = random.randint(len(pairs)//2 + 1 , r-1)
        else:
            num_of_p_pairs = random.randint(r-1, len(pairs)//2)
            
        if (num_of_p_pairs <= len(pairs)):
            flag = True
    print("Final number of pairs is: ",num_of_p_pairs)   
    
    # prepei na dialexw etsi ta zevgaria wste na simperilambanontai oloi oi komvoi
    pairs_f = []
    
    for i in range(num_of_p_pairs):
        pair = random.choice(pairs)
        pairs_f.append(pair)
        pairs.remove(pair)
        
    if not all([x in parents for x in pairs_f[i] for i in range(len(pairs_f))]): # ckeck if all numbers are in pairs list
        print("Not all parents case!")
    
    print("Final pairs",pairs_f)
    
    # make children from these pairs of parents
    children_table = single_point_crossover(pairs_f, dict)
    
    print("\nChildren's table  is:")
    for child in children_table:
        print(child)
        
    print("\nNumber of children is: ",len(children_table))
    
    
    # NOW deal with the rest population
    # choose randomly some of them to pass to the new generation
    untouching_population = [[0] * (n) for _ in range(p - len(children_table))]
    for i in range(p - len(children_table)):
        flag = False
        while flag == False:
            k = random.randint(0, p-1) 
            if k not in untouching_population:
                untouching_population[i] = dict[k]
                flag = True
    
    print("\nRest population is: ")
    for r in untouching_population:
        print(r)
        
    
    # merge the 2 populations
    dict = {}
    i = 0
    
    for child in children_table:
        v = child
        dict[i] = v
        i+=1
    for j in untouching_population:
        v = j
        dict[i] = v
        i+=1
    
    print("\nMerged dictionary is: ")   
    for k, v in dict.items():
        print(k, v)      
    
    
    '''
    Mutation 
    - change list item color 
    - affects 10% of the population
    '''
    
    # metallaxh enos psifioy e.g sto 10% tou population
    n1 = 0.1 * p 
    
    for i in range(int(n1)):  # afhnoume to endehoemno na pathei metallaxh xana to idio stoiheio
        k = random.randint(0, p - 1) # random key
        v = random.randint(0, n - 1) # random value index
        
        flag = False
        while flag == False:
            new_color = random.choice(colors)
            if new_color is not dict[k][v]:
                dict[k][v] = new_color
                flag = True
    
    print("\nAfter mutation dictionary is: ")   
    for k, v in dict.items():
        print(k, v)   
        
        
    repetitions+=1

# end of loop
print("\nBest score of all is: ", best_score)

if flag1: 
    print("Termination because of best score.")
    if (len(b.keys()) > 1): # more than one best scores
        sorted_dict = sorted(b.items(), key=lambda x:x[1])
        best = dict[sorted_dict[0][0]]
        b_score = scores_d[sorted_dict[0][0]]
    else: # one best score
        best = dict[list(b.keys())[0]]
        b_score = scores_d[list(b.keys())[0]]
    print("\nBest graph colouring solution(s) is/are: ", best)
    print("With score(s): ", b_score)

else:
    print("Termination because of repetitions")
    print("\nFinal population: ")
    for k, v in dict.items():
        print(k, v)  
        
    scores_d = find_scores(dict)
    print("\nFinal population's scores are:")
    print(scores_d) 















