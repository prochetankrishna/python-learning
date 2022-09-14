age = 21
is_voter_id_available = True

if age > 18 and is_voter_id_available is True:
    print("You are eligible to vote !")
else:
    print("You are not eligible to vote")

print("You are eligible to vote !") if age > 18 and is_voter_id_available is True else print("You are not eligible to vote")

marks = 75
if marks > 70:
    print("A")
elif marks > 40:
    print("B")
else:
    print("C")

is_pass_or_fail = True if marks > 40 else False
print(is_pass_or_fail)