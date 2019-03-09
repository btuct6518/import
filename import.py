import random
start = input('請決定開始決定值範圍:')
end = input('請決定開始決定值範圍:')
start = int(start)
end = int(end)
r = random.randint(start, end)
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