# Assignment 01 – Cryptography (Python + OOP)

**Course:** IT32023 - Information Assurance and Network Security  
**Intake:** Intake11  
**Student Name:** Gihan Sanjula Sandaruwan

---

# 1. Introduction

Cryptography is the science of securing information through mathematical techniques that transform readable data (plaintext) into unreadable formats (ciphertext). This field encompasses two primary categories: **classical cryptography**, which includes traditional substitution and transposition ciphers, and **modern cryptography**, which employs advanced mathematical concepts such as elliptic curve cryptography (ECC) for secure key exchange.

This assignment demonstrates the practical implementation of both classical and modern cryptographic techniques using **Python** programming language with **Object-Oriented Programming (OOP)** principles. The implementation utilizes the **Matplotlib** library for data visualization, enabling frequency analysis of ciphertexts through histogram representations.

The assignment is divided into two main questions: Question 01 focuses on classical cryptography techniques including the Kamasutra substitution cipher, modular function encryption, and frequency analysis. Question 02 implements the Elliptic Curve Diffie-Hellman (ECDH) key exchange protocol, demonstrating secure key establishment between two parties.

---

# 2. Question 01 – Classical Cryptography

## 2.1 Kamasutra Cipher (Substitution)

The Kamasutra cipher, also known as the Vatsyayana cipher, is a classical substitution cipher that operates by pairing letters of the alphabet. Each pair of letters can substitute for each other, creating a bidirectional mapping. This cipher is symmetric, meaning the same operation is used for both encryption and decryption.

### Key Structure

The cipher uses a 26-character key string where adjacent characters form substitution pairs. The given key is:

```
GJMQTVZADIORUBCEFHKLNPSWXY
```

This key creates 13 pairs: (G,J), (M,Q), (T,V), (Z,A), (D,I), (O,R), (U,B), (C,E), (F,H), (K,L), (N,P), (S,W), (X,Y). Each letter in a pair can be substituted with its partner.

### Object-Oriented Implementation

The implementation follows OOP principles by encapsulating the cipher logic within a `KamasutraCipher` class:

```python
class KamasutraCipher:
    """
    Implements the Kamasutra (Vatsyayana) substitution cipher using OOP.
    """

    def __init__(self, key_string: str):
        """
        Initializes the cipher with a 26-character key string.
        Pairs are formed by adjacent characters: (key[0], key[1]), etc.
        """
        if len(key_string) != 26:
            raise ValueError("Key string must be exactly 26 characters.")
        
        self.key_string = key_string.upper()
        self.mapping = self._generate_mapping()

    def _generate_mapping(self) -> dict:
        """Creates the bidirectional substitution dictionary."""
        map_dict = {}
        # Iterate in steps of 2 to create pairs
        for i in range(0, 26, 2):
            char1 = self.key_string[i]
            char2 = self.key_string[i+1]
            map_dict[char1] = char2
            map_dict[char2] = char1
        return map_dict

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the established pairs.
        Non-alphabet characters (like spaces) are preserved.
        """
        plaintext = plaintext.upper()
        ciphertext = []
        
        for char in plaintext:
            if char in self.mapping:
                ciphertext.append(self.mapping[char])
            else:
                ciphertext.append(char)  # Keep spaces/punctuation as is
                
        return "".join(ciphertext)
```

### Encryption Process

The encryption process involves:
1. Converting the plaintext to uppercase
2. For each character, checking if it exists in the mapping dictionary
3. If found, substituting it with its paired character
4. Preserving non-alphabetic characters (spaces, punctuation) as-is

### Example Encryption

**Plaintext:** "Gihan sanjula sandaruwan"

**Ciphertext:** "JDFZP WZPGBKZ WZPIZOBSZP"

[INSERT OUTPUT SCREENSHOT HERE]

---

## 2.2 Modular Function Cipher (Affine Cipher)

The modular function cipher, also known as the Affine cipher, is a type of monoalphabetic substitution cipher that uses modular arithmetic. Each letter is mapped to a numeric value, transformed using a mathematical function, and then mapped back to a letter.

### Alphabet Mapping

The alphabet is mapped to integers as follows:

