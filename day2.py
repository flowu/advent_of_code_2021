def a(lines):
    x = sum([int(x[1]) for x in lines if x[0] == 'forward'])
    y = sum([-int(x[1]) if x[0] == 'up' else int(x[1]) if x[0] == 'down' else 0 for x in lines])
    return x*y

def b(lines):
    aim, x, y = 0, 0, 0
    for elem in lines:
        (dir, val) = (elem[0], int(elem[1]))
        if dir == 'down':
            aim += val
        elif dir == 'up':
            aim -= val
        else:
            x += val
            y += val*aim
    return x*y

def main():
    with open('C:/Users/Joel/Desktop/advent_of_code/input2.txt','r') as file:
        lines = [line.strip().split(' ') for line in file]
    
    print('a', a(lines))
    print('b', b(lines))

if  __name__ == '__main__':
  main()