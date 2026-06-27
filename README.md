# Password Generator

Deterministic Streamlit password generator from seed strings for local offline use.

A lightweight Python app that generates repeatable passwords from a memorable seed, so you can recover credentials without storing them. Runs as a containerized Streamlit web app on port 8501.

## Features

- **Deterministic generation**: Same seed always produces the same password (useful for password recovery)
- **Multiple interfaces**: Command-line, Tkinter GUI, or Streamlit web app
- **Strength validation**: Checks for uppercase, lowercase, numbers, and special characters
- **Customizable length**: Generate passwords from 4 to 72 characters
- **No database required**: Completely local and offline

## Installation

1. Clone the repository:
```bash
git clone <repo-url>
cd pwd_gen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Requirements
- Python 3.7+
- streamlit (for web app)
- tkinter (usually included with Python)

## Docker

Pull the published image:
```bash
docker pull qnguyen11/pwd-gen:latest
docker run -p 8501:8501 qnguyen11/pwd-gen:latest 
```

Build the image locally:
```bash
docker build -t pwd-gen .
```
or use docker compose:
```bash
docker compose build
```

Run the container:
```bash
docker run -p 8501:8501 pwd-gen
```
or with docker compose:
```bash
docker compose up
```

Then open `http://localhost:8501` in your browser.

## Usage

### Web App (Streamlit)
```bash
streamlit run app.py
```
Access at `http://localhost:8501` or use the hosted version at [pwdgenerator-nqt.streamlit.app](https://pwdgenerator-nqt.streamlit.app/)

### Command Line
```bash
# Generate password with seed and default length (15)
python cli.py -s "myseed"

# Custom length
python cli.py -s "myseed" -l 20

# Show password strength
python cli.py -s "myseed" -l 20 -c

# Full options
python cli.py --help
```

### GUI (Tkinter)
```bash
python pwd_gen_tk_app.py
```
- Enter seed string
- Specify desired length (default: 15)
- Click "Generate" or press Enter
- Click "Copy to clipboard" to copy the password

## How It Works

The generator uses a seed string as input to Python's `random.seed()`, making password generation deterministic:

1. Set random seed from your input string
2. Randomly select characters from: `A-Z`, `a-z`, `0-9`, `!@#$%&*()_`
3. Validate password meets strength criteria (all character types present)

**Important**: The same seed will always produce the same password. This is a feature, not a bug—use it to recover passwords without storing them.

## Security Considerations

⚠️ **This generator is NOT cryptographically secure** for new passwords because:
- Uses `random.seed()` which is for pseudo-random generation, not cryptography
- Seed entropy depends on user input (not truly random)

✅ **Good use cases**:
- Deterministic password recovery from a memorable seed
- Testing and development
- Offline password generation

❌ **Not recommended for**:
- Initial password creation in production systems
- High-security applications

For cryptographic-grade passwords, use `secrets` module or a proper password manager.

## Project Structure

```
.
├── generator.py           # Core password generation logic
├── app.py                 # Streamlit web interface
├── cli.py                 # Command-line interface
├── pwd_gen_tk_app.py      # Tkinter GUI
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Examples

### Example 1: Same seed, same password
```bash
$ python cli.py -s "birthday123" -l 20
k^Af3uXm_zJ!4&QpRvBw

$ python cli.py -s "birthday123" -l 20
k^Af3uXm_zJ!4&QpRvBw  # Identical
```

### Example 2: Different length
```bash
$ python cli.py -s "birthday123" -l 10
k^Af3uXm_z
```

### Example 3: Check strength
```bash
$ python cli.py -s "short" -l 8 -c
abc1!ABC
Strength: ✓ Strong
```

## License

MIT
