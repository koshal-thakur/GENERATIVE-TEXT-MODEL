# Text Generation Model

This project implements a text generation model using either GPT or LSTM architectures. The goal is to generate coherent paragraphs on specific topics based on user input.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd text-generation-model
pip install -r requirements.txt
```

## Usage

To generate text, run the main application:

```bash
python src/main.py
```

Follow the prompts to input a specific topic, and the model will generate a coherent paragraph based on that topic.

## Models

This project includes two models for text generation:

1. **GPT Model**: Implemented in `src/models/gpt_model.py`, this model utilizes the Generative Pre-trained Transformer architecture to generate text. It includes methods for loading the model, generating text, and setting parameters.

2. **LSTM Model**: Implemented in `src/models/lstm_model.py`, this model uses Long Short-Term Memory networks for text generation. It includes methods for loading the model, generating text, and training the model.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.