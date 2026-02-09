#!/usr/bin/env python3
"""
Word counting program.

This program reads text from a file and counts the frequency
of distinct words.
"""

import sys
import time


def read_words_from_file(filename):
    """
    Read words from a file.

    Args:
        filename: Path to the file containing text

    Returns:
        list: List of words
    """
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        # Split by whitespace and filter empty strings
                        line_words = [w.strip() for w in line.split()
                                      if w.strip()]
                        words.extend(line_words)
                    except Exception as error:
                        print(f"Warning: Error processing line "
                              f"{line_number}: {error}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        raise
    except Exception as error:
        print(f"Error reading file: {error}")
        raise

    return words


def count_word_frequencies(words):
    """
    Count frequency of each distinct word.

    Args:
        words: List of words

    Returns:
        dict: Dictionary with word frequencies
    """
    frequency = {}

    for word in words:
        # Convert to lowercase for case-insensitive counting
        word_lower = word.lower()
        frequency[word_lower] = frequency.get(word_lower, 0) + 1

    return frequency


def sort_word_frequencies(frequency):
    """
    Sort word frequencies alphabetically.

    Args:
        frequency: Dictionary with word frequencies

    Returns:
        list: List of tuples (word, frequency) sorted alphabetically
    """
    # Manual sorting using basic algorithm
    items = list(frequency.items())

    # Bubble sort implementation
    length = len(items)
    for i in range(length):
        for j in range(0, length - i - 1):
            if items[j][0] > items[j + 1][0]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def save_word_count_results(filename, sorted_frequencies, total_words,
                             distinct_words, elapsed_time):
    """
    Save word count results to a file.

    Args:
        filename: Output filename
        sorted_frequencies: List of (word, frequency) tuples
        total_words: Total word count
        distinct_words: Count of distinct words
        elapsed_time: Time elapsed for computation
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("WORD FREQUENCY REPORT\n")
            file.write("=" * 60 + "\n\n")

            # Header
            file.write(f"{'Word':<30}{'Frequency':<15}\n")
            file.write("-" * 60 + "\n")

            # Word frequencies
            for word, frequency in sorted_frequencies:
                file.write(f"{word:<30}{frequency:<15}\n")

            file.write("\n")
            file.write(f"Total words: {total_words}\n")
            file.write(f"Distinct words: {distinct_words}\n")
            file.write(f"Elapsed Time: {elapsed_time:.6f} seconds\n")

        print(f"\nResults saved to {filename}")
    except Exception as error:
        print(f"Error saving results: {error}")


def display_word_count_results(sorted_frequencies, total_words,
                                distinct_words, elapsed_time):
    """
    Display word count results on screen.

    Args:
        sorted_frequencies: List of (word, frequency) tuples
        total_words: Total word count
        distinct_words: Count of distinct words
        elapsed_time: Time elapsed for computation
    """
    print("\n" + "=" * 60)
    print("WORD FREQUENCY REPORT")
    print("=" * 60)

    # Header
    print(f"{'Word':<30}{'Frequency':<15}")
    print("-" * 60)

    # Show first 20 words
    display_count = min(20, len(sorted_frequencies))
    for i in range(display_count):
        word, frequency = sorted_frequencies[i]
        print(f"{word:<30}{frequency:<15}")

    if len(sorted_frequencies) > 20:
        print(f"... and {len(sorted_frequencies) - 20} more")

    print("=" * 60)
    print(f"Total words: {total_words}")
    print(f"Distinct words: {distinct_words}")
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")
    print("=" * 60)


def main():
    """Main program function."""
    if len(sys.argv) < 2:
        print("Usage: python word_count.py fileWithData.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = "WordCountResults.txt"

    print(f"Processing file: {input_filename}")

    try:
        # Start timing
        start_time = time.time()

        # Read words
        words = read_words_from_file(input_filename)

        if not words:
            print("Error: No valid words found in file")
            sys.exit(1)

        # Count frequencies
        frequency = count_word_frequencies(words)

        # Sort alphabetically
        sorted_frequencies = sort_word_frequencies(frequency)

        # Calculate statistics
        total_words = len(words)
        distinct_words = len(frequency)

        # End timing
        elapsed_time = time.time() - start_time

        # Display and save results
        display_word_count_results(sorted_frequencies, total_words,
                                    distinct_words, elapsed_time)
        save_word_count_results(output_filename, sorted_frequencies,
                                 total_words, distinct_words, elapsed_time)

        print("\nProgram completed successfully!")

    except FileNotFoundError:
        print("Error: Input file not found")
        sys.exit(1)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
