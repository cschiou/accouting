from datetime import datetime
from datetime import timedelta
from enum import Enum


class DataType(Enum):
    income = 1
    expense = 2
    transfer = 3


class Account:
    def __init__(self):
        self.__date_list = list()
        # [2015/01/06, account, TWD, class, value, description]
        self.__income_list = list()
        self.__expense_list = list()

        # [2015/01/06, source_account, TWD, target_account, TWD, value]
        self.__transfer_list = list()

        self.__account_list = list()
        self.__account_to_date_value_map = dict()
        self.__init_date = datetime.today()
        self.__delta = self.__init_date.today().date() - self.__init_date.date()

    def set_start_date(self):
        expense_init_date = datetime.strptime(self.__expense_list[0][0], '%Y/%m/%d')
        income_init_date = datetime.strptime(self.__income_list[0][0], '%Y/%m/%d')
        transfer_init_date = datetime.strptime(self.__transfer_list[0][0], '%Y/%m/%d')

        self.__init_date = min(expense_init_date, income_init_date, transfer_init_date)
        self.__delta = self.__init_date.today().date() - self.__init_date.date()

    def init_account_to_value_map(self):
        for account in self.__account_list:
            self.__account_to_date_value_map[account] = list([0])
        # TODO: give account initial value
        self.__account_to_date_value_map['現金'][0] = 14028
        self.__account_to_date_value_map['銀行'][0] = 727440

    def build_date_to_account_value(self):
        self.init_account_to_value_map()
        self.set_start_date()
        expense_count = 0
        income_count = 0
        transfer_count = 0
        income_date = self.__ahorro_date_str_to_datetime(DataType.income, income_count)
        expense_date = self.__ahorro_date_str_to_datetime(DataType.expense, expense_count)
        transfer_date = self.__ahorro_date_str_to_datetime(DataType.transfer, transfer_count)

        for i in range(0, self.__delta.days + 1):
            d = self.__init_date + timedelta(days=i)
            self.__date_list.append(d)

            if i:
                for key, value in self.__account_to_date_value_map.items():
                    value.append(value[-1])

            while expense_date == d:
                account_name = self.__expense_list[expense_count][1].lstrip()
                value = int(self.__expense_list[expense_count][4])
                self.reduce_account_value(account_name, value, i)
                expense_count += 1
                if expense_count == len(self.__expense_list):
                    break
                expense_date = self.__ahorro_date_str_to_datetime(DataType.expense, expense_count)

            while income_date == d:
                account_name = self.__income_list[income_count][1].lstrip()
                value = int(self.__income_list[income_count][4])
                self.increase_account_value(account_name, value, i)
                income_count += 1
                if income_count == len(self.__income_list):
                    break
                income_date = self.__ahorro_date_str_to_datetime(DataType.income, income_count)

            while transfer_date == d:
                account1 = self.__transfer_list[transfer_count][1].lstrip()
                account2 = self.__transfer_list[transfer_count][3].lstrip()
                value = int(self.__transfer_list[transfer_count][5])
                self.transfer_value(account1, account2, value, i)
                transfer_count += 1
                if transfer_count == len(self.__transfer_list):
                    break
                transfer_date = self.__ahorro_date_str_to_datetime(DataType.transfer, transfer_count)

    def increase_account_value(self, account_name, value, delta_date):
        # print("Update " + account_name + "+" + str(value) + " " + str(delta_date))
        self.__account_to_date_value_map[account_name][delta_date] += value

    def reduce_account_value(self, account_name, value, delta_date):
        # print("Update " + account_name + "-" + str(value) + " " + str(delta_date))
        self.__account_to_date_value_map[account_name][delta_date] -= value

    def transfer_value(self, src_account, tar_account, value, delta_date):
        # print("Transfer " + src_account + " to " + tar_account + " " + str(value) + " " + str(delta_date))
        self.__account_to_date_value_map[src_account][delta_date] -= value
        self.__account_to_date_value_map[tar_account][delta_date] += value

    def get_account_value(self, account_name, delta_date):
        if account_name in self.__account_to_date_value_map:
            return self.__account_to_date_value_map[account_name][delta_date]

    def get_account_to_date_value_map(self):
        return self.__account_to_date_value_map

    def append_income_list(self, income):
        self.__income_list.append(income)

    def get_income_list(self):
        return self.__income_list

    def append_expense_list(self, expense):
        self.__expense_list.append(expense)

    def get_expense_list(self):
        return self.__expense_list

    def append_transfer_list(self, transfer):
        self.__transfer_list.append(transfer)

    def get_transfer_list(self):
        return self.__transfer_list

    def append_account_list(self, account):
        self.__account_list.append(account)

    def get_account_list(self):
        return self.__account_list

    def get_init_date(self):
        return self.__init_date

    def get_delta_days(self):
        return self.__delta.days

    def get_date_list(self):
        return self.__date_list

    def __ahorro_date_str_to_datetime(self, data_type, log_id):
        if data_type == DataType.income:
            if log_id == len(self.__income_list):
                log_id = len(self.__income_list) - 1
            return datetime.strptime(self.__income_list[log_id][0], '%Y/%m/%d')
        elif data_type == DataType.expense:
            if log_id == len(self.__expense_list):
                log_id = len(self.__expense_list) - 1
            return datetime.strptime(self.__expense_list[log_id][0], '%Y/%m/%d')
        else:
            if log_id == len(self.__transfer_list):
                log_id = len(self.__transfer_list) - 1
            return datetime.strptime(self.__transfer_list[log_id][0], '%Y/%m/%d')
