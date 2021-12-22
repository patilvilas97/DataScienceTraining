def totalExp(JE,AE,SE):             ## Defining the function to find the Total Expenses for 3 months
    total=0
    for i in range(len(JE)):
        total = total + JE[i] + AE[i] + SE[i]
    return total


JulyExpenses = [100,23,45,67,23,90]
AugustExpenses = [19, 4,25,65,678,12]
SeptExpenses = [12, 67, 34,89, 94, 56]

print("Total Expense is",totalExp(JulyExpenses,AugustExpenses,SeptExpenses))