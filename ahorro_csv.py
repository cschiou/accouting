import csv
import os
from Account_ds import Account


def read_csv(file, account):
    if not os.path.exists(file):
        print(file + " does not exist!")
        exit()

    income = False
    expense = False
    transfer = False
    with open(file, 'r', encoding='UTF-8') as fin:
        rows = csv.reader(fin)
        for row in rows:
            if len(row) > 0:
                if '-- 支出 --' in row[0]:
                    expense = True
                elif '-- 收入 --' in row[0]:
                    expense = False
                    income = True
                elif '-- transfer --' in row[0]:
                    income = False
                    transfer = True
                elif row[0] == '日期':
                    continue
                elif expense:
                    account.append_expense_list(row)
                elif income:
                    account.append_income_list(row)
                elif transfer:
                    account.append_transfer_list(row)

    for expense in account.get_expense_list():
        if expense[1].lstrip() not in account.get_account_list():
            account.append_account_list(expense[1].lstrip())
    for income in account.get_income_list():
        if income[1].lstrip() not in account.get_account_list():
            account.append_account_list(income[1].lstrip())
    for transfer in account.get_transfer_list():
        if transfer[1].lstrip() not in account.get_account_list():
            account.append_account_list(transfer[1].lstrip())
        if transfer[3].lstrip() not in account.get_account_list():
            account.append_account_list(transfer[3].lstrip())

    print('Account List: ' + str(account.get_account_list()))
