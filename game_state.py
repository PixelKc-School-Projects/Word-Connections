"""
Game State Module
Handles solved categories tracking and win condition checking.
"""


def mark_category_solved(solved_categories, category_name, words):
    """
    Mark a category as solved by adding it to the solved categories dictionary.
    
    Args:
        solved_categories (dict): Dictionary mapping category names to word lists
        category_name (str): Name of the category that was solved
        words (list): List of words in the solved category
    """
    if category_name not in solved_categories:
        solved_categories[category_name] = words.copy()


def is_game_won(solved_categories):
    """
    Check if the game has been won (all 4 categories solved).
    
    Args:
        solved_categories (dict): Dictionary mapping category names to word lists
        
    Returns:
        bool: True if all 4 categories are solved, False otherwise
    """
    return len(solved_categories) == 4

