# src/ciphers/modular.py

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

    def decrypt(self, ciphertext: str) -> str:
        """
        Note: Decryption for Affine ciphers requires the modular 
        multiplicative inverse of 'a'. 
        For this assignment, only generation (encryption) is explicitly asked.
        """
        # Finding modular inverse of 7 mod 26 is 15
        # inverse_a = 15
        # x = inverse_a * (y - b) mod 26
        pass