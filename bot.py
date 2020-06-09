import tweepy
from tweet_api import *
import random
from transfer_heading import *
from player_names import *
from team_name import *
import time


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def tweet_this_news(mes,teamName):
	teamName = teamName.replace(' ', '')
	tweet = "📰 {} \n#{}".format(mes,teamName)
	api.update_status(status=tweet)
	print('done')
	time.sleep(250)

def randomNumber(num):
	return random.randint(0,num)
def noSameRandomNumber(num,lastNum):
	rand = random.randint(0,num)
	if(lastNum == rand):
		return noSameRandomNumber(num, lastNum)
	else:
		return rand
def transferMoney():
	i = random.randint(0,3)
	if(i == 0):
		return random.randint(0,50)
	elif(i == 1):
		return random.randint(155, 1889)/100
	elif(i == 2):
		return random.randint(50,70)
	else:
		return random.randint(70,150)

last_number = 0
# Random heading
while True:
	try:		
		if(last_number == 0):
			heading_str = randomNumber(22)
		else:
			heading_str = noSameRandomNumber(22,last_number)

		footy_price = transferMoney()
		if(heading_str <= 2):
			val = len(player_name) - 1
			playerNum = randomNumber(val)
			teamVal = len(team_name)-1
			t1 = randomNumber(teamVal)
			t2 = noSameRandomNumber(teamVal,t1)
			mes = transfer_heading[heading_str].format(team_name[t1],team_name[t2],player_name[playerNum])
			tweet_this_news(mes,team_name[t1])

		elif(heading_str == 3):
			val = len(player_name) - 1
			playerNum = randomNumber(val)
			teamVal = len(team_name)-1
			t1 = randomNumber(teamVal)
			mes = transfer_heading[heading_str].format(player_name[playerNum],team_name[t1],footy_price)
			tweet_this_news(mes,team_name[t1])

		elif(heading_str <= 10):
			val = len(player_name) - 1
			playerNum = randomNumber(val)
			teamVal = len(team_name)-1
			t1 = randomNumber(teamVal)
			mes = transfer_heading[heading_str].format(player_name[playerNum],team_name[t1],footy_price)
			tweet_this_news(mes,team_name[t1])

		elif(heading_str <= 15):
			val = len(player_name) - 1
			playerNum = randomNumber(val)
			teamVal = len(team_name)-1
			t1 = randomNumber(teamVal)
			mes = transfer_heading[heading_str].format(team_name[t1],footy_price,player_name[playerNum])
			tweet_this_news(mes,team_name[t1])

		elif(heading_str == 16):
			val = len(player_name) - 1
			playerNum = randomNumber(val)
			teamVal = len(team_name)-1
			t1 = randomNumber(teamVal)
			mes = transfer_heading[heading_str].format(team_name[t1],player_name[playerNum],footy_price)
			tweet_this_news(mes,team_name[t1])

		elif(heading_str <= 21):
			teamVal = len(team_name)-1
			t1 = randomNumber(teamVal)
			t2 = noSameRandomNumber(teamVal,t1)
			mes = transfer_heading[heading_str].format(team_name[t1],footy_price,team_name[t2])
			tweet_this_news(mes,team_name[t1])

		else:
			teamVal = len(team_name)-1
			t1 = randomNumber(teamVal)
			mes = transfer_heading[heading_str].format(team_name[t1],random.randint(17,40))
			tweet_this_news(mes,team_name[t1])

		last_number = heading_str

	except:
		print("Error")