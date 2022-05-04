
def main():

    labs = 0
    num_labs = int(input("Enter number of labs to put in: "))
    for x in range(num_labs):
        labs += int(input("Enter lab score: "))
    labs /= num_labs
    midterm = int(input("Enter midterm score: "))
    final = int(input("Enter final score: "))
    total_score(labs, midterm, final)


def total_score(labs, midterm, final):
    weighed_labs = (labs * 34) / 100
    weighed_midterm = (midterm * 33) / 100
    weighed_final = (final * 33) / 100
    weighed_total = weighed_labs + weighed_midterm + weighed_final
    print("Your final grade is", weighed_total)


main()
