def a(lines):
    return len([x for i,x in enumerate(lines[1:]) if x > lines[i]])

def b(lines):
    return len([x for x in range(3,len(lines)+1) if sum(lines[x-2:x+1]) > sum(lines[x-3:x])])

def main():
    with open('C:/Users/Joel/Desktop/advent_of_code/input1.txt','r') as file:
        lines = [int(line) for line in file]
    
    print('a', a(lines))
    print('b', b(lines))

if  __name__ == '__main__':
  main()