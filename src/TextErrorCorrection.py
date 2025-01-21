import pandas as pd
import numpy as np
import nltk
import re
from collections import Counter

def process_data(file_name):

  with open(file_name) as f:
    file = f.read()
    file = file.lower()
    return re.findall(r'\w+', file)

word_l = process_data('shakespeare.txt')
vocab = set(word_l)
len(vocab),len(word_l)

word_l[:4]

def get_count(word_l):

  word_count = Counter(word_l)
  return word_count

word_count_dict = get_count(word_l)
len(word_count_dict),word_count_dict["thee"]

def get_probs(word_count_dict):

  probs = {}
  M = sum(word_count_dict.values())

  for word, count in word_count_dict.items():
    probs[word] = count / M

  return probs

probs = get_probs(word_count_dict)

len(probs),probs['thee']

def delete_letter(word):

  # skip one letter
  # ex: like -> [ike, lke, lie, lik]
  delete = [ word[:i] + word[i+1:] for i in range(len(word)) ]

  return delete

def switch_letter(word):

  # ex: eat -> [aet, eta]
  switch = [ word[:i] + word[i+1] + word[i] + word[i+2:]
            for i in range(len(word)-1) ]

  return switch

#switch_letter('eta')

import string
letters = string.ascii_lowercase

def replace_letter(word):

  replace = []
  dlt = delete_letter(word)

  for i,d in enumerate(dlt):

    for j in range(len(letters)):

      replace.append(d[:i] + letters[j] + d[i:])

  rep_set = sorted(set(replace))

  return rep_set

#replace_letter('can')

def insert_letter(word):

  insert = []

  for i in range(len(word)+1):

    for j in letters:
      insert.append(word[:i] + j + word[i:])

  return insert

#insert_letter('catalog')

def edit_one_letter(word, allow_switches = True):

  delete = delete_letter(word)
  replace = replace_letter(word)
  insert = insert_letter(word)

  switch = []
  if allow_switches:
    switch = switch_letter(word)

  return set(delete + replace + insert + switch)

print("number of corrected words:", len(edit_one_letter('catq')))
print("corrected words intersected with vocab", edit_one_letter('catq').intersection(vocab))

def edit_two_letters(word, allow_switches = True):

  edit_1 = edit_one_letter(word, allow_switches)
  edit_2 = set()

  for w in edit_1:
    edit_2.update(edit_one_letter(w,allow_switches))

  return edit_2

len(edit_two_letters('catt'))

def get_corrections(word, probs, vocab):

  suggestions = []

  if word in vocab:
    suggestions.append(word)
    return [word, probs[word]]

  edit_1 = edit_one_letter(word).intersection(vocab)
  suggestions.append(edit_1)

  if not suggestions:
    edit_2 = edit_two_letters(word).intersection(vocab)
    suggestions.append(edit_2)

  n_best = sorted([[w,probs[w]] for w in suggestions[0]], key=lambda x:x[1],reverse =True)

  return n_best

get_corrections('carx',probs,vocab)

def min_edit_distance(source, target, ins_cost = 1, del_cost = 1, rep_cost = 2):

    # use deletion and insert cost as  1
    m = len(source)
    n = len(target)

    #initialize cost matrix with zeros and dimensions (m+1,n+1)
    D = np.zeros((m+1, n+1), dtype=int)

    # Fill in column 0, from row 1 to row m, both inclusive
    for row in range(1,m+1): # Replace None with the proper range
        D[row,0] = D[row-1,0] + del_cost

    # Fill in row 0, for all columns from 1 to n, both inclusive
    for col in range(1,n+1): # Replace None with the proper range
        D[0,col] = D[0,col-1] + ins_cost

    # Loop through row 1 to row m, both inclusive
    for row in range(1,m+1):

        # Loop through column 1 to column n, both inclusive
        for col in range(1,n+1):

            # Intialize r_cost to the 'replace' cost that is passed into this function
            r_cost = rep_cost

            # Check to see if source character at the previous row
            # matches the target character at the previous column,
            if source[row-1] == target[col-1]:
                # Update the replacement cost to 0 if source and target are the same
                r_cost = 0

            # Update the cost at row, col based on previous entries in the cost matrix
            # Refer to the equation calculate for D[i,j] (the minimum of three calculated costs)
            D[row,col] = min([D[row-1,col]+del_cost, D[row,col-1]+ins_cost, D[row-1,col-1]+r_cost])

    # Set the minimum edit distance with the cost found at row m, column n
    med = D[m,n]

    return D, med

source =  'dys'
target = 'days'
matrix, min_edits = min_edit_distance(source, target)
print("minimum edits: ",min_edits, "\n")
idx = list('#' + source)
cols = list('#' + target)
df = pd.DataFrame(matrix, index=idx, columns= cols)
print(df)

