import random

# write your code here
print("Enter the number of friends joining (including you):")

try:
    number = int(input())
except ValueError:
    print("No one is joining for the party")
else:
    if number < 1:
        print("No one is joining for the party")
    else:
        party_list = []
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(number):
            party_list.append(input())
        print("Enter the total bill value:")
        total_bill = int(input())
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()
        if answer == "Yes":
            lucky_one = random.choice(party_list)
            print(f'{lucky_one} is the lucky one!')
            bill_each = round(total_bill / (number - 1), 2)
            party_dict = {}
            for name in party_list:
                if name == lucky_one:
                    party_dict[name] = 0
                else:
                    party_dict[name] = bill_each
            print(party_dict)
        else:
            print('No one is going to be lucky')
            bill_each = round(total_bill / number, 2)
            party_dict = dict.fromkeys(party_list, bill_each)
            print(party_dict)
