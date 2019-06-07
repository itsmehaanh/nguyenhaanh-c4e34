employees = [
{
    "name" : "Đức",
    "salary" : 30,
    "hours": 8,
    "days": 20,
},
{
    "name" : "Hoan",
    "salary" : 50,
    "hours" : 5,
    "days" : 25,
},
{
    "name" : "Đạt",
    "salary" : 40,
    "hours" : 7,
    "days" : 30,
}
]
total_salary = 0
for x in employees:
    month_salary = x["salary"] * x["hours"] * x["days"]
    total_salary += month_salary
    print("Lương tháng của {0} là {1}". format(x["name"], month_salary))

print("Tổng lương của 3 người là {0}".format(total_salary))
