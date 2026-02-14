# IT32023 – Cryptography Assignment (Python + OOP)

A comprehensive implementation of classical and modern cryptography techniques using Python and Object-Oriented Programming principles. This project demonstrates substitution ciphers, modular arithmetic encryption, frequency analysis, and elliptic curve cryptography for secure key exchange.

## Features

- **Kamasutra Cipher**: Classical substitution cipher using paired letter mappings
- **Affine Cipher**: Modular function encryption using $E(x) = (7x + 6) \mod 26$
- **Frequency Analysis**: Statistical analysis of ciphertexts with Matplotlib visualizations
- **Elliptic Curve Diffie-Hellman (ECDH)**: Secure key exchange protocol implementation

## Project Structure

```
IT32023_Assignment01/
│
├── main.py                 # Main execution script
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
│
└── src/
    ├── __init__.py
    ├── analysis.py         # FrequencyAnalyzer class
    ├── utils.py           # Utility functions
    │
    └── ciphers/
        ├── __init__.py
        ├── kamasutra.py    # KamasutraCipher class
        ├── modular.py      # ModularCipher class
        └── ecc_system.py   # EllipticCurve and ECCUser classes
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or download this repository

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main program:

```bash
python main.py
```

The program will:
1. Encrypt a plaintext using Kamasutra cipher
2. Encrypt the same plaintext using the modular function cipher
3. Generate frequency analysis histograms for both ciphertexts
4. Demonstrate ECDH key exchange between two users (Tim and Stephen)

## Example Output

```
============================================================
IT32023 - Information Assurance and Network Security
Student: Gihan sanjula sandaruwan
============================================================

[QUESTION 01]
(a) Kamasutra Ciphertext: JDFZP WZPGBKZ WZPIZOBSZP
(b) Modular Ciphertext:   WKDGT CGTRQFG CGTBGVQEGT

(c) Generating Histograms... (Please close plot windows to continue)

============================================================
[QUESTION 02]: ECC Key Exchange
============================================================
Curve: y^2 = x^3 + 2x + 2 (mod 17) | Base Point G: (5, 1)

Tim's Private Key:     3
Tim's Public Key:      (10, 6)

Stephen's Private Key: 7
Stephen's Public Key:  (0, 6)

Tim's Shared Key:     (6, 3)
Stephen's Shared Key: (6, 3)

[VERIFICATION SUCCESS]: Both users obtained the same shared key.

============================================================
Assignment Execution Finished.
```

## Technologies Used

- **Python 3.7+**: Core programming language
- **Object-Oriented Programming**: Encapsulation, classes, and methods
- **Modular Arithmetic**: Mathematical operations for cipher transformations
- **Elliptic Curve Cryptography**: Modern public-key cryptography
- **Matplotlib**: Data visualization and histogram generation

## Object-Oriented Design

The project follows OOP principles with dedicated classes for each cryptographic component:

- `KamasutraCipher`: Handles substitution cipher encryption/decryption
- `ModularCipher`: Implements affine cipher with modular arithmetic
- `FrequencyAnalyzer`: Performs statistical analysis and visualization
- `EllipticCurve`: Manages curve operations (point addition, scalar multiplication)
- `ECCUser`: Represents participants in the ECDH key exchange

Each class encapsulates its data and methods, promoting code reusability and maintainability.

## Learning Outcomes

This project demonstrates:

- Implementation of classical substitution ciphers
- Application of modular arithmetic in cryptography
- Frequency analysis as a cryptanalytic technique
- Elliptic curve mathematics and point operations
- Secure key exchange protocols using public-key cryptography
- Object-Oriented Programming best practices in cryptographic systems

## Dependencies

- `matplotlib >= 3.5.0`: For histogram generation and data visualization

## License

Academic use only. This project is part of the IT32023 - Information Assurance and Network Security course assignment.

