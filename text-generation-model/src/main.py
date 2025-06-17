# main.py

import sys
from models.gpt_model import GptModel
from models.lstm_model import LstmModel
from data.preprocess import load_data, clean_text, tokenize_text
from utils.helpers import save_output, load_config, log_message

def main():
    # Load configuration
    config = load_config('config.py')
    
    # Initialize models
    gpt_model = GptModel()
    lstm_model = LstmModel()
    
    # Load and preprocess data
    raw_data = load_data(config['data_path'])
    cleaned_data = clean_text(raw_data)
    tokenized_data = tokenize_text(cleaned_data)
    
    # Set model parameters
    gpt_model.set_parameters(config['gpt_parameters'])
    lstm_model.set_parameters(config['lstm_parameters'])
    
    # User input for topic
    topic = input("Enter a topic for text generation: ")
    
    # Generate text
    gpt_output = gpt_model.generate_text(topic)
    lstm_output = lstm_model.generate_text(topic)
    
    # Save outputs
    save_output('gpt_output.txt', gpt_output)
    save_output('lstm_output.txt', lstm_output)
    
    # Log messages
    log_message(f"Generated text for topic: {topic}")

if __name__ == "__main__":
    main()