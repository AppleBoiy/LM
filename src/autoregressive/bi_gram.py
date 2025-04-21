#!/usr/bin/env python3
import requests
from string import ascii_lowercase



names_txt_url = "https://raw.githubusercontent.com/cmu-l3/anlp-spring2025-code/refs/heads/main/03_lm_fundamentals/names.txt"
res = requests.get(names_txt_url) 
if res.status_code == 200:
    text = res.text
else:
    print(f"Failed: due status {res.status_code}")
    exit(1)

# training process
bi_counts = {}
for x in text:
   seq = ['S'] + list(x) + ['S']
   for x1, x2 in zip(seq, seq[1:]):
       bigram = (x1, x2)
       bi_counts[bigram] = bi_counts.get(bigram, 0) + 1


# make mapping from char to indices and vice-versa
char_to_index = {char: i for i, char in enumerate(ascii_lowercase)}
char_to_index['[S]'] = 26
index_to_char = {i: char for char, i in char_to_index.items()}

sorted(bi_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(bi_counts)
