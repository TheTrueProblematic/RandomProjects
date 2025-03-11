import random
import re

# Load word lists from files
with open("Adverbs.txt", "r") as f:
    adverbs = [line.strip() for line in f if line.strip()]

with open("Adjectives.txt", "r") as f:
    adjectives = [line.strip() for line in f if line.strip()]

with open("Verbs.txt", "r") as f:
    verbs = [line.strip() for line in f if line.strip()]

with open("Nouns.txt", "r") as f:
    nouns = [line.strip() for line in f if line.strip()]

# Pre-filter lists for specific conditions
vowels = "aeiouAEIOU"

# For adjectives: 'cadj' (starting with a consonant) and 'vadj' (starting with a vowel)
cadj_list = [adj for adj in adjectives if adj and adj[0] not in vowels]
vadj_list = [adj for adj in adjectives if adj and adj[0] in vowels]

# For nouns: separate singular (not ending in 's') and plural (ending in 's')
singular_nouns = [noun for noun in nouns if not noun.endswith("s")]
plural_nouns = [noun for noun in nouns if noun.endswith("s")]

# For adverbs ending in 'ly'
adverbly_list = [adv for adv in adverbs if adv.endswith("ly")]

def word(word_type):
    """
    Returns a random word from the source parts of speech files that matches the requested type,
    without modifying the original words.
    Supported types:
      - "verbing": a verb that already ends in "ing"
      - "verbes": a verb that already ends in "es"
      - "verbed": a verb that already ends in "ed"
      - "verbize": a verb that already ends in "ize"
      - "verbs": a verb that ends in "s" but not "es"
      - "noun": a singular noun (does not end in "s")
      - "nouns": a plural noun (ends in "s")
      - "cadj": an adjective starting with a consonant
      - "vadj": an adjective starting with a vowel
      - "adj": any adjective
      - "adverb": any adverb
      - "adverbly": an adverb that already ends in "ly"
      - "adjest": an adjective that already ends in "est"
      - "adjnest": an adjective that does not end in "est"
      - "adjy": an adjective that already ends in "y"
      - "verbnt": a verb that does not end in "ize", "izes", "s", "es", "ed", or "ing"
    """
    if word_type == "verbing":
        verbing_list = [v for v in verbs if v.endswith("ing")]
        return random.choice(verbing_list) if verbing_list else random.choice(verbs)

    elif word_type == "verbes":
        verbes_list = [v for v in verbs if v.endswith("es")]
        return random.choice(verbes_list) if verbes_list else random.choice(verbs)

    elif word_type == "verbed":
        verbed_list = [v for v in verbs if v.endswith("ed")]
        return random.choice(verbed_list) if verbed_list else random.choice(verbs)

    elif word_type == "verbize":
        verbize_list = [v for v in verbs if v.endswith("ize")]
        return random.choice(verbize_list) if verbize_list else random.choice(verbs)

    elif word_type == "verbs":
        verbs_list = [v for v in verbs if v.endswith("s") and not v.endswith("es")]
        return random.choice(verbs_list) if verbs_list else random.choice(verbs)

    elif word_type == "noun":
        noun_list = [n for n in nouns if not n.endswith("s")]
        return random.choice(noun_list) if noun_list else random.choice(nouns)

    elif word_type == "nouns":
        noun_list = [n for n in nouns if n.endswith("s")]
        return random.choice(noun_list) if noun_list else random.choice(nouns)

    elif word_type == "cadj":
        cadj_filtered = [adj for adj in adjectives if adj and adj[0] not in vowels]
        return random.choice(cadj_filtered) if cadj_filtered else random.choice(adjectives)

    elif word_type == "vadj":
        vadj_filtered = [adj for adj in adjectives if adj and adj[0] in vowels]
        return random.choice(vadj_filtered) if vadj_filtered else random.choice(adjectives)

    elif word_type == "adj":
        return random.choice(adjectives)

    elif word_type == "adverb":
        return random.choice(adverbs)

    elif word_type == "adverbly":
        adverbly_filtered = [adv for adv in adverbs if adv.endswith("ly")]
        return random.choice(adverbly_filtered) if adverbly_filtered else random.choice(adverbs)

    elif word_type == "adjest":
        adjectives_est = [adj for adj in adjectives if adj.endswith("est")]
        return random.choice(adjectives_est) if adjectives_est else random.choice(adjectives)

    elif word_type == "adjnest":
        adjectives_nest = [adj for adj in adjectives if not adj.endswith("est")]
        return random.choice(adjectives_nest) if adjectives_nest else random.choice(adjectives)

    elif word_type == "adjy":
        adjectives_y = [adj for adj in adjectives if adj.endswith("y")]
        return random.choice(adjectives_y) if adjectives_y else random.choice(adjectives)

    elif word_type == "verbnt":
        verbs_nt = [v for v in verbs if not (v.endswith("ize") or v.endswith("izes") or
                                             v.endswith("s") or v.endswith("es") or
                                             v.endswith("ed") or v.endswith("ing"))]
        return random.choice(verbs_nt) if verbs_nt else random.choice(verbs)

    else:
        return ""

def makeSentence():
    """
    Generates a sentence using one of several predefined templates.
    The sentence is created by replacing placeholders (e.g., {adj}, {noun})
    with a random word generated by the word() function. Each placeholder is
    replaced independently.
    """
    templates = [
        "The {adj} {noun} {verbed} {adverbly}, but I {verbed} {adverbly}. ",
        "A {cadj} {noun} is {verbing} the {adj} {nouns}. ",
        "If the {noun} {verbs}, then {verbize} {adverbly}. ",
        "While the {adj} {nouns} {verbed}, I {verbed} the {adj} {noun}. ",
        "Thus, all of the {adj} {nouns} {verbed}, and a {cadj} {noun} {verbed} alone. ",
        "You can't stop {verbing} until the {adj} {noun} {verbs}. ",
        "I regularly {verbnt} {adverbly} while {verbing} {adverbly}. ",
        "Suddenly, the {noun} {verbed} {nouns} in an {vadj} manner. "
    ]
    template = random.choice(templates)

    # Replace each placeholder individually with a new random word
    def repl(match):
        return word(match.group(1))
    return re.sub(r"\{(.*?)\}", repl, template)

if __name__ == "__main__":
    try:
        num_sentences = int(input("How many sentences to make? "))
    except ValueError:
        print("Please enter a valid integer.")
        exit(1)

    sentences = [makeSentence() for _ in range(num_sentences)]

    with open("sentences.txt", "w") as out_file:
        for sentence in sentences:
            out_file.write(sentence.strip() + "\n")

    print(f"{num_sentences} sentences written to sentences.txt")
