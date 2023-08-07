import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

strs = input().strip()


def main():

    ioi = "IOI" + "OI" * (n-1)
    lens = len(ioi)
    count = 0
    for i in range(m):
        if strs[i:i+lens] == ioi:
            count += 1
    print(count)
    return


main()
