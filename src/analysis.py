# src/analysis.py
import matplotlib.pyplot as plt
import string

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
            if height > 0: # Only label bars that have a value
                plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                         f'{height:.1f}%', ha='center', va='bottom', fontsize=8, rotation=0)

        plt.xlabel('Letters')
        plt.ylabel('Percentage Frequency (%)')
        plt.title(f'Frequency Analysis: {self.title}')
        plt.ylim(0, max(percentages) + 10 if percentages else 100) # Give room for labels
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.show()