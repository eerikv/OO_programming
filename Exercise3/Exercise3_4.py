# File name:    Exercise3_4.py
# Author:       Eerik Vainio
# Description:  The program takes in examinees and their exam points.
#               Creates a new list with examinees, who passed a given
#               threshold.

class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'Exam submission (examinee: {self.examinee}, points: {self.points})'

def passed(submissions: list, lowest_passing: int):
    new_list = []
    for x in submissions:
        if x.points >= lowest_passing:
            new_list.append(x)
    return(new_list)

if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)
