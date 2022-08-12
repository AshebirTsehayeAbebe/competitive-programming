def gradingStudents(grades):
    remainder=0;
    for i in range(0,len(grades)):
        remainder=grades[i]%5
        if remainder>2 and grades[i]>37:
            grades[i] += 5-remainder
        
    return grades
n = int(input("Enter number of grades : "))   
grades = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
output = gradingStudents(grades)
print(output)