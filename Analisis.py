import string
import operator

cipher = 'pjej xj wq dpjjafbu'
class Attack:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.freq = {}
        self.freq_eng = {'a': 0.0812, 'b': 0.0150, 'c': 0.0271, 'd': 0.0432, 'e': 0.1202, 'f': 0.0230,
        'g': 0.0203, 'h': 0.0592, 'i': 0.0731,
        'j': 0.0010, 'k': 0.0069, 'l': 0.0398,
        'm': 0.0261, 'n': 0.0675, 'o': 0.0751,
        'p': 0.0182, 'q': 0.0011, 'r': 0.0602,
        's': 0.0628, 't': 0.0910, 'u': 0.0288,
        'v': 0.0111, 'w': 0.0209, 'x': 0.0017,
        'y': 0.0211, 'z': 0.0007}
        self.mappings = {}

    def calculate_freq(self, cipher):
        for c in self.alphabet:
            self.freq[c] = 0
        letter_count = 0

        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                letter_count += 1

        for c in self.freq:
            self.freq[c] = round(self.freq[c] / letter_count, 4)
    def print_freq(self):
        new_line_count = 0
        for c in self.freq:
            print(c, ':', self.freq[c], " ", end='')
            if new_line_count % 3 == 2:
                print()
            new_line_count += 1
    def calculate_matches(self):
        for cipher_char in self.alphabet:
            map = {}
            for plain_char in self.alphabet:
                map[plain_char] = round(abs(self.freq[cipher_char] - self.freq_eng[plain_char]), 4)
            self.mappings[cipher_char] = sorted(map.items(), key=operator.itemgetter(1))

attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()
print("\n")
attack.calculate_matches()

for c in attack.mappings:
    print(c, attack.mappings[c])
    print("\n")