$$ A = 0, B = 1, C = 2, \ldots, Z = 25 $$

### Encryption Function

The encryption function is defined as:

$$ E(x) = (7x + 6) \mod 26 $$

where:
- $x$ is the numeric value of the plaintext letter (0-25)
- $7$ is the multiplicative coefficient
- $6$ is the additive constant
- $\mod 26$ ensures the result remains within the alphabet range

### Modular Arithmetic Explanation

Modular arithmetic, denoted as $a \mod n$, returns the remainder when $a$ is divided by $n$. This ensures that all results fall within the range $[0, n-1]$, making it ideal for mapping back to the 26-letter alphabet.

### Object-Oriented Implementation

The `ModularCipher` class encapsulates the encryption logic:

```python
class ModularCipher:
    """
    Implements a Modular Function Cipher (Affine Cipher variant).
    Function: f(x) = (ax + b) mod 26
    """

    def __init__(self, a: int = 7, b: int = 6):
        """
        Initializes the modular function with constants a and b.
        Standard for this assignment: f(x) = (7x + 6) mod 26
        """
        self.a = a
        self.b = b
        self.mod = 26

    def _char_to_num(self, char: str) -> int:
        """Converts A-Z to 0-25."""
        return ord(char.upper()) - ord('A')

    def _num_to_char(self, num: int) -> str:
        """Converts 0-25 back to A-Z."""
        return chr((num % self.mod) + ord('A'))

    def encrypt(self, plaintext: str) -> str:
        """
        Applies the transformation f(x) = (7x + 6) mod 26 letter-by-letter.
        """
        plaintext = plaintext.upper()
        ciphertext = []

        for char in plaintext:
            if char.isalpha():
                x = self._char_to_num(char)
                # Apply the modular function
                transformed_val = (self.a * x + self.b) % self.mod
                ciphertext.append(self._num_to_char(transformed_val))
            else:
                # Keep spaces and non-alphabet characters as they are
                ciphertext.append(char)

        return "".join(ciphertext)
```

### Letter-by-Letter Transformation

The transformation is applied independently to each alphabetic character:
1. Convert letter to numeric value (A→0, B→1, ..., Z→25)
2. Apply the function: $(7x + 6) \mod 26$
3. Convert the result back to a letter
4. Non-alphabetic characters remain unchanged

### Example Encryption

**Plaintext:** "Gihan sanjula sandaruwan"

**Ciphertext:** "WKDGT CGTRQFG CGTBGVQEGT"

[INSERT OUTPUT SCREENSHOT HERE]

---

## 2.3 Frequency Analysis and Histogram

Frequency analysis is a cryptanalytic technique that examines the frequency of letters or groups of letters in ciphertext. This method is particularly effective against monoalphabetic substitution ciphers, as it exploits the fact that certain letters appear more frequently in natural language.

### Frequency Calculation

The percentage frequency of each letter is calculated using the formula:

$$ Frequency = \frac{Count}{Total} \times 100 $$

where:
- $Count$ is the number of occurrences of a specific letter
- $Total$ is the total number of alphabetic characters in the ciphertext

### Object-Oriented Implementation

The `FrequencyAnalyzer` class performs frequency analysis and generates visualizations:

```python
class FrequencyAnalyzer:
    """
    Performs frequency analysis on ciphertexts and generates histograms.
    """

    def __init__(self, ciphertext: str, title: str):
        self.ciphertext = ciphertext.upper()
        self.title = title
        self.alphabet = string.ascii_uppercase
        self.frequencies = self._calculate_frequencies()

    def _calculate_frequencies(self) -> dict:
        """Counts the occurrence of each letter A-Z."""
        # Filter only alphabetical characters
        filtered_text = [char for char in self.ciphertext if char in self.alphabet]
        total_chars = len(filtered_text)
        
        # Initialize counts for all letters to 0
        counts = {letter: 0 for letter in self.alphabet}
        
        for char in filtered_text:
            counts[char] += 1
            
        # Convert to percentages
        if total_chars > 0:
            return {letter: (count / total_chars) * 100 for letter, count in counts.items()}
        return counts

    def plot_histogram(self):
        """Generates and displays a Matplotlib histogram with percentage labels."""
        letters = list(self.frequencies.keys())
        percentages = list(self.frequencies.values())

        plt.figure(figsize=(12, 6))
        bars = plt.bar(letters, percentages, color='skyblue', edgecolor='navy')

        # Add labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            if height > 0:  # Only label bars that have a value
                plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                         f'{height:.1f}%', ha='center', va='bottom', fontsize=8, rotation=0)

        plt.xlabel('Letters')
        plt.ylabel('Percentage Frequency (%)')
        plt.title(f'Frequency Analysis: {self.title}')
        plt.ylim(0, max(percentages) + 10 if percentages else 100)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.show()
```

