"""
Main Game Loop (PROVIDED)
Word Connections Game - Main entry point.
"""

import random
from category_manager import *
from game_state import *
from display import *
from game_logic import *
from helpers import getch


def select_random_categories(categories_dict, num_categories=4):
    """
    Select random categories for the game.
    
    Args:
        categories_dict (dict): Dictionary of all available categories
        num_categories (int): Number of categories to select (default: 4)
        
    Returns:
        dict: Dictionary with selected categories only
    """
    if len(categories_dict) < num_categories:
        return categories_dict
    
    category_names = list(categories_dict.keys())
    selected_names = random.sample(category_names, num_categories)
    
    selected_categories = {}
    for name in selected_names:
        selected_categories[name] = categories_dict[name]
    
    return selected_categories


def get_all_words(categories_dict):
    """
    Get all words from the selected categories.
    
    Args:
        categories_dict (dict): Dictionary mapping category names to word lists
        
    Returns:
        list: List of all 16 words (shuffled)
    """
    all_words = []
    for words in categories_dict.values():
        all_words.extend(words)
    
    # Shuffle the words
    random.shuffle(all_words)
    return all_words


def play_game(categories_dict, word_lookup_dict):
    """
    Main game loop that handles player interaction and game flow.
    
    Args:
        categories_dict (dict): Dictionary mapping category names to word lists
        word_lookup_dict (dict): Dictionary mapping words to category names
    """
    # Initialize game state
    previous_guesses = []
    current_selection = []
    all_words = get_all_words(categories_dict)
    solved_categories = {}  # Dictionary mapping category names to word lists (maintains insertion order)
    error_message = None  # Store error messages to display at top
    cursor_row = 0  # Cursor position in grid
    cursor_col = 0  # Cursor position in grid
    previous_grid_size = len(all_words)  # Track grid size changes
    
    # Game loop - continue until 5 guesses made or game won
    while len(previous_guesses) < 5:
        # Reset cursor if grid size changed
        if len(all_words) != previous_grid_size:
            cursor_row = 0
            cursor_col = 0
            previous_grid_size = len(all_words)
        
        clear_screen()
        display_game_screen(all_words, current_selection, solved_categories, error_message, cursor_row, cursor_col)
        error_message = None  # Clear error message after displaying once
        
        # Check if game is won
        if is_game_won(solved_categories):
            display_win_screen()
            return
        
        # Get player input using getch (arrow keys, no Enter required)
        key = getch()
        
        # Calculate current grid dimensions
        rows, cols = get_grid_dimensions(len(all_words))
        
        # Ensure cursor is within bounds (before processing input)
        if cursor_row >= rows:
            cursor_row = max(0, rows - 1)
        if cursor_col >= cols:
            cursor_col = max(0, cols - 1)
        
        if key == 'q':
            print("\nThanks for playing!")
            return
        
        elif key == 'c':
            # Clear selection
            current_selection = []
            continue
        
        elif key == 's':
            # Submit guess
            if len(current_selection) != 4:
                error_message = "✗ Please select exactly 4 words before submitting!"
                continue
            
            # Validate the guess
            category = validate_group(current_selection, categories_dict, word_lookup_dict)
            
            if category:
                # Correct guess!
                mark_category_solved(solved_categories, category, current_selection)
                
                # Remove all 4 words from the grid
                for word in current_selection:
                    if word in all_words:
                        all_words.remove(word)
                
                # Skip success message - screen will update immediately
                add_guess_to_history(previous_guesses, current_selection)
                current_selection = []
                
                # Check if only 4 words remain (last category automatically solved)
                if len(all_words) == 4:
                    # Find which category these 4 words belong to
                    remaining_category = None
                    for cat_name, cat_words in categories_dict.items():
                        if set(all_words) == set(cat_words):
                            remaining_category = cat_name
                            break
                    
                    if remaining_category:
                        # Automatically solve the last category
                        mark_category_solved(solved_categories, remaining_category, all_words)
                        all_words = []  # Clear the grid
                
                # Reshuffle remaining words for new grid (if any remain)
                if all_words:
                    random.shuffle(all_words)
                
                # Check if game is won
                if is_game_won(solved_categories):
                    display_win_screen()
                    return
                # Continue immediately - screen will update on next loop iteration
                continue
            else:
                # Incorrect guess - set error message to display at top
                error_message = "✗ Incorrect. Try again!"
                add_guess_to_history(previous_guesses, current_selection)
                current_selection = []
                # Continue immediately - screen will update on next loop iteration
                continue
        
        elif key in ['up', 'down', 'left', 'right']:
            # Arrow key navigation with wrapping
            if key == 'up':
                cursor_row = (cursor_row - 1) % rows if rows > 0 else 0
            elif key == 'down':
                cursor_row = (cursor_row + 1) % rows if rows > 0 else 0
            elif key == 'left':
                cursor_col = (cursor_col - 1) % cols if cols > 0 else 0
            elif key == 'right':
                cursor_col = (cursor_col + 1) % cols if cols > 0 else 0
            
            # Ensure cursor is on a valid word position (not empty cell)
            word_idx = cursor_row * cols + cursor_col
            if word_idx >= len(all_words):
                # Cursor is on empty cell, move to last valid position in row
                last_col_in_row = (len(all_words) - 1) % cols
                if cursor_row * cols + last_col_in_row < len(all_words):
                    cursor_col = last_col_in_row
                else:
                    # Move to previous row if current row is empty
                    cursor_row = max(0, cursor_row - 1)
                    cursor_col = min(cols - 1, (len(all_words) - cursor_row * cols - 1) % cols)
            continue
        
        elif key in [' ', '\n', '\r']:  # Space or Enter to toggle selection
            # Get word at cursor position
            word_idx = cursor_row * cols + cursor_col
            if word_idx < len(all_words):
                word = all_words[word_idx]
                
                # Toggle selection
                if word in current_selection:
                    current_selection.remove(word)
                elif len(current_selection) < 4:
                    current_selection.append(word)
                else:
                    error_message = "✗ You can only select 4 words at a time!"
            else:
                # Cursor is on empty cell (partial row)
                error_message = "✗ No word at this position!"
            continue
        
        elif key == 'r':
            # Reshuffle words
            random.shuffle(all_words)
            continue
    
    # Game over - ran out of guesses
    print("\nSorry you lost, Game Over!")

def main():
    """Main entry point for the game."""
    # Load categories from file
    filename = "categories_data.txt"
    
    try:
        all_categories = load_categories(filename)
        
        if len(all_categories) < 4:
            print(f"Error: Need at least 4 categories in {filename}")
            return
        
        # Select 4 random categories for the game
        selected_categories = select_random_categories(all_categories, 4)
        
        # Create word-to-category lookup
        word_lookup = create_word_lookup(selected_categories)
        
        # Start the game
        play_game(selected_categories, word_lookup)
        
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        print("Make sure the file exists in the same directory as main.py")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

