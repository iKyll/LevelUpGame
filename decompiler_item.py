import json
import sys
import os

items = {'swords': 
            {'wooden_sword': 1,
             'stone_sword': 2, 
             'long_sword': 5}, 
        'helmets': 
            {'wooden_helmet': 2, 
            'steel_helmet': 5}, 
        'chestplates': 
            {'wooden_chestplate': 2, 
            'steel_chestplate': 5}, 
        'leggings': 
            {'wooden_leggings': 2, 
            'steel_leggings': 5}, 
        'boots':
            {'wooden_boots': 2, 
            'steel_boots': 5}, 
        'rings': 
            {'steel_ring': 2, 
            'jeweled_ring': 5},
        'collars': {
            'steel_collar': 2,
            'jeweled_collar': 5,}
        }

writer_data = open(os.path.join(sys.path[0], "items_id.txt"), "w")
writer_data.write(json.dumps(items))