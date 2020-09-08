import random
options = ['Stone', 'Paper', 'Scissors', 'Lizard', 'Spock']
rounds = int(input('Enter number of rounds:'))
user_points = 0
computer_points = 0
for i in range(rounds):
    user = input('Enter your choice(from Stone,Paper,Lizard,Scissor,Spock):')
    computer = random.choice(options)
    print(computer)
    if computer == 'Stone' and user == 'Paper':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Stone' and user == 'Spock':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Paper' and user == 'Scissor':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Paper' and user == 'Lizard':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Scissors' and user == 'Stone':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Scissors' and user == 'Spock':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Lizard' and user == 'Rock':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Lizard' and user == 'Scissors':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Spock' and user == 'Lizard':
        print('User wins')
        user_points = user_points + 1
    elif computer == 'Spock' and user == 'Lizard':
        print('User wins')
        user_points = user_points + 1
    elif computer == user:
        print("It's a Tie")
    else:
        print('Computer wins')
        computer_points = computer_points + 1
print(f'User points = {user_points}')
print(f'Computer points = {computer_points}')
if user_points > computer_points:
    print('User is the winner')
elif user_points < computer_points:
    print('Computer is the winner')
else:
    print("It's a Tie")
