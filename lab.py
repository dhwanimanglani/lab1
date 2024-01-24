# function name: wins_rock_scissors_paper

def wins_rock_scissors_paper(player, opponent):
    player_choice = player.lower()
    opponent_choice = opponent.lower()

    if player_choice == opponent_choice:
        return False
    elif (player_choice == "rock" and opponent_choice == "scissors") or \
         (player_choice == "paper" and opponent_choice == "rock") or \
         (player_choice == "scissors" and opponent_choice == "paper"):
        return True
    else:
        return False
    
    # function name: factorial

    def factorial(int_n):
    if int_n == 0:
        return 1

    result = 1
    for i in range(1, int_n + 1):
        result *= i

    return result

# function name: fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev_digit, prev_prev_digit = 1, 0

    for _ in range(3, n + 1):
        result = prev_digit + prev_prev_digit
        prev_prev_digit, prev_digit = prev_digit, result

    return prev_digit

#function name: sum_to_goal
def sum_to_goal(number_list, goal_val):
    list_len = len(number_list)

    for i in range(list_len):
        for j in range(i + 1, list_len):
            if number_list[i] + number_list[j] == goal_val:
                return number_list[i] * number_list[j]

    return 0

# class : UpCounter
class UpCounter:
    def __init__(self, step_size=1):
        self.step_size = step_size
        self.counter = 0

    def count(self):
        return self.counter

    def update(self):
        """
        Update the counter by adding the step size.
        """
        self.counter += self.step_size


     # class : DownCounter
        class DownCounter(UpCounter):
    def update(self):
        """
        Update the counter by subtracting the step size.
        """
        self.counter -= self.step_size


