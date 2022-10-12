def print_monthly_deposits():
    interest_rate = 3.5
    interest_rate = interest_rate/100
    one_million = 1000000
    monthly_deposit_start = 3000
    list = []
    list.append(monthly_deposit_start)

    while sum(list) < one_million:
        new_monthly_deposit = list[-1] + (list[-1]*interest_rate)
        list.append(new_monthly_deposit)

    print(f"Collaborative Performance Task in Math and Computer\n\
            Saving up for my Dream House\ncreated by: Nicole Goot\n\
            Type in interest rate:{interest_rate}\n\
            Type in the monthly deposit:{monthly_deposit_start}\n\
            Monthly Amount")

    number = 0
    for each in list:
        print(number, each)
        number += 1

print_monthly_deposits()