#!/usr/bin/env python3
"""
Statistical computation program.

This program reads numeric data from a file and calculates
descriptive statistics including mean, median, mode, standard deviation,
and variance.
"""

import sys
import time


def read_data_from_file(filename):
    """
    Read numeric data from a file.

    Args:
        filename: Path to the file containing numeric data

    Returns:
        list: List of numeric values

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file contains invalid data
    """
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        value = float(line)
                        data.append(value)
                    except ValueError:
                        print(f"Warning: Invalid data at line {line_number}: "
                              f"'{line}' - Skipping")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        raise
    except Exception as error:
        print(f"Error reading file: {error}")
        raise

    return data


def calculate_mean(data):
    """
    Calculate the arithmetic mean.

    Args:
        data: List of numeric values

    Returns:
        float: The mean value
    """
    if not data:
        return 0
    return sum(data) / len(data)


def calculate_median(data):
    """
    Calculate the median value.

    Args:
        data: List of numeric values

    Returns:
        float: The median value
    """
    if not data:
        return 0

    sorted_data = sorted(data)
    length = len(sorted_data)

    if length % 2 == 0:
        # Even number of elements: average of two middle values
        mid1 = sorted_data[length // 2 - 1]
        mid2 = sorted_data[length // 2]
        return (mid1 + mid2) / 2
    # Odd number of elements: middle value
    return sorted_data[length // 2]


def calculate_mode(data):
    """
    Calculate the mode (most frequent value).

    Args:
        data: List of numeric values

    Returns:
        float: The mode value
    """
    if not data:
        return 0

    # Count frequencies
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    # Find maximum frequency
    max_frequency = max(frequency.values())

    # Return first value with maximum frequency
    for value in data:
        if frequency[value] == max_frequency:
            return value

    return 0


def calculate_population_std_dev(data):
    """
    Calculate population standard deviation.

    Args:
        data: List of numeric values

    Returns:
        float: Population standard deviation
    """
    if not data:
        return 0

    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)
    return variance ** 0.5


def calculate_population_variance(data):
    """
    Calculate population variance.

    Args:
        data: List of numeric values

    Returns:
        float: Population variance
    """
    if not data:
        return 0

    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / (len(data) - 1)


def save_results(filename, statistics, elapsed_time):
    """
    Save statistical results to a file.

    Args:
        filename: Output filename
        statistics: Dictionary with statistical results
        elapsed_time: Time elapsed for computation
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("DESCRIPTIVE STATISTICS REPORT\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"Count: {statistics['count']}\n")
            file.write(f"Mean: {statistics['mean']:.2f}\n")
            file.write(f"Median: {statistics['median']:.2f}\n")
            file.write(f"Mode: {statistics['mode']}\n")
            file.write(f"Population Std Dev: "
                       f"{statistics['std_dev']:.15f}\n")
            file.write(f"Population Variance: "
                       f"{statistics['variance']:.15f}\n\n")

            file.write(f"Elapsed Time: {elapsed_time:.6f} seconds\n")

        print(f"\nResults saved to {filename}")
    except Exception as error:
        print(f"Error saving results: {error}")


def display_results(statistics, elapsed_time):
    """
    Display statistical results on screen.

    Args:
        statistics: Dictionary with statistical results
        elapsed_time: Time elapsed for computation
    """
    print("\n" + "=" * 50)
    print("DESCRIPTIVE STATISTICS REPORT")
    print("=" * 50)
    print(f"Count: {statistics['count']}")
    print(f"Mean: {statistics['mean']:.2f}")
    print(f"Median: {statistics['median']:.2f}")
    print(f"Mode: {statistics['mode']}")
    print(f"Population Std Dev: {statistics['std_dev']:.15f}")
    print(f"Population Variance: {statistics['variance']:.15f}")
    print("=" * 50)
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")
    print("=" * 50)


def main():
    """Main program function."""
    if len(sys.argv) < 2:
        print("Usage: python compute_statistics.py fileWithData.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = "StatisticsResults.txt"

    print(f"Processing file: {input_filename}")

    try:
        # Start timing
        start_time = time.time()

        # Read data
        data = read_data_from_file(input_filename)

        if not data:
            print("Error: No valid data found in file")
            sys.exit(1)

        # Calculate statistics
        statistics = {
            'count': len(data),
            'mean': calculate_mean(data),
            'median': calculate_median(data),
            'mode': calculate_mode(data),
            'std_dev': calculate_population_std_dev(data),
            'variance': calculate_population_variance(data)
        }

        # End timing
        elapsed_time = time.time() - start_time

        # Display and save results
        display_results(statistics, elapsed_time)
        save_results(output_filename, statistics, elapsed_time)

        print("\nProgram completed successfully!")

    except FileNotFoundError:
        print("Error: Input file not found")
        sys.exit(1)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
