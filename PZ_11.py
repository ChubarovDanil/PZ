import random


def generate_sequence(length=10):
    return [random.randint(-100, 100) for _ in range(length)]


def write_to_file(filename, sequence):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, sequence)))


def read_from_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return list(map(int, data.split()))


seq1 = generate_sequence()
seq2 = generate_sequence()
write_to_file('file1.txt', seq1)
write_to_file('file2.txt', seq2)


nums1 = read_from_file('file1.txt')
nums2 = read_from_file('file2.txt')


common_elements = len(set(nums1) & set(nums2))
even_in_file1 = len([x for x in nums1 if x % 2 == 0])
odd_in_file2 = len([x for x in nums2 if x % 2 != 0])


result_content = f"""Элементы первого и второго файлов:
{', '.join(map(str, nums1))}
{', '.join(map(str, nums2))}
Количество элементов первого и второго файлов:
{len(nums1)}, {len(nums2)}
Количество элементов, общих для двух файлов:
{common_elements}
Количество четных элементов первого файла:
{even_in_file1}
Количество нечетных элементов второго файла:
{odd_in_file2}"""


with open('result.txt', 'w') as f:
    f.write(result_content)

print("Файлы успешно созданы и обработаны.")