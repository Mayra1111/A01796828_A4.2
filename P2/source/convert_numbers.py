#!/usr/bin/env python3
"""
Number conversion program.

This program reads decimal numbers from a file, extracts the last
two decimal digits, and converts them to binary and hexadecimal bases
using basic algorithms.
"""

import sys
import time


def decimal_to_binary(decimal_num):
    """
    Convert a decimal number to binary using basic algorithm.

    Args:
        decimal_num: Integer decimal number

    Returns:
        str: Binary representation as string
    """
    if decimal_num == 0:
        return "0"

    binary = ""
    num = abs(int(decimal_num))

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    return binary if decimal_num >= 0 else "-" + binary


def decimal_to_hexadecimal(decimal_num):
    """
    Convert a decimal number to hexadecimal using basic algorithm.

    Args:
        decimal_num: Integer decimal number

    Returns:
        str: Hexadecimal representation as string
    """
    if decimal_num == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    num = abs(int(decimal_num))

    while num > 0:
        remainder = num % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        num = num // 16

    return hexadecimal if decimal_num >= 0 else "-" + hexadecimal


def get_last_two_decimal_digits(number):
    """
    Extract last two decimal digits from a number.

    Args:
        number: Integer number

    Returns:
        int: Last two decimal digits
    """
    return abs(int(number)) % 100


def read_numbers_from_file(filename):
    """
    Read numbers from a file.

    Args:
        filename: Path to the file containing numbers

    Returns:
        list: List of numeric values
    """
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        value = int(line)
                        numbers.append(value)
                    except ValueError:
                        print(f"Warning: Invalid data at line {line_number}: "
                              f"'{line}' - Skipping")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        raise
    except Exception as error:
        print(f"Error reading file: {error}")
        raise

    return numbers


def save_conversion_results(filename, conversions, elapsed_time):
    """
    Save conversion results to a file.

    Args:
        filename: Output filename
        conversions: List of conversion dictionaries
        elapsed_time: Time elapsed for computation
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("NUMBER CONVERSION REPORT\n")
            file.write("=" * 70 + "\n\n")

            # Header
            file.write(f"{'Index':<8}{'Decimal':<15}{'Last 2':<10}"
                       f"{'Binary':<15}{'Hex':<10}\n")
            file.write("-" * 70 + "\n")

            # Data rows
            for i, conv in enumerate(conversions, 1):
                file.write(f"{i:<8}{conv['decimal']:<15}"
                           f"{conv['last_two']:<10}"
                           f"{conv['binary']:<15}"
                           f"{conv['hex']:<10}\n")

            file.write("\n")
            file.write(f"Total numbers processed: {len(conversions)}\n")
            file.write(f"Elapsed Time: {elapsed_time:.6f} seconds\n")

        print(f"\nResults saved to {filename}")
    except Exception as error:
        print(f"Error saving results: {error}")


def display_conversion_results(conversions, elapsed_time):
    """
    Display conversion results on screen.

    Args:
        conversions: List of conversion dictionaries
        elapsed_time: Time elapsed for computation
    """
    print("\n" + "=" * 70)
    print("NUMBER CONVERSION REPORT")
    print("=" * 70)

    # Header
    print(f"{'Index':<8}{'Decimal':<15}{'Last 2':<10}"
          f"{'Binary':<15}{'Hex':<10}")
    print("-" * 70)

    # Show first 10 conversions
    display_count = min(10, len(conversions))
    for i in range(display_count):
        conv = conversions[i]
        print(f"{i+1:<8}{conv['decimal']:<15}"
              f"{conv['last_two']:<10}"
              f"{conv['binary']:<15}"
              f"{conv['hex']:<10}")

    if len(conversions) > 10:
        print(f"... and {len(conversions) - 10} more")

    print("=" * 70)
    print(f"Total numbers processed: {len(conversions)}")
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")
    print("=" * 70)


def main():
    """Main program function."""
    if len(sys.argv) < 2:
        print("Usage: python convert_numbers.py fileWithData.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = "ConvertionResults.txt"

    print(f"Processing file: {input_filename}")

    try:
        # Start timing
        start_time = time.time()

        # Read numbers
        numbers = read_numbers_from_file(input_filename)

        if not numbers:
            print("Error: No valid numbers found in file")
            sys.exit(1)

        # Perform conversions
        conversions = []
        for num in numbers:
            last_two = get_last_two_decimal_digits(num)
            binary = decimal_to_binary(last_two)
            hexadecimal = decimal_to_hexadecimal(last_two)

            conversion = {
                'decimal': num,
                'last_two': last_two,
                'binary': binary,
                'hex': hexadecimal
            }
            conversions.append(conversion)

        # End timing
        elapsed_time = time.time() - start_time

        # Display and save results
        display_conversion_results(conversions, elapsed_time)
        save_conversion_results(output_filename, conversions, elapsed_time)

        print("\nProgram completed successfully!")

    except FileNotFoundError:
        print("Error: Input file not found")
        sys.exit(1)
    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
