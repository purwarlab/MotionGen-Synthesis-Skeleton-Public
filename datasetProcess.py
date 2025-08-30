import json
import numpy as np
import os


"""
    The code below reads the dictionary of the kinematic structures. 
    The dictionary saves the predefined kinematic structures which is mentioned in our dataset paper: 

    A Dataset of 3M Single-DOF Planar 4-, 6-, and 8-Bar Linkage Mechanisms With Open and Closed Coupler Curves for Machine Learning-Driven Path Synthesis

"""

# Open the JSON file in read mode
with open('BSIdict_468.json', 'r') as file:
    # Load the JSON data into a Python dictionary
    BSIdict_468 = json.load(file) 

with open('KV_468.json', 'r') as file2:
    # Load the JSON data into a Python dictionary
    mechStackKV = json.load(file2)

with open('VK_468.json', 'r') as file3:
    # Load the JSON data into a Python dictionary
    mechStackVK = json.load(file3)


four_bar = ['RRRR', 'RRRP', 'RRPR', 'PRPR'] 
six_bar  = ['Watt1T1A1', 'Watt1T2A1', 'Watt1T3A1', 'Watt1T1A2', 'Watt1T2A2', 'Watt1T3A2', 
            'Watt2T1A1', 'Watt2T2A1', 'Watt2T1A2', 'Watt2T2A2', 'Steph1T1', 'Steph1T2',
            'Steph1T3', 'Steph2T1A1', 'Steph2T2A1', 'Steph3T1A1', 'Steph3T2A1', 'Steph3T1A2', 
            'Steph3T2A2', 'Steph2T1A2', 'Steph2T2A2']
eight_bar = list(set(mechStackKV.keys()) - set(four_bar) - set(six_bar))

watt1 = ['Watt1T1A1', 'Watt1T2A1', 'Watt1T3A1', 'Watt1T1A2', 'Watt1T2A2', 'Watt1T3A2']
watt2 = ['Watt2T1A1', 'Watt2T2A1', 'Watt2T1A2', 'Watt2T2A2']
steph1= ['Steph1T1', 'Steph1T2', 'Steph1T3'] 
steph2= ['Steph2T1A1', 'Steph2T2A1', 'Steph2T1A2', 'Steph2T2A2']
steph3= ['Steph3T1A1', 'Steph3T2A1', 'Steph3T1A2', 'Steph3T2A2']


# Get the corresponding mechanism after query, if you build any dataset and find the configuartion from it.  
def getMech(pN = np.zeros((5, 2)), mechKey = "RRRR", BSIdict = BSIdict_468, vk = mechStackVK, saveToLocal = False): 
    # pN is one point config for the kinematic structure. 
    # mechKey is a string. For example, "RRRR". BSIdict saves the constraint graph for the kinematic structure. 
    # feel free to use other kinematic structures that are not in the dictionary. As long as its matrices follows the definition, it will be correctly displayed. 

    BSIpc = {
            "B": BSIdict[mechKey]['B'],
            "S": BSIdict[mechKey]["S"],
            "I": BSIdict[mechKey]["I"],
            "p": pN.tolist(),
            "c": BSIdict[mechKey]["c"],

    }
    
    if saveToLocal: # if you want to test and save the sample locally. 
        file_path = './sample.json'
        # Open the file in write mode and write the data
        with open(file_path, 'w') as file:
            json.dump(BSIpc, file)  # 'indent=4' makes the output pretty-printed
    
    return BSIpc