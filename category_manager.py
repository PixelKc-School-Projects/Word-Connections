"""
Category Manager Module
Handles loading categories from file and creating word-to-category lookup dictionary.
"""

import os


def load_categories(filename):
    """
    Load categories from a text file and build a dictionary.
    
    Args:
        filename (str): Name of the categories text file (will be found in script's directory)
        
    Returns:
        dict: Dictionary mapping category names to lists of words
              Example: {"fruits": ["apple", "banana", "cherry", "date"], ...}
    """
    # PROVIDED: Get the directory where this script is located
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # PROVIDED: Construct full path to the categories file
    file_path = os.path.join(dir_path, filename)
    
    categories = {}

    with open(file_path) as file:
        for line in file:
            category_list = line.split(': ')
            category = category_list[0]
            words = category_list[1].strip().split(', ')
            categories[category] = words
    return categories


def create_word_lookup(categories_dict):
    """
    Create a reverse lookup dictionary mapping words to their categories.
    
    Args:
        categories_dict (dict): Dictionary mapping category names to word lists
        
    Returns:
        dict: Dictionary mapping words to category names
              Example: {"apple": "fruits", "red": "colors", ...}
    """
    word_lookup = {}
    for category, words in categories_dict.items():
        for word in words:
            word_lookup[word] = category
    
    return word_lookup
    
    pass

