import random
r = random.randint(1, 100)
print(r)
count = 0
while True:
	count = count + 1
	num = input('請輸入數字:')
	num = int(num)
	if num == r:
		print('終於猜對了!!')
		break
	elif num <= r:
		print('比答案小喔!')
	elif num >= r:
		print('比答案大喔!')
	print('這是你猜的第', count, '次')