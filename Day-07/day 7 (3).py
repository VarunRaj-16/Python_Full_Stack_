# COMPLETE STRING METHODS DEMONSTRATION
print("=" * 60)
print("1. BASIC STRING OPERATIONS")
print("=" * 60)

# Defining different types of strings
greeting = 'Hello'                          # Single-quoted string
planet = "World"                            # Double-quoted string
multiline = '''This is a
multi-line string.'''                       # Multi-line string using triple quotes

print(greeting)
print(planet)
print(multiline)

# Concatenation → Joining two or more strings using +
full_greeting = greeting + " " + planet
print("Concatenation:", full_greeting)

# Repetition → Repeating a string multiple times using *
repeated = "Python! " * 3
print("Repetition:", repeated)

# Indexing → Accessing individual characters using positive/negative index
language = "Python"
print("First character:", language[0])      # Index 0 → first character
print("Last character:", language[-1])      # Index -1 → last character

# Slicing → Extracting a portion (substring) of the string
print("Slicing [0:3]:", language[0:3])      # From index 0 to 2
print("Slicing [:4]:", language[:4])        # From start to index 3
print("Slicing [2:]:", language[2:])        # From index 2 to end

# Membership → Checking if a substring exists inside the string
print("'Pyt' in language:", 'Pyt' in language)
print("'Java' not in language:", 'Java' not in language)
print("\n" + "=" * 60)
print("2. BUILT-IN STRING FUNCTIONS")
print("=" * 60)
sample_text = "Hello World"
