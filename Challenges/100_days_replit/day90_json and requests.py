import requests


def saved_images(name, picture):
    with open(f"{name}.jpg", "wb") as f:
        f.write(picture.content)


for _ in range(10):
    result = requests.get("https://randomuser.me/api/")
    user = result.json()

    name = (
        user["results"][0]["name"]["first"] + " " + user["results"][0]["name"]["last"]
    )
    image_medium = user["results"][0]["picture"]["medium"]

    picture_medium = requests.get(image_medium)

    saved_images(name, picture_medium)
