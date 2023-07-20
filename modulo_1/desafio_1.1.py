T = input("Digite seu tweet: ")
contador = 0

for letra in T:
    contador += 1

if contador <= 140:
    print("TWEET")
else:
    print("MUTE")
