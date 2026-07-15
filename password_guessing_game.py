import random

easy_words=['apple','train','tiger','money','india']
medium_words=['python','bottel','monkey','plannet','laptop']
hards_words=['elephant','diamond','umbrella','computer','mountain']

print('welcome to the pasword guessing game')
print('choose the difficulty level: easy,medium,hard')

level=input('enter difficylty:').lower()
if level=='easy':
    secret=random.choice(easy_words)
elif level=='medium':
    secret=random.choice(medium_words)
elif level=='hard':
    secret=random.choice(hards_words)
else:
    print('invalid choice. defaulting to easy level')
    secret = random.choice(easy_words)
attempts=0
print('\nguess the secret password')

while True:
    guess=input('enter your guess:').lower()
    attempts += 1

    if guess ==secret:
        print(f'congratulation ! you gussed it in {attempts} attempts')
        break
    hint=''
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint += guess[i]
        else:
            hint += '__'
    print('hint:',hint)
print('game over')
        
