import csv
import os


def read_csv(path):
    with open(path, "r") as file:
        data = list(csv.DictReader(file))
        file.close()
    return data


def parent_file(data):
    for idx in range(len(data)):
        if data[idx]["Artist(s)"] not in os.listdir():
            os.mkdir(data[idx]["Artist(s)"])


def sub_file(data):
    for idx in range(len(data)):
        parent_file = data[idx]["Artist(s)"]
        branch_file = data[idx]["Song"]
        path = os.path.join(parent_file + "/", branch_file)
        with open(path, "w") as file:
            file.write("")
            file.close()


album = read_csv("100MostStreamedSongs.csv")
parent_file(album)
sub_file(album)
