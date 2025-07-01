from itertools import combinations

def solve(s):
    max_len = 0
    
    
    for a, b in combinations(set(s), 2):
        # Keep only these 2 characters
        new_s = ''.join(c for c in s if c == a or c == b)
        
        # Check if alternating (no same adjacent chars)
        if len(new_s) > 0 and all(new_s[i] != new_s[i+1] for i in range(len(new_s)-1)):
            max_len = max(max_len, len(new_s))
    
    return max_len

def main():
    user_string = input("Enter a string: ")
    result = solve(user_string)
    print(f"Input: '{user_string}'")
    print(f"Output: {result}")

if __name__ == "__main__":
    main()