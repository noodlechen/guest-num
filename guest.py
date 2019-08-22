bottom = input('請輸入數字下限： ')
bottom = int(bottom)
top = input('請輸入數字上限： ')
top = int(top)

import random
r = random.randint(bottom, top)

count = 0

while True:
	count += 1
	guest = input('請輸入您的數字： ')
	guest = int(guest)
	if guest == r:
		print('you are right!')
		print('這是你猜的', count, '次')
		break
	elif guest > r:
		print('your number bigger than the ans')
	elif guest < r:
		print('your number smaller than the ans')
	print('這是你猜的', count, '次')