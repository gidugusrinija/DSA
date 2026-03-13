l = [101, 5, 6, 8, 9, 14, 65, 91, 100]

max_num = 0

previous = 0

for i in l:
   if i > max_num:
      previous = max_num
      max_num = i
   elif max_num > i > previous:
      previous = i
print(previous)


