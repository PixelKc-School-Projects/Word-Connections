"""
Display Module (PROVIDED)
UI rendering functions for the Word Connections game.
"""

import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')


def get_grid_dimensions(num_words):
    """
    Calculate rows and cols for grid based on word count.
    Shared utility function.
    
    Args:
        num_words (int): Number of words to display
        
    Returns:
        tuple: (rows, cols) for the grid
    """
    if num_words >= 12:
        cols = 4
    elif num_words >= 8:
        cols = 4
    else:
        cols = 2
    rows = (num_words + cols - 1) // cols
    return rows, cols


def display_header():
    """Display the game header."""
    print("\n" + "="*50)
    print("WORD CONNECTIONS GAME")
    print("="*50)


def display_error_message(error_message):
    """
    Display error message at the top of the screen.
    
    Args:
        error_message (str): Error message to display (None to skip)
    """
    if error_message:
        print(f"\n{error_message}\n")
        print("-" * 73)


def display_instructions():
    """Display game instructions."""
    print("\nSelect 4 words that belong to the same category.")
    print("You have 5 guesses to find all 4 categories!\n")


def display_solved_categories(solved_categories):
    """
    Display solved categories at the top of the screen.
    
    Args:
        solved_categories (dict): Dictionary mapping category names to word lists (maintains insertion order)
    """
    if not solved_categories:
        return
    
    # Color scheme matching win screen
    colors = ['🟨', '🟩', '🟦', '🟪']
    
    for idx, (category_name, words_list) in enumerate(solved_categories.items()):
        color = colors[idx % len(colors)]
        
        # Center the category name
        category_display = f"{color} {category_name.upper()}"
        padding = (50 - len(category_display)) // 2
        print(" " * padding + category_display)
        
        # Display words aligned with grid columns (16 chars per word + separators)
        word_display = []
        for word in words_list:
            word_display.append(f" {word:16} ")
        print(" | ".join(word_display))
    
    # Separator line
    print("-" * 73)
    print()


def display_word_grid(all_words, current_selection, cursor_row, cursor_col):
    """
    Display remaining words in a grid with cursor and selection highlighting.
    
    Args:
        all_words (list): List of remaining words to display in grid
        current_selection (list): List of currently selected words
        cursor_row (int): Current cursor row position in grid
        cursor_col (int): Current cursor column position in grid
    """
    num_words = len(all_words)
    rows, cols = get_grid_dimensions(num_words)
    
    # Display remaining words in grid with cursor
    for row in range(rows):
        start_idx = row * cols
        end_idx = min(start_idx + cols, num_words)
        row_words = all_words[start_idx:end_idx]
        row_display = []
        
        for col in range(len(row_words)):
            word = row_words[col]
            word_idx = start_idx + col
            
            # Check if this is the cursor position
            is_cursor = (row == cursor_row and col == cursor_col)
            
            # Check if word is selected
            is_selected = word in current_selection
            
            if is_cursor and is_selected:
                # Cursor on selected word: >[word]<
                row_display.append(f">[{word:14}]<")
            elif is_cursor:
                # Cursor on word: > word <
                row_display.append(f"> {word:14} <")
            elif is_selected:
                # Selected word (not cursor): [word]
                row_display.append(f"[{word:16}]")
            else:
                # Regular word:  word 
                row_display.append(f" {word:16} ")
        
        print(" | ".join(row_display))


def display_selection_info(current_selection):
    """
    Display current selection count and words.
    
    Args:
        current_selection (list): List of currently selected words
    """
    print(f"\nSelected: {len(current_selection)}/4")
    if current_selection:
        print(f"Current selection: {', '.join(current_selection)}")


def display_help_menu():
    """Display the help menu with controls."""
    print("\n" + "-" * 73)
    print("Controls: Arrow keys to move | Space/Enter to select | 's' to submit | 'c' to clear | 'r' to reshuffle | 'q' to quit")


def display_game_screen(all_words, current_selection, solved_categories, error_message, cursor_row, cursor_col):
    """
    Display the complete game screen (header, error, solved categories, grid, selection info, help).
    This is the main function students call - it orchestrates all the smaller display functions.
    
    Args:
        all_words (list): List of remaining words to display in grid
        current_selection (list): List of currently selected words
        solved_categories (dict): Dictionary mapping category names to word lists (maintains insertion order)
        error_message (str, optional): Error message to display at the top
        cursor_row (int): Current cursor row position in grid
        cursor_col (int): Current cursor column position in grid
    """
    display_header()
    display_error_message(error_message)
    display_instructions()
    display_solved_categories(solved_categories)
    display_word_grid(all_words, current_selection, cursor_row, cursor_col)
    display_selection_info(current_selection)
    display_help_menu()


def display_win_screen():
    """
    Display the win screen with all categories and their words.
    
    Args:
        categories_dict (dict): Dictionary mapping category names to word lists
    """
    clear_screen()
    print("\n" + "="*60)
    print("🎉 CONGRATULATIONS! YOU WON! 🎉")
    print("="*60)
