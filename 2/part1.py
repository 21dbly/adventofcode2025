
def main():
    total = 0

    with open("input.txt") as file:
        txt = file.read()

    for r in txt.split(','):
        r_split = r.split('-')
        start = int(r_split[0])
        end = int(r_split[1])
        for n in range(start, end+1):
            n_str = str(n)
            if len(n_str) % 2 == 1: continue
            if n_str[:len(n_str)//2] == n_str[len(n_str)//2:]:
                total += n

    print(total)


main()