import random

class Spinner:
    def __init__(self, synonym_file):
        self.synonyms = self.load_synonyms(synonym_file)

    def load_synonyms(self, synonym_file):
        synonyms = {}
        with open(synonym_file, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    word, synonym_str = parts
                    synonym_list = synonym_str.split(',')
                    synonyms[word] = synonym_list
        return synonyms

    def change_words(self, text, probability):
        words = text.split()
        modified_text = []

        for word in words:
            # Check if the word is in the synonym dictionary
            if word in self.synonyms:
                # Generate a random number between 1 and 100
                random_num = random.randint(1, 100)
                # If the random number is less than or equal to the given probability, replace the word
                if random_num <= probability:
                    synonyms_list = self.synonyms[word]
                    # Choose a random synonym from the list
                    new_word = random.choice(synonyms_list)
                    modified_text.append(new_word)
                else:
                    modified_text.append(word)
            else:
                modified_text.append(word)

        return ' '.join(modified_text)
