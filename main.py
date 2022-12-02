def get_elf_to_calories(input_calories):
    """
    
    :param list input_calories : List of all calories in file separated by line
    :returns: elf_to_calories - dictionary mapping each elf to calories with them
    """

    # calorie_to_elf = {}
    elf_to_calories = {}

    curr_calories = 0
    curr_elf = 0
    
    for calorie in input_calories: 
        if calorie == "\n":
            # calorie_to_elf[curr_calories] = curr_elf
            elf_to_calories[curr_elf] = curr_calories
            curr_elf += 1
            curr_calories = 0
        else:
            curr_calories += int(calorie)

    return elf_to_calories

def get_n_max_calories(input_calories, n):
    """
    :param list input_calories : List of all calories in file separated by line
    :param int n : no of elves with highest calories
    :returns: sum_of_n_max - sum of the top n calories
    """

    elf_to_calories = get_elf_to_calories(input_calories)

    sum_of_n_max = 0
    sorted_calories = sorted(elf_to_calories.values())

    while n > 0: 
        sum_of_n_max += sorted_calories[-1]
        sorted_calories.pop()
        n -= 1

    return sum_of_n_max

def get_score_literal_moves(strategy):
    def result_of_two_moves(left, right):
        if left == "A" and right == "Y": 
            return "win"
        if left == "A" and right == "Z": 
            return "loss"
        if left == "A" and right == "X": 
            return "draw"

        if left == "B" and right == "Z": 
            return "win"
        if left == "B" and right == "X": 
            return "loss"
        if left == "B" and right == "Y": 
            return "draw"

        if left == "C" and right == "X": 
            return "win"
        if left == "C" and right == "Y": 
            return "loss"
        if left == "C" and right == "Z": 
            return "draw"

    X, Y, Z = 1, 2, 3 # rock, paper, scissors
    loss, draw, win = 0, 3, 6 

    convert = {"X" : X, "Y" : Y, "Z" : Z}
    total_score = 0

    for round in strategy:
        moves = round.split(" ")
        left = moves[0]
        right = moves[1].strip()

        if result_of_two_moves(left, right) == "win":
            total_score += convert[right] + win
        if result_of_two_moves(left, right) == "loss":
            total_score += convert[right] + loss
        if result_of_two_moves(left, right) == "draw":
            total_score += convert[right] + draw
    return total_score

def get_score_strategy_moves(strategy):
    def response_move(left, right):
        if left == "A" and right == "Y": 
            return "A"
        if left == "A" and right == "Z": 
            return "B"
        if left == "A" and right == "X": 
            return "C"

        if left == "B" and right == "Z": 
            return "C"
        if left == "B" and right == "X": 
            return "A"
        if left == "B" and right == "Y": 
            return "B"

        if left == "C" and right == "X": 
            return "B"
        if left == "C" and right == "Y": 
            return "C"
        if left == "C" and right == "Z": 
            return "A"

    A, B, C = 1, 2, 3 # rock, paper, scissors
    X, Y, Z = 0, 3, 6 # loss, draw, win

    convert = {"A" : A, "B" : B, "C" : C, "X": X, "Y": Y, "Z":Z}
    total_score = 0

    for round in strategy:
        moves = round.split(" ")
        left = moves[0]
        right = moves[1].strip()
        
        my_move = response_move(left, right)

        if my_move == "A":
            total_score += convert[right] + A
        if my_move == "B":
            total_score += convert[right] + B
        if my_move == "C":
            total_score += convert[right] + C

    return total_score

def main():
    # Day 1
    input_calories = open('calories.txt','r').readlines()

    # Task 1
    print(f"elf with most calories: {get_n_max_calories(input_calories, 1)}")

    # Task 2
    print(f"top 3 elves with most calories: {get_n_max_calories(input_calories, 3)}")


    # Day 2
    strategy = open('strategies.txt','r').readlines()

    # Task 3
    print(f"total score after all rounds: {get_score_literal_moves(strategy)}")

    # Task 4
    print(f"total score after playing moves according to strategy: {get_score_strategy_moves(strategy)}")

    
# Main function calling
if __name__ == "__main__":
    main()
