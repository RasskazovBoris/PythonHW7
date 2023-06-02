sing = input("Песня Пуха: ").split()
result = []

for i in range(len(sing)):
    result.append(list(filter(lambda x: x in "уеыаоэяию", sing[i])))
result = list([len(i) for i in result])
acc = 0
for i in result:
    acc = acc + i
if acc/len(result) == result[0]:
    print("Парам пам-пам")
else:
    print("Пам парам")