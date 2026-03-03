# Week 21: Word Connections Game - Core Dictionary Operations

## Project Overview

Welcome to the Word Connections game! This is a Connections-style word grouping game where you'll find groups of 4 words that belong to the same category. In Week 21, you'll implement the core dictionary operations needed to load categories and create word lookups.

This is a **multi-week project** - Week 21 focuses on loading and organizing data using dictionaries, and Week 22 will add win/lose states and solution display.

## Game Description

The game presents you with 16 words arranged in a grid. Your goal is to find 4 groups of 4 words each, where all words in a group belong to the same category. You have 5 guesses to find all 4 categories!

**Example Categories:**
- `fruits`: apple, banana, cherry, date
- `colors`: red, blue, green, yellow
- `animals`: dog, cat, bird, fish
- `countries`: usa, canada, mexico, brazil

## Learning Objectives

- Load data from text files into dictionaries
- Parse strings using `.split()` method
- Create reverse lookup dictionaries
- Iterate through dictionaries using `.items()`
- Work with file I/O operations

## Project Structure

The starting project includes:
- `category_manager.py` - Where you'll implement the 2 core dictionary functions
- `game_logic.py` - PROVIDED: Validation functions
- `game_state.py` - PROVIDED: Game state tracking
- `display.py` - PROVIDED: All UI rendering
- `main.py` - PROVIDED: Main game loop
- `helpers.py` - PROVIDED: Input handling utilities
- `categories_data.txt` - Text file containing category data

## Setup Instructions

1. Open the `starting-project/category_manager.py` file
2. Look for the TODO comments marking the 2 functions you need to implement
3. Review the `categories_data.txt` file to understand the data format
4. Run the game to see what happens before your implementation (it won't work yet!)

## Data File Format

The `categories_data.txt` file contains one category per line in this format:
```
category_name: word1, word2, word3, word4
```

**Example:**
```
fruits: apple, banana, cherry, date
colors: red, blue, green, yellow
animals: dog, cat, bird, fish
```

## Step-by-Step Implementation

### STEP #1: Implement `load_categories()` Function

**Purpose:** Load categories from a text file and build a dictionary mapping category names to lists of words.

**What to do:**
1. Create an empty dictionary to store categories
2. Open the file and read it line by line
3. For each line:
   - Strip whitespace and skip empty lines
   - Check if the line contains a `:` (which separates category from words)
   - Split the line on `:` to separate the category name from the words
   - Split the words string on `,` to get a list of individual words
   - Strip whitespace from each word
   - Add the category and its words to the dictionary
4. Return the completed dictionary

**Syntax Examples:**
```python
# Split on ':' with max 1 split (prevents issues if category name contains ':')
parts = line.split(':', 1)

# Split and strip words in one line using list comprehension
words = [word.strip() for word in words_str.split(',')]
```

**Expected Result:**
The function should return a dictionary like:
```python
{
    "fruits": ["apple", "banana", "cherry", "date"],
    "colors": ["red", "blue", "green", "yellow"],
    "animals": ["dog", "cat", "bird", "fish"]
}
```

**Test Checkpoint:**
- After implementing, test that `load_categories("categories_data.txt")` returns a dictionary
- Verify the dictionary has the correct structure (category names as keys, lists of words as values)
- Check that all words are properly stripped of whitespace

---

### STEP #2: Implement `create_word_lookup()` Function

**Purpose:** Create a reverse lookup dictionary that maps each word to its category name.

**What to do:**
1. Create an empty dictionary for the word lookup
2. Iterate through `categories_dict` to access each category and its words
3. For each category, loop through all its words
4. Add each word to the lookup dictionary, mapping the word to its category
5. Return the completed lookup dictionary

**Syntax Examples:**
```python
# Use .items() to get both key and value when iterating through a dictionary
for category, words in categories_dict.items():
    # (students figure out the nested loop and dictionary assignment themselves)
```

**Expected Result:**
The function should return a dictionary like:
```python
{
    "apple": "fruits",
    "banana": "fruits",
    "cherry": "fruits",
    "date": "fruits",
    "red": "colors",
    "blue": "colors",
    "green": "colors",
    "yellow": "colors"
}
```

**Test Checkpoint:**
- After implementing, test that `create_word_lookup(categories_dict)` returns a dictionary
- Verify each word maps to its correct category
- Check that all words from all categories are included

---

## Testing Your Implementation

1. **Run the game** and verify it loads:
   - The game should start without errors
   - Categories should be loaded from the file
   - The word grid should display 16 words

2. **Test category loading:**
   - Verify categories are loaded correctly
   - Check that words are properly parsed from the file

3. **Test word lookup:**
   - Select 4 words that belong to the same category
   - Submit your guess (press 's')
   - Verify the game correctly identifies matching categories

4. **Test with different categories:**
   - Try finding different category groups
   - Verify the lookup works for all categories

## Troubleshooting

**File not found error:**
- Make sure `categories_data.txt` is in the same directory as `category_manager.py`
- The provided code handles file path resolution automatically

**Dictionary is empty:**
- Check that you're opening the file correctly
- Verify you're splitting the line on `:` correctly
- Make sure you're adding items to the dictionary inside the loop

**Words not parsing correctly:**
- Verify you're splitting on `,` to separate words
- Check that you're stripping whitespace from each word
- Make sure you're handling the case where `:` is in the line

**Lookup dictionary missing words:**
- Verify you're iterating through all categories using `.items()`
- Check that you're looping through all words in each category
- Ensure you're adding each word to the lookup dictionary

## Next Steps

Once you've completed Week 21, you're ready for Week 22 where you'll add win/lose states and display the solution with color-coded categories!

