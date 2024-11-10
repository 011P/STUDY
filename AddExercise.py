grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = grades[0] ; average = sum(a) / len(a) ; b = grades[1] ; average2 = sum(b) / len(b)
c = grades[2] ; average3 = sum(c) / len(c) ; d = grades[3] ; average4 = sum(d) / len(d)
e = grades[4] ; average5 = sum(e) / len(e)
students = (sorted(students))
print(students[0],': ', average, students[1],': ', average2, students[2],': ', average3,
      students[3],': ', average4, students[4],': ', average5)
