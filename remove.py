import time
print("Welcome to the TestWiki:Inactivity Script")
print("This script may only be used by consuls")
print("Please ensure notifications were sent > 7 days ago and the users are still inacitve")
time.sleep(2)
print("https://publictestwiki.com/wiki/Special:ApiSandbox#action=userrights&format=json&user=&add=&remove=bot%7Csysop%7Cbureaucrat%7Cconsul%7Ctestgroup%7Cautopatrolled%7Cconfirmed%7Crollbacker%7Cinterface-admin%7Cflow-bot%7Ccheckuser%7Cinterwiki-admin%7Coversight%7Csteward&reason=per%20%5B%5BTestWiki%3AInactivity%7CInactivity%20report%5D%5D&token=")
time.sleep(2)
userremoving = input("What is your username?")
#Add Template:Inactivty when params fixed
time.sleep(2)
