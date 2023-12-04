Task 1
def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins."
    elif (player2 == 'rock' and player1 == 'scissors') or (player2 == 'scissors' and player1 == 'paper') or (player2 == 'paper' and player1 == 'rock'):
        return "Player 2 wins."
    else:
        return "This input is not valid for our game!"

# Get input from users
player1_choice = input("Player 1? ").lower()
player2_choice = input("Player 2? ").lower()

# Check for valid inputs and determine the winner
if player1_choice in ['rock', 'paper', 'scissors'] and player2_choice in ['rock', 'paper', 'scissors']:
    result = determine_winner(player1_choice, player2_choice)
    print(result)
else:
    print("This input is not valid for our game!")

Task 2
 for i in range(1, 8):
    print('*' * i)

for i in range(6, 0, -1):
    print('*' * i)

Task 3
Step 1:
a = [2, 2, 3, 1, 1, 1, 1, 3, 2, 2, 6, 5, 4, 7, 8, 31]
b = [2, 7, 4, 6, 7, 4, 2, 31, 2, 5, 11, 1, 2, 1, 3, 1, 7, 9, 5]

common_elements = list(set(a) & set(b))
print(common_elements)

Step 2 (One-liner):
a = [2, 2, 3, 1, 1, 1, 1, 3, 2, 2, 6, 5, 4, 7, 8, 31]
b = [2, 7, 4, 6, 7, 4, 2, 31, 2, 5, 11, 1, 2, 1, 3, 1, 7, 9, 5]

common_elements = list(set(a) & set(b))
print(common_elements)

Task 4
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get input from the user
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")

Task 5
my_list = [2, 5, 4, 4, 6, 7, 5, 6, 9, 22, 23, 44, 32]
new_list = [x for x in my_list if x % 2 != 0]
print(new_list)