### Visualization

The Matplotlib library is used to create bar charts (histograms) that visually represent the frequency distribution. Each bar corresponds to a letter (A-Z), and the height represents its percentage frequency. Percentage labels are displayed on top of each bar for clarity.

### Histogram Results

[INSERT HISTOGRAM IMAGE HERE - Kamasutra Ciphertext]

[INSERT HISTOGRAM IMAGE HERE - Modular Function Ciphertext]

---

# 3. Question 02 – Elliptic Curve Diffie-Hellman (ECDH)

## 3.1 Elliptic Curve Definition

Elliptic Curve Cryptography (ECC) is a modern cryptographic approach that provides strong security with smaller key sizes compared to traditional methods. An elliptic curve over a finite field is defined by the equation:

$$ y^2 = x^3 + ax + b \pmod{p} $$

where:
- $a$ and $b$ are coefficients that define the curve
- $p$ is a prime number that defines the finite field
- All operations are performed modulo $p$

### Curve Parameters

For this implementation, the following small values are chosen:

- $a = 2$
- $b = 2$
- $p = 17$ (prime number)

Thus, the curve equation becomes:

$$ y^2 = x^3 + 2x + 2 \pmod{17} $$

### Object-Oriented Implementation

The `EllipticCurve` class encapsulates the curve operations:

```python
class EllipticCurve:
    """Represents an elliptic curve y^2 = x^3 + ax + b (mod p)."""
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, x, y):
        """Checks if a point (x, y) lies on the curve."""
        if x is None: return True  # Point at infinity
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def point_addition(self, P, Q):
        """Adds two points P and Q on the curve."""
        if P is None: return Q
        if Q is None: return P
        
        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and (y1 != y2 or y1 == 0):
            return None  # Point at infinity

        if x1 == x2:
            # Point doubling
            m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p)
        else:
            # Point addition
            m = (y2 - y1) * pow(x2 - x1, -1, self.p)

        m %= self.p
        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_multiplication(self, k, P):
        """Computes k * P using the double-and-add algorithm."""
        result = None
        addend = P
        while k:
            if k & 1:
                result = self.point_addition(result, addend)
            addend = self.point_addition(addend, addend)
            k >>= 1
        return result
```

---

## 3.2 Base Point Verification

A base point $G$ is a point on the elliptic curve that serves as a generator for the cryptographic operations. The base point must satisfy the curve equation.

### Base Point Selection

The base point chosen is:

$$ G = (5, 1) $$

### Verification

To verify that $(5, 1)$ lies on the curve, we substitute into the curve equation:

$$ y^2 = x^3 + 2x + 2 \pmod{17} $$

$$ 1^2 = 5^3 + 2(5) + 2 \pmod{17} $$

$$ 1 = 125 + 10 + 2 \pmod{17} $$

$$ 1 = 137 \pmod{17} $$

$$ 1 = 137 - 8(17) = 137 - 136 = 1 \pmod{17} $$

Since $1 \equiv 1 \pmod{17}$, the point $(5, 1)$ satisfies the curve equation and is a valid base point.

---

## 3.3 Key Generation

The Elliptic Curve Diffie-Hellman (ECDH) key exchange protocol allows two parties to establish a shared secret key over an insecure channel.

### Private Key

Each user selects a private key $d$, which is a random integer. This key must be kept secret.

- **Tim's Private Key:** $d_T = 3$
- **Stephen's Private Key:** $d_S = 7$

### Public Key

The public key is computed by multiplying the private key with the base point:

