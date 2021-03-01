from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

API_key = 'W3JSF1ARJ5QB2RDA'


def get_option():
    print('Please inform one of the following options:\n1 - Stock Time Series\n2 - Fundamental Data\n')
    if validation_user_input('OPTION NUMBER: ', ['1', '2'], True) == '1':
        return StockTimeSeries.display_options_ts(TimeSeries(key=API_key, output_format='pandas'))
    else:
        return Fundamental.display_options_fd(FundamentalData(key=API_key, output_format='pandas'))


def validation_user_input(message, possible_inputs, case_sensitive):
    """
    Checks the information given according to the established validation criteria
    """
    user_input = input(message).lower()

    if case_sensitive:
        while user_input not in possible_inputs:
            print('Please enter a valid option')
            user_input = input(message).lower()
    else:
        while user_input not in [choice for choice in possible_inputs]:
            print('Please enter a valid option')
            user_input = input(message)
    return user_input


class Fundamental:

    @classmethod
    def display_options_fd(cls, fd):
        print('Please inform one of the following options:\n'
              '1 - Company Overview\n'
              '2 - Balance Sheet Annual\n'
              '3 - Cash Flow Annual\n'
              '4 - Income Statement Annual\n')
        cls.get_user_choice_fd(fd)

    @classmethod
    def get_user_choice_fd(cls, fd):
        """
        Gets the option from the client and validates it
        """
        return cls.chosen_company_fd(fd, validation_user_input('OPTION NUMBER: ', ['1', '2', '3', '4'], True))

    @classmethod
    def chosen_company_fd(cls, fd, option):
        return cls.return_selected_option_fd(fd, option, input('choose the company:').upper())

    @staticmethod
    def return_selected_option_fd(fd, option_chosen, company):
        """
        Directs the client according to the requested option
        """
        if option_chosen == '1':
            print(fd.get_company_overview(company)[0])
        elif option_chosen == '2':
            print(fd.get_balance_sheet_annual(company)[0])
        elif option_chosen == '3':
            print(fd.get_cash_flow_annual(company)[0])
        else:
            return print(fd.get_income_statement_annual(company)[0])


class StockTimeSeries:

    @classmethod
    def display_options_ts(cls, ts):
        print('Please inform one of the following options:\n1 - Intraday\n2 - Daily\n3 - Weekly\n4 - Monthly\n')
        cls.get_user_choice_ts(ts)

    @classmethod
    def get_user_choice_ts(cls, ts):
        """
        Gets the option from the client
        """
        return cls.chosen_company_ts(ts, validation_user_input('OPTION NUMBER: ', ['1', '2', '3', '4'], True))

    @classmethod
    def chosen_company_ts(cls, ts, option):
        return cls.return_selected_option_ts(ts, option, input('choose the company:').upper())

    @staticmethod
    def return_selected_option_ts(ts, option_chosen, company):
        if option_chosen == '1':
            print(ts.get_intraday(company)[0])
        elif option_chosen == '2':
            print(ts.get_daily(company)[0])
        elif option_chosen == '3':
            print(ts.get_weekly(company)[0])
        else:
            return print(ts.get_monthly(company)[0])

