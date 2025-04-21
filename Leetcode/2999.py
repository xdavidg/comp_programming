def numberOfPowerfulInt(start, finish, limit, s):

    # Checking base case if s is greater than finish, obviously can't make any powerful numbers
    s_int = int(s)
    if finish < s_int:
        return 0

    f_str = str(finish)
    # Checking other base case where actual limit is lower than the finish value
    if int(f_str[0]) > limit:
        limit_str = [str(limit) for _ in range(len(f_str))]
        limit_int = int("".join(limit_str))
        if limit_int < s_int:
            return 0
        finish = limit_int
    
    


def main():
    start = 1
    finish = 6000
    limit = 4
    s = "124"
    print(numberOfPowerfulInt(start, finish, limit, s))


if __name__ == "__main__":
    main()
