print("🌟Contact Card🌟")

name = input("Input your name > ")
date_of_birth = input("Input your date of birth > ")
phone_number = input("Input your telephone number > ")
email = input("Input your email > ")
address = input("Input your address > ")

data = {
    "name": name,
    "date_of_birth": date_of_birth,
    "phone_number": phone_number,
    "email": email,
    "address": address,
}

print(
    f"Hi {data['name']}. Our dictionary says that you were born on {data['date_of_birth']}, we can call you on {data['phone_number']}, email {data['email']}, or write to {data['address']}."
)
