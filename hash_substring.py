def read_input():
    input_type = input().rstrip()
    if input_type == 'i':
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        filename = input().rstrip()
        with open(filename, 'f') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 101
    p_len, t_len = len(pattern), len(text)
    pattern_hash = sum(ord(pattern[i]) * pow(prime, i) for i in range(p_len))
    text_hash = sum(ord(text[i]) * pow(prime, i) for i in range(p_len))
    occurrences = []
    for i in range(t_len - p_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        if i < t_len - p_len:
            text_hash = (text_hash - ord(text[i])) / prime + ord(text[i+p_len]) * pow(prime, p_len-1)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
