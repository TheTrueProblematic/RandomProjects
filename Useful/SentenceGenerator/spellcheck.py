#!/usr/bin/env python3
"""
A simple Python script that takes a sentence as input and outputs the sentence
with all words spell checked.

Requires:
    pyspellchecker (install via: pip install pyspellchecker)
"""

import re
from spellchecker import SpellChecker

def spell_check_sentence(sentence):
    """
Spell checks the given sentence and returns a corrected version.

The sentence is tokenized into words and punctuation using regex.
Each word is checked and corrected, preserving the original capitalization.
    """
    spell = SpellChecker()
    # Tokenize: capture words (including contractions) and punctuation.
    tokens = re.findall(r"[\w']+|[.,!?;]", sentence)
    corrected_tokens = []

    for token in tokens:
      # Only apply spell check to alphabetic tokens (including apostrophes)
      if re.match(r"^[A-Za-z']+$", token):
        # Get the correction in lowercase
        corrected = spell.correction(token.lower())
        # If no correction is found, use the original token
        if corrected is None:
          corrected = token.lower()
        # Restore capitalization if needed
        if token[0].isupper():
          corrected = corrected.capitalize()
        corrected_tokens.append(corrected)
      else:
        # For punctuation or tokens that don't match, leave unchanged.
        corrected_tokens.append(token)

    # Reassemble the tokens into a sentence.
    result = ""
    for token in corrected_tokens:
      if token in [".", ",", "!", "?", ";"]:
        result += token
      else:
        if result:
          result += " "
        result += token
    return result

if __name__ == "__main__":
  sentence = input("Enter a sentence: ")
  corrected_sentence = spell_check_sentence(sentence)
  print("Corrected sentence:", corrected_sentence)
  