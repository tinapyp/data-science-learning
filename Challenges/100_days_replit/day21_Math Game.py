print('Math Game!')

pertanyaan = [
    "1. Berapakah hasil dari 5 + 3?",
    "2. Jika 7 dikurangi 2, berapakah hasilnya?",
    "3. Jika 4 dikalikan dengan 6, berapakah hasilnya?",
    "4. Berapakah hasil dari 12 dibagi dengan 3?",
    "5. Jika 8 ditambah 2, berapakah hasilnya?",
    "6. Jika 15 dikurangi 9, berapakah hasilnya?",
    "7. Berapakah hasil dari 10 dikali 2?",
    "8. Jika 18 dibagi dengan 6, berapakah hasilnya?",
    "9. Jika 25 ditambah 15, berapakah hasilnya?",
    "10. Berapakah hasil dari 9 dikurangi 4?",
]

correct_answer = [
    8,
    5,
    24,
    4,
    10,
    6,
    20,
    3,
    40,
    5,
]
try:
    counter = 0

    for idx, question in enumerate(pertanyaan):
        user = int(input(question + " : "))
        if user != correct_answer[idx]:
            print("Nope! 😭, The answer is {}".format(correct_answer[idx]))
        else:
            counter += 1
            print("Great Work 😋")
    print("You scored {} out of 10".format(counter))
except Exception as e:
    print(f'The program Broke by {e}')
