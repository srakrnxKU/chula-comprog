# palindrome.py

txt = input().split() #อีเกรดเดอร์ควาย
l = len(txt)-1
status = "Y"
for i in range(0,int(l/2)):
    if txt[i] != txt[l-i]:
        status = "N"
        break
print(status)