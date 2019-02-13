#2. Закодируйте любую строку из трех слов по алгоритму Хаффмана

from collections import Counter, namedtuple

Char = namedtuple('Char', 'freq text')
Tree = namedtuple('Tree', 'value left right')

def is_leaf(tree):
    return tree.left is None and tree.right is None

def print_tree(t, level=0):
    if t is None:
        pass
    else:
        print((" " * level), t.value)
        print_tree(t.left, level + 2)
        print_tree(t.right, level + 2)


def make_table(t, code="", result={}):
    if is_leaf(t):
        result[t.value.text] = code
    else:
        make_table(t.left, code + "0")
        make_table(t.right, code + "1")
    return result

def combine(m1, m2):
    nf = m1.value.freq + m2.value.freq
    nt = m1.value.text + m2.value.text
    nC = Char(nf, nt)
    nTr = Tree(nC, m1, m2)
    return nTr

def pop_min(a):
    min_el = min(a)
    a.remove(min_el)
    return min_el

def encode(str):
    encoded = ""
    for letter in str:
        encoded += result[letter]
    return encoded

str = "hop hei lalaleihhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
print(f"Строка: {str}")
letter_freqs = Counter(str)
print("Считаем частоту символов в строке: {letter_freqs}")

a = [Tree(Char(freq, text), None, None) for text, freq in letter_freqs.items()]

while len(a) > 1:
    m1 = pop_min(a)
    m2 = pop_min(a)
    a.append(combine(m1, m2))

print("Рисуем дерево:")
print_tree(a[0])
result = make_table(a[0])
print(f"Таблица: {result}")
print(f"Результат кодирования {encode(str)}")
