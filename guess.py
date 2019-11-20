import random

with open("score.txt", "r") as file_object:
    old_scores_raw = file_object.read()

old_scores_raw = old_scores_raw.split("\n")

old_scores = []
for i in old_scores_raw[:-1]:
    old_scores.append(int(i))

# HOMEWORK - printing out best three results.
old_scores.sort()
first, second, third = old_scores[0:3]
print(f"Best three results are: {first}, {second}, {third}")

min_score = min(old_scores)
print(f"Best result so far is {min_score} tries.")

# exit()

secret_num = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Ugibaj število med 1 in 100: "))
    attempts += 1

    if guess < secret_num:
        print("Guess higher!")
    elif guess > secret_num:
        print("Guess lower!")
    else:
        print(f"You guessed correct number in {attempts} attempts.")
        break


with open("score.txt", "a") as file_object:
    file_object.write(f"{attempts}\n")