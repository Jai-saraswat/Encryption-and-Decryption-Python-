# Encryption and Decryption System 🔒💻

This project implements an encryption and decryption system using a combination of various techniques, including XOR cipher, Caesar cipher, and custom methods like adding random characters at the start/end of strings and reversing text. The system allows users to encrypt and decrypt messages with a randomly generated key and a sequence of encryption steps.

## Features 🌟

- **Multiple Encryption Techniques**: Includes XOR cipher, Caesar cipher, and custom methods for adding random characters, reversing text, and more. 🔑
- **Randomized Key Generation**: Encryption is performed using a randomly generated key for better security. 🔐
- **Encryption and Decryption Functions**: Encrypt and decrypt messages securely using the provided key. 🔄
- **Flexible and Extensible**: Easily extendable with more encryption methods. 🔧

## Techniques Used 🛠️

- **Caesar Cipher**: Shifts the characters in the string by a specified number. 🔠
- **XOR Cipher**: Uses a bitwise XOR operation with a randomly generated key. 🔲
- **Random Character Insertion**: Inserts random characters at the start or end of the string to obfuscate the plaintext. ✨
- **String Reversal**: Reverses the entire string for added complexity. 🔄
- **Random Word Insertion**: Adds random words in between original words. 📚
- **Word Repeats**: Repeats words multiple times within the text for obfuscation. 🔁

## Installation ⚙️

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/encryption-decryption-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd encryption-decryption-system
    ```

3. Install any dependencies (if required). This project doesn't have any external dependencies, but if you plan to add additional features, you may need libraries like `base64` or `pickle`.

## Usage 🖥️

1. **Encrypt a message**:

   To encrypt a message, use the provided `encryption.py` script. The script will output the encrypted message and the key used for encryption.

   **Run the command**:
    ```bash
    python encryption.py
    ```

   **Sample Output**:
    ```
    Encrypted Text: [85, 56, 89, 110]
    Random Key: 42
    ```

2. **Decrypt a message**:

   To decrypt an encrypted message, use the `decryption.py` script. It will ask for the encrypted data and the corresponding key to restore the original message.

   **Run the command**:
    ```bash
    python decryption.py
    ```

   **Sample Output**:
    ```
    Decrypted Text: "Hello, World!"
    ```

## Example Workflow 🔄

1. **Encryption**:

   **Run the command**:
    ```bash
    python encryption.py
    ```

   **Sample Output**:
    ```
    Encrypted Text: [85, 56, 89, 110]
    Random Key: 42
    ```

2. **Decryption**:

   **Run the command**:
    ```bash
    python decryption.py
    ```

   **Sample Output**:
    ```
    Decrypted Text: "Hello, World!"
    ```

## Contributing 🤝

Feel free to fork this repository, make improvements, or contribute new features. If you find any bugs or have suggestions, please open an issue or create a pull request.

---

🔒 **Security**: This system is suitable for educational and experimental purposes. Always ensure that you use strong, tested encryption algorithms for production environments.

Happy coding! 💻✨
