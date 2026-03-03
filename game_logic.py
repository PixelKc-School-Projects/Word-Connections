"""
Game Logic Module (PROVIDED)
Validation and game logic functions.
"""


def validate_group(words_list, categories_dict, word_lookup_dict):
    """
    Validate if a list of 4 words forms a valid category group.
    
    Args:
        words_list (list): List of 4 words to validate
        categories_dict (dict): Dictionary mapping category names to word lists
        word_lookup_dict (dict): Dictionary mapping words to category names
        
    Returns:
        str or None: Category name if valid group, None otherwise
    """
    if len(words_list) != 4:
        return None
    
    # Check if all words belong to the same category
    categories = set()
    for word in words_list:
        if word in word_lookup_dict:
            categories.add(word_lookup_dict[word])
        else:
            return None
    
    # All words must belong to the same category
    if len(categories) == 1:
        category = categories.pop()
        # Verify all 4 words are in the category
        if category in categories_dict:
            category_words = set(categories_dict[category])
            if set(words_list).issubset(category_words):
                return category
    
    return None

def add_guess_to_history(previous_guesses, words_list):
    """
    Add a guess to the history.
    
    Args:
        previous_guesses (list): List of previous guesses
        words_list (list): List of 4 words from the current guess
    """
    previous_guesses.append(words_list.copy())


