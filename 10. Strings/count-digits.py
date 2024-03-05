a = "Pytho1n is A GreAT LangAUGE"
cnt = 0
for char in a:
    asc_num = ord(char)
    if "0" <= char <= "9":
        cnt += 1
print(cnt)
