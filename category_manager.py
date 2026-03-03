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
    
    # STEP #1 (Week 21): Load Categories Dictionary
    # TODO: Create an empty dictionary to store categories
    # TODO: Open the file and read it line by line
    # TODO: For each line, split on ':' to separate category name and words
    # TODO: Split words on ',' to get a list of words
    # TODO: Add the category and words to the dictionary
    
    pass


def create_word_lookup(categories_dict):
    """
    Create a reverse lookup dictionary mapping words to their categories.
    
    Args:
        categories_dict (dict): Dictionary mapping category names to word lists
        
    Returns:
        dict: Dictionary mapping words to category names
              Example: {"apple": "fruits", "red": "colors", ...}
    """
    # STEP #2 (Week 21): Create Word-to-Category Lookup
    # TODO: Create an empty dictionary for the word lookup
    # TODO: Iterate through categories_dict using .items()
    # TODO: For each category and its words, add each word to the lookup dictionary
    
    pass

