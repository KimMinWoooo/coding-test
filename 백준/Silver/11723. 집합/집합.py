import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    commands = sys.stdin.readline().strip().split()

    if len(commands) == 1:
        # all
        if commands[0] == "all":
            S = set([i for i in range(1, 21)])
        # empty
        else:
            S = set()
    else:
        comm, number = commands[0], commands[1]
        number = int(number)
        # add
        if comm == "add":
            S.add(number)
        # remove
        elif comm == "remove":
            S.discard(number)
        # check
        elif comm == "check":
            print(1 if number in S else 0)
        # toggle
        elif comm == "toggle":
            if number in S:
                S.discard(number)
            else:
                S.add(number)