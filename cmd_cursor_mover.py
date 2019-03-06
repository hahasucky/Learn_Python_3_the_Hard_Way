import sys
que = "are you a student?"
ans = input(que)
sys.stdout.write("\033[{}C".format(len(que + ans)+1))
sys.stdout.write("\033[1A")
print("thank you for participation.")
