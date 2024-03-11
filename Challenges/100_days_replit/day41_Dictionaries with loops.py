print("🌟Website Rating🌟")

df = {"web_name": None, "url": None, "description": None, "rating": None}


def get_data(data_frame):
    web_name = input("Input the website name: ")
    URL = input("Input the URL: ")
    description = input("Input a description: ")
    rating = int(input("Input a star rating out of 5: "))

    data_frame["web_name"] = web_name
    data_frame["url"] = URL
    data_frame["description"] = description
    data_frame["rating"] = rating


def display(data_frame):
    for key, values in data_frame.items():
        if key == "rating":
            print(f"{key}: {values*'*'}")
        else:
            print(f"{key}: {values}")


def main():
    get_data(df)
    display(df)


main()
