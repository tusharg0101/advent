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

def get_priority_sum_compartments(rucksack):
    result = 0

    for i in rucksack:
        i = i.strip()
        length = len(i)
        first_compartment = set(i[: length//2 ]) 
        second_compartment = set(i[length//2 : ])
        misplaced_item = first_compartment.intersection(second_compartment).pop()
        if misplaced_item.islower():
            result += ord(misplaced_item) - 96
        elif misplaced_item.isupper(): 
            result += ord(misplaced_item) - 38

    return result

def get_priority_sum_badges(rucksack):
    result = 0

    for i in range(0, len(rucksack), 3):
        first_elf = set(rucksack[i].strip())
        second_elf = set(rucksack[i + 1].strip())
        third_elf = set(rucksack[i + 2].strip())

        badge = first_elf.intersection(second_elf)
        badge = badge.intersection(third_elf).pop()
        if badge.islower():
            result += ord(badge) - 96
        elif badge.isupper(): 
            result += ord(badge) - 38
    return result

def get_fully_contain(clean_up):
    result = 0
    for i in clean_up: 
        line = i.split(",")
        first = line[0].split("-")
        second = line[1].split("-")
        start1 = int(first[0])
        end1 = int(first[1])
        start2 = int(second[0])
        end2 =  int(second[1])
        
        if start1 <= start2 and end1 >= end2:
            result += 1
        
        elif start1 >= start2 and end1 <= end2:
            result += 1
    return result

def get_overlaps(clean_up):
    def check_overlap(regions):
        result = 0
        start1, end1, start2, end2 = regions[0][0], regions[0][1], regions[1][0], regions[1][1]

        if start1 <= start2 and end1 >= end2:
                result += 1
            
        elif start1 >= start2 and end1 <= end2:
            result += 1
        
        elif end1 >= start2 and end1 <= end2: 
            result += 1
        
        elif end2 >= start1 and end2 <= end1: 
            result += 1

        return result

    result = 0
    for i in clean_up: 
        line = i.split(",")
        first = line[0].split("-")
        second = line[1].split("-")
        regions = [[int(first[0]), int(first[1])], [int(second[0]), int(second[1])]]
        result += check_overlap(regions)
    return result

def get_top_crates(crates, same_order):
    def process_crates_data(crates):

        moves_start = 0
        for i in range(len(crates)): 
            if crates[i][1] == "1": 
                moves_start = i + 2
                break

        num_stacks = len(crates[i])//4
        result = {i:[] for i in range(1, num_stacks + 1)}

        for line in crates:
            line = line.replace("\n", "")
            if line[1] == "1":
                break
            
            for char in range(0, len(line), 4): 
                crate_name = line[char + 1]
                if crate_name != " ":
                    result[char//4 + 1] += [crate_name]
                    
        for lis in result: 
            result[lis] = [result[lis][i] for i in range((len(result[lis]) - 1), -1, -1)]

        return result, moves_start
    
    result = ""
    processed_crates, moves_start = process_crates_data(crates)
    
    for line in crates[moves_start: ]:
        data = line.split()
        move_num_crates = int(data[1])
        from_stack_num = int(data[3])
        to_stack_num = int(data[5])

        to_move = processed_crates[from_stack_num][-move_num_crates:]
        if not same_order: 
            to_move.reverse()
        processed_crates[to_stack_num] += to_move
        processed_crates[from_stack_num] = processed_crates[from_stack_num][:-move_num_crates]
    
    for stack in processed_crates:
        result += processed_crates[stack][-1]
    return result

def get_char_processed(signal, msg_or_pkt):
    start = 0
    end = 0
    proc = []
    signal = signal[0]
    distincts = 0

    if msg_or_pkt == 1:
        distincts = 4
    elif msg_or_pkt == 0:
        distincts = 14
    else: 
        return -1

    while start <= end and end < len(signal):
        curr = signal[end]
        if len(proc) == distincts:
            return end
        if curr not in proc:
            proc.append(curr)
            end += 1
        else: 
            id = proc.index(curr)
            proc = proc[(id + 1):]
            proc.append(curr)
            start = end - id + 1
            end += 1
    return -1

def main():
    print("\nDay1")
    # Day 1
    calories_data = open('calories.txt','r')
    input_calories = calories_data.readlines()

    # Task 1
    print(f"elf with most calories: {get_n_max_calories(input_calories, 1)}")

    # Task 2
    print(f"top 3 elves with most calories: {get_n_max_calories(input_calories, 3)}")

    calories_data.close()

    print("\nDay2")
    # Day 2
    strategy_data = open('strategies.txt','r')
    strategy = strategy_data.readlines()

    # Task 3
    print(f"total score after all rounds: {get_score_literal_moves(strategy)}")

    # Task 4
    print(f"total score after playing moves according to strategy: {get_score_strategy_moves(strategy)}")

    strategy_data.close()
    
    print("\nDay3")
    # Day 3
    rucksack_data = open('rucksack.txt','r')
    rucksack = rucksack_data.readlines()

    # Task 5
    print(f"sum of priorities of item types in both comparments: {get_priority_sum_compartments(rucksack)}")

    # Task 6
    print(f"sum of priorities of badges of 3-elf groups: {get_priority_sum_badges(rucksack)}")

    rucksack_data.close()

    print("\nDay4")
    # Day 4
    clean_up_data = open('clean_up.txt','r')
    clean_up = clean_up_data.readlines()

    # Task 7
    print(f"total number of assignments that full contain the other: {get_fully_contain(clean_up)}")

    # Task 8
    print(f"total number of assignments that have overlap: {get_overlaps(clean_up)}")

    clean_up_data.close()

    print("\nDay5")
    # Day 5
    crates_data = open('crates.txt','r')
    crates = crates_data.readlines()

    # Task 9
    print(f"top crates after all procedures : {get_top_crates(crates, False)}")

    # Task 10
    print(f"top crates after all procedures with same_order movements : {get_top_crates(crates, True)}")

    crates_data.close()

    print("\nDay6")
    # Day 6
    signal_data = open('signal.txt','r')
    signal = signal_data.readlines()

    # Task 11
    print(f"characters processed before first start-of-packet marker : {get_char_processed(signal, 1)}")

    # Task 12
    print(f"characters processed before first start-of-message marker : {get_char_processed(signal, 0)}")

    signal_data.close()


# Main function calling
if __name__ == "__main__":
    main()
