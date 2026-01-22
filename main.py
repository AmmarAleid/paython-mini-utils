from paython_utils.string_utils import reverse_string, count_vowels
from paython_utils.math_utils import add, is_even
def main():
    print("String utilities:")
    print("Reverse:", reverse_string("Paython"))
    print("Vowels:", count_vowels("Paython"))

    print("\nMath utilities:")
    print("Add:", add(5, 3))
    print("Is even (10):", is_even(10))
    print("Is even (7):", is_even(7))


if __name__ == "__main__":
    main()