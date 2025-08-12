import itertools
import random

def generate_password(length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]};:\'",<.>/?'
    return ''.join(random.choice(chars) for _ in range(length))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    unique_words = set(words)
    return {
        'word_count': word_count,
        'char_count': char_count,
        'unique_words': unique_words
    }

def main():
    password_length = 12
    password = generate_password(password_length)
    print(f"Generated password: {password}")

    prime_limit = 20
    primes = find_primes(prime_limit)
    print(f"Prime numbers up to {prime_limit}: {primes}")

    fib_length = 10
    fibonacci_sequence = fibonacci(fib_length)
    print(f"Fibonacci sequence of length {fib_length}: {fibonacci_sequence}")

    sample_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. 
    Sed venenatis tellus quis urna volutpat, in ultricies lorem pretium. 
    Vestibulum sit amet odio et libero suscipit blandit eu at nisi. 
    """
    analysis = analyze_text(sample_text)
    print(f"Text analysis:")
    print(f" - Word count: {analysis['word_count']}")
    print(f" - Character count: {analysis['char_count']}")
    print(f" - Unique words: {analysis['unique_words']}")

if __name__ == "__main__":
    main()
