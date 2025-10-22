hindi_to_english = {
    "pustak": "book",
    "kutta": "dog",
    "billi": "cat",
    "ghar": "house",
    "pani": "water",
    "khaana": "food",
    "school": "school",
    "dost": "friend",
    "gaadi": "car",
    "ped": "tree"
}

print("Welcome to the Hindi-to-English Dictionary!")
print("Available Hindi words:", ', '.join(hindi_to_english.keys()))

word = input("\nEnter a Hindi word to get its English meaning: ").strip().lower()

print(hindi_to_english[word])