# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:21:42 2020

@author: kshit
"""

class Date(object):

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


    def __le__(self, other: 'Date') -> bool:
        if isinstance(other, Date):
            if self.year < other.year:
                return True
            elif self.year == other.year and self.month < other.month:
                return True
            elif self.month == other.month and self.day < other.day:
                return True 
        return False

    def __add__(self, other: int) -> 'Date':
        if not isinstance(other, int):
            raise TypeError("unsupported operand type(s) for +")

        rv = Date(self.day, self.month, self.year) 
        if rv.day + other > Date.days_to_a_month(rv.month, rv.year):
            other -= Date.days_to_a_month(rv.month, rv.year) - rv.day
            rv.day = 0
            rv.month += 1
        if rv.month > 12:
            rv.month = 1
            rv.year += 1
        rv.day += other
        return rv

    @staticmethod
    def leap_year(year: int) -> bool:
        return ((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0))

    @staticmethod
    def days_to_a_month(month, year):
        usual = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if month == 2 and Date.leap_year(year):
            return 29 
        else:
            return usual[month - 1]

def solve(begin_day, begin_month, begin_year, end_day, end_month, end_year):
    """ Compute the answer to Project Euler's problem #19 """

    lower_bound = Date(begin_day, begin_month, begin_year)
    upper_bound = Date(end_day, end_month, end_year)
    given_date = Date(1, 1, 1900)
    answer = 0

    given_date += 6

    while given_date <= lower_bound:
        given_date += 7 

    while given_date <= upper_bound:
        if given_date.day == 1:
            answer += 1 
        given_date += 7

    return answer

if __name__ == "__main__":
    print(solve(1,1,1901,31,12,2000))