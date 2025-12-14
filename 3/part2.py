def main():
    total = 0

    with open("input.txt") as file:
        lines = file.readlines()

    for bank in lines:
        bank = bank.strip()
        bats_str = ""
        prev_ind = -1
        for bat_num in range(12):
            cut_off = len(bank) - 11 + bat_num
            bat_ind = prev_ind+1 + max_index(bank[prev_ind+1:cut_off])
            bats_str += bank[bat_ind]
            prev_ind = bat_ind
        # print(bats_str)
        total += int(bats_str)
        
    print(total)

def max_index(lst):
    return max(range(len(lst)), key=lambda i: lst[i])

main()