# Password Manager

A simple password manager application built with Python and Tkinter. This app allows you to securely generate, store, and retrieve passwords for different websites.

## Features

- **Password Generation:** Generates strong, random passwords including letters, numbers, and symbols.
- **Password Storage:** Saves website, email/username, and password entries to a local JSON file (`data.json`).
- **Password Search:** Quickly search for saved credentials by website name.
- **Clipboard Copy:** Automatically copies generated passwords to your clipboard.
- **User-Friendly GUI:** Easy-to-use graphical interface built with Tkinter.

## Requirements

- Python 3.6+
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [pyperclip](https://pypi.org/project/pyperclip/) (for clipboard functionality)

Other packages listed in `requirements.txt` are not strictly necessary for the password manager, but may be present for your environment.

## Installation

1. **Clone the repository or download the files.**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   If you only need the essentials:
   ```sh
   pip install pyperclip
   ```

## Usage

1. Run the application:
   ```sh
   python main.py
   ```
2. Use the GUI to:
   - Enter a website and your email/username.
   - Generate a secure password or enter your own.
   - Click "Add" to save the credentials.
   - Use "Search" to retrieve saved credentials for a website.

## Files

- [`main.py`](main.py): Main application code.
- `logo.png`: Logo image displayed in the GUI.
- `data.json`: Created automatically to store your passwords (not included in the repo for security).

## Security Notice

- Passwords are stored in plain text in `data.json`. For real-world use, consider encrypting your data.
- Do not share your `data.json` file.

## License

This project is licensed under the MIT License.

Feel free to open issues or submit pull requests for improvements!
