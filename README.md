# Text Processing and Spell Checker Implementation

This notebook implements a spell checker and text processing system using various word transformation techniques and minimum edit distance calculations.

## Overview

The project includes:
- Text preprocessing for Shakespeare's text
- Word probability calculations
- Word transformation methods
- Minimum edit distance implementation
- Spell checking suggestions

## Requirements

- Python 3.x
- NumPy
- Pandas
- NLTK
- Regular expressions (re)
- Collections

## Data Files

- `shakespeare.txt`: Source text for vocabulary and word frequencies

## Main Functions

### Text Processing
```python
def process_data(file_name):
    # Processes text file and returns list of words
    
def get_count(word_l):
    # Returns word frequency dictionary
    
def get_probs(word_count_dict):
    # Calculates word probabilities
```

### Word Transformations
```python
def delete_letter(word):
    # Returns all possible single letter deletions

def switch_letter(word):
    # Returns all possible adjacent letter switches

def replace_letter(word):
    # Returns all possible single letter replacements

def insert_letter(word):
    # Returns all possible single letter insertions

def edit_one_letter(word, allow_switches=True):
    # Combines all single-edit transformations

def edit_two_letters(word, allow_switches=True):
    # Generates all two-edit transformations
```

### Spell Checking
```python
def get_corrections(word, probs, vocab):
    # Returns spelling suggestions with probabilities

def min_edit_distance(source, target, ins_cost=1, del_cost=1, rep_cost=2):
    # Calculates minimum edit distance between words
```

## Usage Example

```python
# Process text and create vocabulary
word_l = process_data('shakespeare.txt')
vocab = set(word_l)

# Generate word probabilities
word_count_dict = get_count(word_l)
probs = get_probs(word_count_dict)

# Get spelling suggestions
corrections = get_corrections('carx', probs, vocab)

# Calculate edit distance
matrix, min_edits = min_edit_distance('dys', 'days')
```

## Key Features

### Text Processing
- Case normalization
- Word tokenization
- Frequency counting
- Probability calculation

### Spell Checking
- Single-edit transformations
  - Deletions
  - Switches
  - Replacements
  - Insertions
- Two-edit transformations
- Probability-based suggestions
- Vocabulary intersection

### Edit Distance
- Dynamic programming implementation
- Configurable costs for:
  - Insertions
  - Deletions
  - Replacements
- Matrix visualization using Pandas

## Implementation Details

- Uses dynamic programming for edit distance
- Implements various word transformation techniques
- Provides probability-based correction suggestions
- Supports both single and double-edit distances
- Handles custom cost configurations for edit operations

## Algorithm Complexity
- Edit distance: O(mn) where m,n are word lengths
- Word transformations: O(n) for single edits
- Spell checking suggestions: O(vocabulary_size * word_length)
