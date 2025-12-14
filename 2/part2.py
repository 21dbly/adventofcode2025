
def main():
    total = 0

    with open("input.txt") as file:
        txt = file.read()

    for r in txt.split(','):
        r_split = r.split('-')
        start = int(r_split[0])
        end = int(r_split[1])
        for n in range(start, end+1):
            if has_pattern(n):
                total += n

    print(total)

def has_pattern(n):
    str_n = str(n)
    l = len(str_n)
    for d in range(1, l//2 + 1):
        if l % d != 0: continue
        rep = l // d
        if str_n[:d]*rep == str_n:
            return True
    return False

main()
# while True:
#     print(has_pattern(int(input())))