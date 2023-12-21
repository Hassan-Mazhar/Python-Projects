email=input("Enter your Email: ")#g@g.in(minimun six characters)
if len(email)>=6:
	if email[0].isalpha():
		if("@"in email) and (email.count("@")==1):
		   if (email[-4]==".") ^ (email[-3]=="."):
			for i in email:
				if i==i.isspace():
					k=1
				elif i.isalpha():
					if i==i.upper():
						j=1
				elif i.isdigit():
					continue
				elif i=="_" or i=="." or i=="@"
					continue
				else:
					d=1
			if k==1 or j==1 or d==1:
				print("Wrong Email 5")
			else
				print("right Wmail")
		   else:
			print("wrong Email 4")

		else:
			print("wrong Email 3")
	      else:
			print('wrong Email 2')
else:
	print("wrong Email 1")
