# import math
# print(dir(math))
# print(math.pi)
# print(math.pow(2,3))

# import datetime
# # print(dir(datetime.datetime))
# # print(datetime.datetime.now())
# # print(datetime.datetime.now().year)
# # new_date = datetime.datetime(1993,5,10)
# today=datetime.datetime.now()
# print(today-new_date)
# date="2020-12-12"
# print(datetime.datetime.strftime(date, "%Y-%m-%d"))

#(1)
# import datetime
# today=datetime.datetime.now()
# b_date =input("enter your birth date (yyyy-mm-dd):")
# n_date = datetime.datetime.strptime(b_date, "%Y-%m-%d")
# if today>n_date:
#     day = today - n_date
#     print("Your birth date is" , day.days, "days ago" )
# else:
#     day = n_date - today
#     print("your birth date is in future", day.days, "days left")


#(2)
jobs =[
    {'title':'python developer', 'salary':20000, 'exp_date':'2025-5-21'},
    {'title':'java developer', 'salary':30000, 'exp_date':'2024-5-21'},
    {'title':'php developer', 'salary':40000, 'exp_date':'2025-5-21'},
    {'title':'web developer', 'salary':50000, 'exp_date':'2022-6-21'},
]

import datetime

for job in jobs:
    job_exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
    today = datetime.datetime.now()
    if today>job_exp_date:
        diff = today - job_exp_date
        print(f"{job['title']} job is expired {diff.days} days ago")
    else:
        diff = job_exp_date - today
        print(f"{job['title']} job is going to expire in {diff.days} days")



#>>>
# jobs = [
#     {'title': 'python developer', 'salary': 20000, 'exp_date': '2025-5-21'},
#     {'title': 'java developer', 'salary': 30000, 'exp_date': '2024-5-21'},
#     {'title': 'php developer', 'salary': 40000, 'exp_date': '2025-5-21'},
#     {'title': 'web developer', 'salary': 50000, 'exp_date': '2022-6-21'},
# ]
# import datetime
# user_input = input("Enter a date (yyyy-mm-dd): ")
# user_date = datetime.datetime.strptime(user_input, "%Y-%m-%d")
# valid_jobs = []

# for job in jobs:
#     job_exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#     if user_date <= job_exp_date:
#         valid_jobs.append(job)

# if valid_jobs:
#     print("You can apply for the following jobs:")
#     for job in valid_jobs:
#         print(f"- {job['title']} (Salary: {job['salary']}, Expiration Date: {job['exp_date']})")
# else:
#     print("No jobs available to apply for.")


# file handling
#exception hendling
# import Os
# import sys
# import global















