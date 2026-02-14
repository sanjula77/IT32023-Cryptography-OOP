# src/ciphers/kamasutra.py

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

    def decrypt(self, ciphertext: str) -> str:
        """In Kamasutra, encryption and decryption are identical."""
        return self.encrypt(ciphertext)