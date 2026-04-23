class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

# results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

# print(results.count())          # 9
# print(results.get_by_index(2))  # 91
# print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    def get_grade(self,index):
        points = self.scores[index]

        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"

    def find(self,points):
        students = []

        for i in range(len(self.scores)):
            if self.scores[i] == points:
                students.append(i)

        return students

    def get_sorted(self):
        scores = self.scores.copy()
        length = len(scores)

        for i in range(length):
            end = length - i - 1
            for j in range(0,end):
                if scores[j] > scores[j+1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores

from sorting import random_numbers

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # print(results.count())  # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    #
    # print(results.find(100))  # [6]
    # print(results.find(50))  # [4]
    # print(results.find(77))  # []
    #
    # print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    print("Test psalo:", results.count())

    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")

    print("Indexy studentů, kteří měli plný počet bodů:", results.find(100))

    print("Seřazené výsledky od nejhoršího po nejlepšího:", results.get_sorted())

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print("Test psalo:", random_results.count())
    print("Seřazené výsledky od nejhoršího po nejlepšího:", random_results.get_sorted())