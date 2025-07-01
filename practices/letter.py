

from itertools import combinations

def solve(s):
    max_len = 0
    best_str = ""
    for a, b in combinations(set(s), 2):
        # Keep only these 2 characters
        new_s = ''.join(c for c in s if c == a or c == b)
        # Check if alternating (no same adjacent chars)
        if len(new_s) > 1 and all(new_s[i] != new_s[i+1] for i in range(len(new_s)-1)):
            if len(new_s) > max_len:
                max_len = len(new_s)
                best_str = new_s
    return best_str, max_len

def main():
    user_string = input("Enter a string: ")
    alt_str, result = solve(user_string)
    print(f"Input: '{user_string}'")
    print(f"Longest alternating string: '{alt_str}'")
    print(f"Length: {result}")

if __name__ == "__main__":
    main()