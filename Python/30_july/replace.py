#WAP to replace all vowels with their index positions in a given string.
'''
string = input('enter string: ')

for ip in range(len(string)):
    if string[ip] in 'aeiouAEIOU':
        string = string.replace(string[ip],str(ip))

print(string)'''


s = input('Enter String: ')
new = ''

for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
        new+=str(ip)
    else:
        new+=s[ip]

print(new)