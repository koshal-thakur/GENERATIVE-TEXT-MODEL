# Configuration settings for the text generation model

class Config:
    # Model parameters
    MODEL_TYPE = 'gpt'  # Options: 'gpt' or 'lstm'
    MAX_LENGTH = 100  # Maximum length of generated text
    TEMPERATURE = 0.7  # Sampling temperature for text generation
    TOP_K = 50  # Top-k sampling
    TOP_P = 0.95  # Nucleus sampling

    # File paths
    DATA_PATH = 'data/input.txt'  # Path to the input data file
    OUTPUT_PATH = 'output/generated_text.txt'  # Path to save generated text
    CHECKPOINT_PATH = 'models/checkpoint.pth'  # Path to model checkpoint

    # Training parameters
    EPOCHS = 10  # Number of training epochs
    BATCH_SIZE = 32  # Batch size for training
    LEARNING_RATE = 0.001  # Learning rate for the optimizer

    # Logging settings
    LOGGING_LEVEL = 'INFO'  # Logging level (DEBUG, INFO, WARNING, ERROR)
    LOGGING_PATH = 'logs/training.log'  # Path to save logs