marks = [73, 35, 56, 78, 99, 88, 62, 56, 67, 96]
print("a)", 70 in marks)
print("b)", marks[4])
print("c)", marks[-2:])
print("d)", marks[:3])
print("e)", marks[2:5])
print("f)", sum(marks))
print("g)", max(marks))
print("h)", 100 in marks)
print("i)", any(m < 40 for m in marks))
marks[7] = 64
print("j)", marks)
print("k)", len(marks))
marks.append(78)
marks.append(34)
print("l)", marks)
marks.extend([45, 78, 67])
print("m)", marks)
print("n)", sorted(marks))
marks = [m for m in marks if m >= 50]
print("o)", marks)
def find_min_and_index(lst):
    min_val = min(lst)
    index = lst.index(min_val)
    return min_val, index

min_value, min_index = find_min_and_index(marks)
print("p) Min value:", min_value, "at index", min_index)
squares = [x**2 for x in range(1, 21)]
print("q)", squares)
words = ["banana", "umbrella", "jungle", "puzzle"]
word_lengths = [len(word) for word in words]
print("r)", word_lengths)