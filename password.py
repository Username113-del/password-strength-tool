import argparse
import math
from zxcvbn import zxcvbn

# -------------------------------
# Password Analysis Functions
# -------------------------------
def analyze_password(password):
    result = zxcvbn(password)
    entropy = calculate_entropy(password)
    return {
        'score': result['score'],
        'entropy': entropy,
        'crack_times': result['crack_times_display'],
        'feedback': result['feedback']
    }

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password): charset += 32
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

# -------------------------------
# Wordlist Generator Functions
# -------------------------------
def leetspeak_variants(word):
    leet_map = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['$', '5']}
    variants = set([word])
    for i, c in enumerate(word):
        if c.lower() in leet_map:
            for replacement in leet_map[c.lower()]:
                new_word = word[:i] + replacement + word[i+1:]
                variants.add(new_word)
    return variants

def append_years(word, start=1990, end=2025):
    return [f"{word}{year}" for year in range(start, end+1)]

def generate_wordlist(inputs):
    base_words = set()
    for item in inputs:
        item = item.strip()
        base_words.add(item.lower())
        base_words.update(leetspeak_variants(item))
        base_words.update(append_years(item))
    return sorted(base_words)

def export_wordlist(wordlist, filename="wordlist.txt"):
    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

# -------------------------------
# CLI Interface
# -------------------------------
def main():
    parser = argparse.ArgumentParser(description="🔐 Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze")
    parser.add_argument("--inputs", nargs="+", help="Custom inputs (name, pet, etc.)")
    parser.add_argument("--output", default="wordlist.txt", help="Output wordlist file")
    args = parser.parse_args()

    if args.password:
        print("\n🔍 Analyzing Password...")
        result = analyze_password(args.password)
        print(f"Score: {result['score']} / 4")
        print(f"Entropy: {result['entropy']} bits")
        print("Crack Times:")
        for k, v in result['crack_times'].items():
            print(f"  {k}: {v}")
        print("Feedback:", result['feedback'])

    if args.inputs:
        print("\n🧠 Generating Wordlist...")
        wordlist = generate_wordlist(args.inputs)
        export_wordlist(wordlist, args.output)
        print(f"✅ Wordlist saved to {args.output} with {len(wordlist)} entries.")

if __name__ == "__main__":
    main()
