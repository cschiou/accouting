import csv
from datetime import datetime
from datetime import timedelta


def output_csv(file, account):
    income_list = account.get_income_list()
    expense_list = account.get_expense_list()
    transfer_list = account.get_transfer_list()
    account_list = account.get_account_list()

    account.init_account_to_value_map()
    init_date, delta = account.set_start_date()
    expense_count = 0
    income_count = 0
    transfer_count = 0

    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['日期', '現金', '汽車', '銀行', '台股投資', '美金投資', 'Total'])
        for i in range(0, delta.days + 1):
            d = init_date + timedelta(days=i)

            if income_count == len(income_list):
                income_count = len(income_list) - 1
            if expense_count == len(expense_list):
                expense_count = len(expense_list) - 1
            if transfer_count == len(transfer_list):
                transfer_count = len(transfer_list) - 1
            expense_date = datetime.strptime(expense_list[expense_count][0], '%Y/%m/%d')
            income_date = datetime.strptime(income_list[income_count][0], '%Y/%m/%d')
            transfer_date = datetime.strptime(transfer_list[transfer_count][0], '%Y/%m/%d')

            while expense_date == d:
                account_name = expense_list[expense_count][1].lstrip()
                value = int(expense_list[expense_count][4])
                account.reduce_account_value(account_name, value)
                expense_count += 1
                if expense_count == len(expense_list):
                    break
                expense_date = datetime.strptime(expense_list[expense_count][0], '%Y/%m/%d')

            while income_date == d:
                account_name = income_list[income_count][1].lstrip()
                value = int(income_list[income_count][4])
                account.increase_account_value(account_name, value)
                income_count += 1
                if income_count == len(income_list):
                    break
                income_date = datetime.strptime(income_list[income_count][0], '%Y/%m/%d')

            while transfer_date == d:
                account1 = transfer_list[transfer_count][1].lstrip()
                account2 = transfer_list[transfer_count][3].lstrip()
                value = int(transfer_list[transfer_count][5])
                account.transfer_value(account1, account2, value)
                transfer_count += 1
                if transfer_count == len(transfer_list):
                    break
                transfer_date = datetime.strptime(transfer_list[transfer_count][0], '%Y/%m/%d')

            total = 0
            for account_name in account_list:
                total += account.get_account_value(account_name)

            writer.writerow([d.date(),
                             account.get_account_value('現金'),
                             account.get_account_value('汽車'),
                             account.get_account_value('銀行'),
                             account.get_account_value('台股投資'),
                             account.get_account_value('美金投資'),
                             total])
