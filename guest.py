import random

r = random.randint(1, 100)


while True:
	guest = input('請輸入您的數字： ')
	guest = int(guest)
	if guest == r:
		print('you are right!')
		break
	elif guest > r:
		print('your number bigger than the ans')
	elif guest < r:
		print('your number smaller than the ans')