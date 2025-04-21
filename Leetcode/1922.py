import math


def countGoodNumbers(n):
    switch = True
    output = 1

    for _ in range(n):
        if switch:
            output *= 5
            switch = False
        else:
            output *= 4
            switch = True
    return output


def main():
    print(countGoodNumbers(3))


if __name__ == "__main__":
    main()
