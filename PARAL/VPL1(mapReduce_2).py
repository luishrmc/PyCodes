from collections import Counter

def reduz(contagem_1, contagem_2):
    return Counter(contagem_1) + Counter(contagem_2)

def conta_um_arquivo(fpath):
    A = Counter()
    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                words = line.split()
                A += Counter(words)
        return A