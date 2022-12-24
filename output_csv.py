import csv
from datetime import timedelta


def output_csv(file, account):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # title = ['日期', '現金', '汽車', '銀行', '台股投資', '美金投資', 'Total']
        title = ['Date'] + account.get_account_list() + ['Total']
        writer.writerow(title)
        for i in range(0, account.get_delta_days() + 1):
            d = account.get_init_date() + timedelta(days=i)

            row_data = [d.date()]
            total = 0
            for account_name in account.get_account_list():
                row_data.append(account.get_account_value(account_name, i))
                total += account.get_account_value(account_name, i)

            row_data.append(total)
            writer.writerow(row_data)
