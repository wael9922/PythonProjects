""" Automates creating personalized letters by filling a template with names from a list using Python. """

with open(r'D:\Mail Merge Project Start\Input\Letters\starting_letter.txt','r') as f:
	letter = f.read() # read the mail template
	# print(letter)
with open(r"D:\Mail Merge Project Start\Input\Names\invited_names.txt",'r') as f:
	invite_list = f.readlines()

invite_list = [name.strip() for name in invite_list] # clean up the names
# print(invite_list)
for name in invite_list:
	with open(rf"E:\ReadyToSend\{name}.txt","w") as f:
		invite = letter.replace("[name]",name) # uses the mail template add receiver name
		f.write(invite) # write a mail for each name in separate text file


"""
		Letter Template used
		Dear [name],
		
		You are invited to my birthday this Saturday.
		
		Hope you can make it!
		
		Angela
"""
