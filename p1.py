import pandas as pd
student_grades={
    'students':["sara","lisa","thomas","jilli","gary"],
    'grades':[78,82,95,88,79]
    }
students=pd.DataFrame(student_grades)
print(students)
