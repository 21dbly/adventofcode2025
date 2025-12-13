
def main():
    pos = 50
    count = 0

    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        move = parse_line(line)
        pos = (pos + move)%100
        if pos == 0: count += 1
    print(count)

def parse_line(line):
    dir = line[0]
    dist = int(line[1:])
    if dir == "L": dist *= -1
    return dist

main()