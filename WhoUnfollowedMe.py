import tweepy
import os
import sys

CONSUMER_KEY  =  "???????"    
CONSUMER_SECRET =  "???????"       
ACCESS_KEY =  "???????"    
ACCESS_SECRET = "???????"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def CleanUp():
	old="CurrentFollowers.txt"
	os.remove(old)
	os.rename("Temp.txt","CurrentFollowers.txt")

def NewFollowersList():
	file = open("Temp.txt","w")
	for page in tweepy.Cursor(api.followers, screen_name="YourTwitterName").items():    
		  ids="@"+page.screen_name
		  file.write(ids+'\n')
	file.close()
	GetUnfollower()

def GetUnfollower():
	try:
		with open('CurrentFollowers.txt') as my_file:
			currfollwers = my_file.readlines()
		with open('Temp.txt') as my_file:
			newfollwers = my_file.readlines()
		currfollwers = map(str.strip, currfollwers)
		newfollwers = map(str.strip, newfollwers)
		unfollowed = list(set(currfollwers) - set(newfollwers))
	except FileNotFoundError:
			os.rename("Temp.txt","CurrentFollowers.txt")
			print("'CurrentFollowers.txt' does not exist")
			print("Don't worry, one was created.")
			print("It has all your current followers.")
			print("Run the program again when you've lost a follower to see who unfollowed you.")
			sys.exit()
	try:
		for n in range(len(unfollowed)):
			print(unfollowed[n]+' Unfollowed you. #TwitterBot #WhoUnfollowedMe')
		CleanUp()
	except:
		print("No one unfollowed you.")

def sendtweet():
	tweet=input("tweet: ")
	try:
		api.update_status (status=tweet)
	except:
		print("Sorry, Tweet Not Sent!")

if __name__ == '__main__':
	NewFollowersList()