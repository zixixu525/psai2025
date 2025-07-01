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
    # Test with the example
    test_string = "abaacdabd"
    result = solve(test_string)
    print(f"Input: '{test_string}'")
    print(f"Output: {result}")
    
    # Test with more examples
    test_cases = ["beabeefeab", "aab", "aaa", "ab"]
    for test in test_cases:
        print(f"Input: '{test}' -> Output: {solve(test)}")

if __name__ == "__main__":
    main()