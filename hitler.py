#%% Libraries
import random
from collections import Counter


#%% Idea
"""
# for t in range(10): # float(inf)

# chancellor_id = input()
# president_id = input()
# chancellor_passed_law = input("L or F")
# disagrement = bool(input("0 or 1"))

c_id = 2
p_id = 3
passed_law = "F"
disagrement = 0

# update state given c_id := chancellor and a_vote = {L, F}
p_f_given_ad[c_id] = (p_af_given_f[c_id] * p_f[c_id]) / p_af[c_id]
print(p_f_given_ad)

# update state base on the prior and likehood give
# i = p, c, a_dis = [0, 1] and j in 0, n-1
pf[x_j] = # president
pf[x_j] = # chancellor
"""

#%%
n = 6
# Initialize prior probabilities
p_f = [2/n] * n  # Initial prior probabilities for each hypothesis
p_not_f = [1 - x for x in p_f]  # Complementary probabilities

# Likelihood of action given hypothesis f
p_af_given_f = [2/3] * n  
p_af_given_not_f = [1/3] * n  

p_af = [0] * n
p_not_af = [0] * n
for i in range(n):
    p_af[i] = p_af_given_f[i] * p_f[i] + p_af_given_not_f[i] * p_not_f[i]
    p_not_af[i] = (1 - p_af_given_f[i]) * p_f[i] + (1 - p_af_given_not_f[i]) * p_not_f[i]
    
p_f_given_af = [0] * n
for i in range(n):
    p_f_given_af[i] = (p_af_given_f[i] * p_f[i]) / p_af[i]

# Likelihood of action given hypothesis d

p_ad_given_f = [1/3] * n  
p_ad_given_not_f = [1/3] * n

p_ad = [0] * n
p_not_ad = [0] * n
for i in range(n):
    p_ad[i] = p_ad_given_f[i] * p_f[i] + p_ad_given_not_f[i] * p_not_f[i]
    p_not_ad[i] = (1 - p_ad_given_f[i]) * p_f[i] + (1 - p_ad_given_not_f[i]) * p_not_f[i]
    
p_f_given_ad = [0] * n
for i in range(n):
    p_f_given_ad[i] = (p_ad_given_f[i] * p_f[i]) / p_af[i]

def p_posteriori(p_f, is_c, p_id, ad, af):
    p_not_f = [1 - x for x in p_f]

    # update state given is_c := is chancellor and a_vote = {L, F}
    # Calculate evidence p_af for the c_id player as chancellor
    # Case AF
    for i in range(n):
        p_af[i] = p_af_given_f[i] * p_f[i] + p_af_given_not_f[i] * p_not_f[i]
        p_not_af[i] = (1 - p_af_given_f[i]) * p_f[i] + (1 - p_af_given_not_f[i]) * p_not_f[i]
    
    if af == 1: 
        p_f[p_id] = (p_af_given_f[p_id] * p_f[p_id]) / p_af[p_id] 
    else:
        p_f[p_id] = ((1 - p_af_given_f[p_id]) * p_f[p_id]) / p_not_af[p_id]

    # Case AD
    for i in range(n):
        p_ad[i] = p_ad_given_f[i] * p_f[i] + p_ad_given_not_f[i] * p_not_f[i]
        p_not_ad[i] = (1 - p_ad_given_f[i]) * p_f[i] + (1 - p_ad_given_not_f[i]) * p_not_f[i]
    
    if ad == 1: 
        p_f[p_id] = (p_ad_given_f[p_id] * p_f[p_id]) / p_ad[p_id] 
    else:
        p_f[p_id] = ((1 - p_ad_given_f[p_id]) * p_f[p_id]) / p_not_ad[p_id]
    return p_f

# Example data for multiple actions (this can be a list of actions observed)

# Function to update the probabilities
af_list =    [1, 0, 1, 0]
ad_list =    [1, 0, 1, 0]
p_ids_list = [1, 2, 1, 2]  
is_c_list =  [1, 1, 1, 1]  

# Iterate over each action to update probabilities

for af, ad, p_id, is_c in zip(af_list, ad_list, p_ids_list, is_c_list):
    print(f'af: {af:.2f}, p_id: {p_id:.2f}, is_c: {is_c:.2f}')
    p_f = p_posteriori(p_f, is_c, p_id, ad, af)
    print(f"Updated p_f after action: {[round(x, 2) for x in p_f]}")

