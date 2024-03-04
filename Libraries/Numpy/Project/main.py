import numpy as np
from operationClass import IntArray


def productivity_of_company(order, df):
    return np.sum(df[order], axis=0)


def max_productivity(df):
    i = 0
    best_company = i + 1
    num_of_products = 0

    for i in range(len(df)):
        result = productivity_of_company(i, df)
        if result > num_of_products:
            num_of_products = result
            best_company = i + 1

    print(
        f"The best company is the {best_company}, with {num_of_products} Number of products sold"
    )


def min_productivity(df):
    i = 0
    worst_company = i + 1
    num_of_products = productivity_of_company(0, df)

    for i in range(len(df)):
        result = productivity_of_company(i, df)
        if result <= num_of_products:
            num_of_products = result
            worst_company = i + 1

    print(
        f"The worst company is {worst_company}, with {num_of_products} Number of products sold"
    )


def mean_productivity(df):
    for i in range(len(df)):
        average = np.mean(df[i])
        print(f"On Average, company {i+1} produces {average} product on average")

    products = 0
    employees = 0

    for idx in range(len(df)):
        employee, product = len(df[idx]), np.sum(df[idx])
        employees += employee
        products += product

    total_mean = products / employees
    print(f"On total, average all company {total_mean} products")


def file_handling():
    lines = []
    with open("data.txt", "r") as file:
        for line in file:
            values = line.strip().split(",")
            int_values = [int(val) for val in values]
            lines.append(int_values)

        df = np.array([np.array(row) for row in lines], dtype="object")
        return df


def main():
    df = file_handling()
    print(df)

    first_branch = IntArray(df[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()

    max_productivity(df)
    min_productivity(df)
    mean_productivity(df)


main()
