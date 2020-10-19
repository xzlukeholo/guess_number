import random

print('歡迎來到~終極密碼~請先決定最大的數字與最小的數字')
min_number = input('請輸入最「小」值:')
max_number = input('請輸入最「大」值:')
min_number = int(min_number)
max_number = int(max_number)
game_round = 0
answer = random.randint(min_number, max_number)

while True:
	num = input('請猜數字:')
	num = int(num)
	game_round = game_round + 1
	if num == answer:
		if game_round == 1:
			print('才第一局就猜中O口O!?太厲害惹!恭喜猜中喵!')
			break
		elif game_round == 2:
			print('(~￣▽￣)~太厲害惹!第二局就猜中!恭喜猜中喵!')
			break
		elif game_round > 15:
			print('恭喜猜中!獲勝!')
			print('可是第', game_round, '次才猜到〳 ° ▾ ° 〵，太弱囉喵~')
			break
		else:
			print('恭喜猜中!獲勝!')
			break
	else:
		print('可惜沒猜對喔~嘿嘿owo~')
		if num > answer:
			print('妳猜的數字，比答案大喔')
		elif num < answer:
			print('妳猜的數字，比答案小喔')
		print('現在是猜第', game_round, '次喔喵~')