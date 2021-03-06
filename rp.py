"""
==========================
Rock, Paper, Scissors Game
==========================
Python 3.5.2

Author : JKY

Version : 1.0



-----------------------
Manual
-----------------------


this is rock,scissors,paper game made by Python3

please enter input '1 = scissors' or '2 = rock' or '3 = paper'

so, after 10 turns, result is printed

"""
import random

def play():
	com = [1,2,3]
	choi = ["가위","바위","보"]
	
	print("-------------------")
	print("가위바위보를 시작합니다.")
	print("-------------------")

	result = [0,0,0]
	count = 10
	
	while count > 0:
		print("가위(1) 바위(2) 보(3) 를 선택해 주세요.")
		player = input()

		while not (player.isdigit()) or int(player)>3 or int(player)==0:
			print("부적절한 숫자 혹은 문자 입니다.")
			print("가위(1) 바위(2) 보(3) 를 선택해 주세요.")
			player = input()
		
		player = int(player)
		c = random.choice(com)
		
		if (player==1 and c == 1) or (player==2 and c == 2) or (player==3 and c == 3):
			print("당신과 컴퓨터는 서로 ",choi[player-1], "를 내서 비겼습니다.")
			result[1] += 1
		
		elif (player==2 and c==1) or (player==1 and c==3) or (player==3 and c==2):
			if player==1:
				print("당신은 ",choi[player-1],"을 냈고 컴퓨터는 ",choi[2],"를 내서 당신은 이겼습니다.")
			else:
				print("당신은 ",choi[player-1],"을 냈고 컴퓨터는 ",choi[player-2],"를 내서 당신은 이겼습니다.")
			result[0] += 1
			
		else:
			if player==3:
				print("당신은 ",choi[player-1],"을 냈고 컴퓨터는 ",choi[0],"를 내서 당신은 겼습니다.")
			else:
				print("당신은 ",choi[player-1],"을 냈고 컴퓨터는 ",choi[player],"를 내서 당신은 겼습니다.")
			result[2] += 1

		count -= 1
		print("-------------------------------------------------------------------")
		print()

	print("당신의 결과 입니다")
	print("승  무  패")
	print(result[0]," ",result[1]," ",result[2])

while True:
	print("플레이를 시작합니다.")
	play()
	q = input("가위바위보롤 또 하시길 원하세요? (1: yes ,2:no)")
	while not q.isdigit() or int(q)==0 or int(q)>2:
		print("적절한 입력이 아닙니다.")
		q = input("가위바위보롤 또 하시길 원하세요? (1: yes ,2:no)")
	if int(q)==2:
		break;
print("종료되었습니다")
