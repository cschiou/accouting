from datetime import datetime


class Account:
    def set_start_date(self):
        expense_init_date = datetime.strptime(self.__expense_list[0][0], '%Y/%m/%d')
        income_init_date = datetime.strptime(self.__income_list[0][0], '%Y/%m/%d')
        transfer_init_date = datetime.strptime(self.__transfer_list[0][0], '%Y/%m/%d')

        init_date = min(expense_init_date, income_init_date, transfer_init_date)
        delta = init_date.today().date() - init_date.date()
        return init_date, delta

    def init_account_to_value_map(self):
        for account in self.__account_list:
            self.__account_to_value_map[account] = 0
        # TODO: give account initial value
        self.__account_to_value_map['現金'] = 14028
        self.__account_to_value_map['銀行'] = 727440

    def increase_account_value(self, account_name, value):
        if account_name in self.__account_to_value_map:
            self.__account_to_value_map[account_name] += value

    def reduce_account_value(self, account_name, value):
        if account_name in self.__account_to_value_map:
            self.__account_to_value_map[account_name] -= value

    def transfer_value(self, src_account, tar_account, value):
        if src_account in self.__account_to_value_map and \
                tar_account in self.__account_to_value_map:
            self.__account_to_value_map[src_account] -= value
            self.__account_to_value_map[tar_account] += value

    def get_account_value(self, account_name):
        if account_name in self.__account_to_value_map:
            return self.__account_to_value_map[account_name]

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

    __income_list = []
    __expense_list = []
    __transfer_list = []
    __account_list = []
    __account_to_value_map = {}
