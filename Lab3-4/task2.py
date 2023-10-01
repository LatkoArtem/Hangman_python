'Task 2'
r = int(input("Enter the student's rating score: "))
if 0 <= r < 60:
    print("R: Unsatisfactory(%s)" % r)
elif 60 <= r < 65:
    print("R: Marginal(%s)" % r)
elif 65 <= r < 75:
    print("R: Satisfactory(%s)" % r)
elif 75 <= r < 85:
    print("R: Good(%s)" % r)
elif 85 <= r < 95:
    print("R: Very good(%s)" % r)
elif 95 <= r <= 100:
    print("R: Excellent(%s)" % r)
else:
    print("Еhe score doesn't correspond to the rating system!")