$$ Q = d \cdot G $$

where:
- $Q$ is the public key (a point on the curve)
- $d$ is the private key
- $G$ is the base point
- The multiplication is scalar multiplication on the elliptic curve

### Point Multiplication

Scalar multiplication $k \cdot P$ is computed by repeatedly adding point $P$ to itself $k$ times. The implementation uses the efficient double-and-add algorithm, which reduces the number of operations from $O(k)$ to $O(\log k)$.

### Object-Oriented Implementation

The `ECCUser` class represents a participant in the key exchange:

```python
class ECCUser:
    """Represents a user (like Tim or Stephen) in the ECDH exchange."""
    def __init__(self, name, curve, base_point, private_key):
        self.name = name
        self.curve = curve
        self.base_point = base_point
        self.private_key = private_key
        # Public Key = private_key * Base_Point
        self.public_key = self.curve.scalar_multiplication(private_key, base_point)

    def compute_shared_secret(self, other_public_key):
        """Shared Secret = my_private_key * other_public_key."""
        return self.curve.scalar_multiplication(self.private_key, other_public_key)
```

### Key Generation Results

- **Tim's Private Key:** $d_T = 3$
- **Tim's Public Key:** $Q_T = 3 \cdot G = (10, 6)$

- **Stephen's Private Key:** $d_S = 7$
- **Stephen's Public Key:** $Q_S = 7 \cdot G = (0, 6)$

[INSERT OUTPUT SCREENSHOT HERE]

---

## 3.4 Shared Secret Computation

After exchanging public keys, each party computes the shared secret by multiplying their private key with the other party's public key.

### Mathematical Foundation

The shared secret is computed as:

$$ Shared = d_T \cdot Q_S = d_S \cdot Q_T $$

Substituting the public key definitions:

$$ Shared = d_T \cdot (d_S \cdot G) = d_S \cdot (d_T \cdot G) $$

By the associativity of scalar multiplication:

$$ Shared = d_T \cdot d_S \cdot G = d_S \cdot d_T \cdot G $$

This demonstrates that both parties will compute the same shared secret point.

### Computation Process

**Tim computes:**
$$ Shared_T = d_T \cdot Q_S = 3 \cdot (0, 6) = (6, 3) $$

**Stephen computes:**
$$ Shared_S = d_S \cdot Q_T = 7 \cdot (10, 6) = (6, 3) $$

### Verification

Both parties obtain the same shared secret point $(6, 3)$, confirming the correctness of the ECDH protocol implementation.

### Output Results

```
Tim's Private Key:     3
Tim's Public Key:      (10, 6)

Stephen's Private Key: 7
Stephen's Public Key:  (0, 6)

Tim's Shared Key:     (6, 3)
Stephen's Shared Key: (6, 3)

[VERIFICATION SUCCESS]: Both users obtained the same shared key.
```

[INSERT OUTPUT SCREENSHOT HERE]

---

# 4. Conclusion

This assignment successfully demonstrates the implementation of both classical and modern cryptographic techniques using Python and Object-Oriented Programming principles. The classical cryptography section (Question 01) illustrated substitution ciphers through the Kamasutra cipher and modular arithmetic through the Affine cipher, while frequency analysis provided insights into cryptanalytic techniques.

The modern cryptography section (Question 02) implemented the Elliptic Curve Diffie-Hellman key exchange protocol, demonstrating how two parties can securely establish a shared secret over an insecure channel. The implementation verified that both parties compute identical shared keys, confirming the mathematical correctness of the ECDH protocol.

Key learning outcomes include:
- Understanding of classical substitution ciphers and their vulnerabilities
- Application of modular arithmetic in cryptographic transformations
- Frequency analysis as a cryptanalytic tool
- Elliptic curve mathematics and point operations
- Secure key exchange protocols using public-key cryptography
- Object-Oriented Programming principles in cryptographic system design

The use of OOP throughout the implementation enhanced code organization, reusability, and maintainability. The Matplotlib visualizations provided clear insights into ciphertext frequency distributions, demonstrating the practical application of data visualization in cryptanalysis.

This assignment reinforces the importance of both theoretical understanding and practical implementation in the field of information assurance and network security.

