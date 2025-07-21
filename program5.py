results = []
for num in range(1000, 1501):
    if num % 11 == 0 and num % 7 == 0:
        results.append(num)
print("Numbers divisible by 11 and multiple of 7 between 1000 and 1500:")
print(results)