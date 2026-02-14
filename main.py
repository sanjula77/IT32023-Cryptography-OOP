import os
import matplotlib.pyplot as plt

# Import custom modules
from src.ciphers.kamasutra import KamasutraCipher
from src.ciphers.modular import ModularCipher
from src.ciphers.ecc_system import EllipticCurve, ECCUser
from src.analysis import FrequencyAnalyzer

def main():
    # --- Configuration ---
    full_name = "Gihan sanjula sandaruwan" 
    kamasutra_key = "GJMQTVZADIORUBCEFHKLNPSWXY"

    print("="*60)
    print("IT32023 - Information Assurance and Network Security")
    print(f"Student: {full_name}")
    print("="*60)

    # --- QUESTION 01: Classical Cryptography ---
    print("\n[QUESTION 01]")
    
    # Part (a): Kamasutra Cipher
    kama_cipher = KamasutraCipher(kamasutra_key)
    kama_ct = kama_cipher.encrypt(full_name)
    print(f"(a) Kamasutra Ciphertext: {kama_ct}")

    # Part (b): Modular Function Cipher f(x) = (7x + 6) mod 26
    mod_cipher = ModularCipher(a=7, b=6)
    mod_ct = mod_cipher.encrypt(full_name)
    print(f"(b) Modular Ciphertext:   {mod_ct}")

    # Part (c): Frequency Analysis
    print("\n(c) Generating Histograms... (Please close plot windows to continue)")
    kama_analyzer = FrequencyAnalyzer(kama_ct, "Kamasutra Ciphertext")
    kama_analyzer.plot_histogram()
    
    mod_analyzer = FrequencyAnalyzer(mod_ct, "Modular Function Ciphertext")
    mod_analyzer.plot_histogram()


    # --- QUESTION 02: Elliptic Curve Diffie-Hellman ---
    print("\n" + "="*60)
    print("[QUESTION 02]: ECC Key Exchange")
    print("="*60)

    # a) Define Curve: y^2 = x^3 + 2x + 2 (mod 17)
    curve = EllipticCurve(a=2, b=2, p=17)
    
    # b) Base Point G
    G = (5, 1) 
    print(f"Curve: y^2 = x^3 + 2x + 2 (mod 17) | Base Point G: {G}")

    # c) & d) Tim and Stephen's Keys
    tim = ECCUser("Tim", curve, G, private_key=3)
    stephen = ECCUser("Stephen", curve, G, private_key=7)

    print(f"\nTim's Private Key:     {tim.private_key}")
    print(f"Tim's Public Key:      {tim.public_key}")
    
    print(f"\nStephen's Private Key: {stephen.private_key}")
    print(f"Stephen's Public Key:  {stephen.public_key}")

    # e) Compute Shared Secret
    tim_shared = tim.compute_shared_secret(stephen.public_key)
    stephen_shared = stephen.compute_shared_secret(tim.public_key)

    # f) Verification
    print(f"\nTim's Shared Key:     {tim_shared}")
    print(f"Stephen's Shared Key: {stephen_shared}")

    if tim_shared == stephen_shared:
        print("\n[VERIFICATION SUCCESS]: Both users obtained the same shared key.")
    else:
        print("\n[VERIFICATION FAILED]: Shared keys do not match.")

    print("\n" + "="*60)
    print("Assignment Execution Finished.")

if __name__ == "__main__":
    main()