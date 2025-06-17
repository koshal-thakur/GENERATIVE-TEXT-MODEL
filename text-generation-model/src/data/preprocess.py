def load_data(file_path):
    # Function to load data from a specified file path
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def clean_text(text):
    # Function to clean the input text by removing unwanted characters and normalizing
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text

def tokenize_text(text):
    # Function to tokenize the cleaned text into words
    return text.split()