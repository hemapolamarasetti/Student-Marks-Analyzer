def calculate_grade(avg):
    if(avg >= 90):
        return 'A+'
    elif(avg >= 80):
        return 'A' 
    elif(avg >= 70):
        return 'B'
    elif(avg >= 60):
        return 'C'
    else:
        return 'F'
students={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input(f"\n Enter name of the student {i+1}: ")
    marks=list(map(int,input("Enter marks separated by the space: ").split()))
    avg=sum(marks)/len(marks)
    grade=calculate_grade(avg)
    students[name]={"Marks": marks,"Average": avg,"Grade":grade}
print("\n ===== Students Report =====")
for name,info in students.items():
    print(f"{name} --> Marks:{info["Marks"]} | Average:{info["Average"]:.2f} | Grade:{info["Grade"]} ")