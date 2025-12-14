def main():
    total = 0

    with open("input.txt") as file:
        lines = file.readlines()

    for bank in lines:
        bank = bank.strip()
        ind = max_index(bank[:-1])
        str_val = bank[ind] + max(bank[ind+1:])
        # print(str_val)
        total += int(str_val)
        
    print(total)

def max_index(lst):
    return max(range(len(lst)), key=lambda i: lst[i])

main()