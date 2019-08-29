import re

# 'find the month and date'
# regex=r"[a-zA-Z]+ \d+"
#
#
# match=re.findall(regex,"june 32,JUNE 42,march 43")
# print(match)
# for m in match:
#     print(m)

'''Find the file extensions like txt'''

# regex=r"[a-zA-Z]+\.[txt]+"
#
# match=re.findall(regex,"sudheer.txt,mahesh.txt,sekhar.txt,murali.txt,mouni.txt,sudheer")
# print(match)
# for m in match:
#     print(m)


'''Find the gmails in the string'''
#
# regex=r"[a-zA-z0-9.+-]+[a-zA-Z0-9-]+@[a-zA-z]+\.com"
# match=re.findall(regex,"sudheer.m@gmail.com,sudheer+m@gmail.com,sudheer_m@gmail.com,sudheer-m@gmail.com")
# print(match)


'''Replace string using re.sub'''

# regex=r"\W"
# match=re.subn(regex,"$","sudheer@@@@dgjdg#n,mnvn%n,mnvnd&")
# print(match)

'''validate mobile numbers'''

# regex=r"[6789][0-9]{9}"
#
# s=re.match(regex,"9177935906")
# print(s.group())


'''read mobile numbers from file and write all mobile number into another file'''

# regex=r"[6-9]\d{9}"
#
# with open('sudheer.txt') as mobile:
#     match=re.findall(regex,mobile.read())
#
#     with open('mobile.txt','w') as b:
#         for i in match:
#             b.write(i+"\n")
#     print("Sucessfull")


