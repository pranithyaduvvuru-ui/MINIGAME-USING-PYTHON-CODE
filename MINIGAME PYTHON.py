import random

questions = {
    "What is the capital of India?": "delhi",
    "What is 5 + 7?": "12",
    "Which planet is known as the Red Planet?": "mars",
    "What is the largest ocean?": "pacific"
}

treasures = ["Gold Coin", "Diamond", "Silver Sword", "Magic Ring"]
bonus_rewards = ("Extra Life", "Shield", "Power Boost")

collected = set()
score = 0
attempts = 3

print("🏴☠️ Welcome to Treasure Hunt Quiz Game!")
print("Answer correctly to collect treasures!")
print("--------------------------------------")

for question, answer in questions.items():
    if attempts == 0:
        print("❌ No attempts left! Game Over!")
        break

    print("\nQuestion:", question)
    user_answer = input("Your Answer: ").lower()

    if user_answer == answer:
        print("✅ Correct!")
        score += 10

        treasure = random.choice(treasures)
        collected.add(treasure)
        print("🎁 You got a treasure:", treasure)

        bonus = random.choice(bonus_rewards)
        print("✨ Bonus Reward:", bonus)

    else:
        print("❌ Wrong answer!")
        attempts -= 1
        print("Attempts left:", attempts)

print("\n🏁 Game Over!")
print("Your Score:", score)
print("Collected Treasures:", collected)
