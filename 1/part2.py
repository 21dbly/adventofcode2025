
def main():
    pos = 50
    count = 0

    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        # line = input()
        move = parse_line(line)
        prev_pos = pos
        if pos == 0 and move < 0: count -= 1
        pos += move
        # print("pos",pos)
        passes = pos // 100
        # print("passes",abs(passes))
        pos = pos % 100
        count += abs(passes)
        if move <= 0 and pos == 0 and prev_pos != 0: count += 1
        # print("count",count)
    print(count)
    # print(pos)

def parse_line(line):
    dir = line[0]
    dist = int(line[1:])
    if dir == "L": dist *= -1
    return dist

main()