import random

digits = list(range(10))
random.shuffle(digits)

ans = digits[:3]

while True:
    guess = input("Enter you number: ")
    guess_ans = []
    for val in guess:
        guess_ans.append(int(val))

    close_ans = False
    match_ans = False
    nope_ans = False
    cnt = 0
    for val in guess_ans:
        if val == ans[guess_ans.index(val)]:
            match_ans = True
            cnt += 1
        elif val in ans:
            close_ans = True
    if cnt == 3:
        break
    if not close_ans and not match_ans:
        nope_ans = True

    if match_ans:
        print("There is a match in the answer")
    if close_ans:
        print("It is close to the answer")
    if nope_ans:
        print("It is nowhere near the answer lol")

print("Congratz")
