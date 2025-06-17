def save_output(output, file_path):
    with open(file_path, 'w') as f:
        f.write(output)

def load_config(config_path):
    import json
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def log_message(message, log_file='app.log'):
    with open(log_file, 'a') as f:
        f.write(f"{message}\n")