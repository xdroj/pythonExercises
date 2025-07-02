Credit Card Validator (Luhn Algorithm)
This project implements a credit card number validation utility using the Luhn Algorithm (also known as the modulus 10 or mod 10 algorithm). The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, and Canadian Social Insurance Numbers.

Features
Luhn Algorithm Implementation: Core logic for validating numbers based on the Luhn formula.

Flexible Input: Handles credit card numbers with common separators like hyphens (-) and spaces (     ).

Clear Output: Prints "VALID!" or "INVALID!" based on the validation result.

How the Luhn Algorithm Works
The verify_card_number function performs the following steps as per the Luhn algorithm:

Reverse the Card Number: The digits of the credit card number are processed from right to left.

Sum of Odd-Positioned Digits: Starting from the rightmost digit (which is considered position 1, an "odd" position), every digit at an odd position is added to sum_of_odd_digits.

Sum of Doubled Even-Positioned Digits: Starting from the second digit from the right (position 2, an "even" position), every digit at an even position is doubled.

If doubling a digit results in a two-digit number (e.g., 7 * 2 = 14), the digits of that two-digit number are summed (e.g., 1 + 4 = 5).

These results are added to sum_of_even_digits.

Total Sum: The sum_of_odd_digits and sum_of_even_digits are added together.

Validation: If the total sum is a multiple of 10 (i.e., total % 10 == 0), the card number is considered VALID. Otherwise, it's INVALID.

Files
main.py (or your Python script name): Contains the credit card validation logic.

Usage
To use the validator, simply run the Python script. The main() function is set up to test a sample card number.

Functions
verify_card_number(card_number):

Takes a card_number (string) as input. This number should contain only digits (no spaces or hyphens).

Applies the Luhn algorithm to determine validity.

Returns True if the card number is valid, False otherwise.

main():

Defines a sample card_number string which may include separators.

Uses str.maketrans and translate to remove spaces and hyphens from the card_number.

Calls verify_card_number with the cleaned number.

Prints "VALID!" or "INVALID!" to the console.

Example
The provided code includes a main function to demonstrate its use:

Python

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142' # Example: A valid test card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
When you run this script, it will output:

VALID!