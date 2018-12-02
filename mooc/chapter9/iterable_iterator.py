# _*_ coding: utf-8 _*_


class Company(object):

    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return 1

    # def __getitem__(self, item):
    #     return self.employee[item]


if __name__ == "__main__":
    company = Company(["tom", "bob", "jane"])
    my_itor = iter(company)
    for item in company:
        print(item)
