
import random


def math_quiz():
    print("🎉 Oddiy matematik o‘yin — boshladik! 🎉\n")
    score = 0  # Foydalanuvchi balli
    for i in range(5):  # 5 ta savol beradi
        # Tasodifiy sonlar va amal tanlash
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-", "*"])

        # Masalani chiqarish
        if operation == "+":
            correct_answer = num1 + num2
        elif operation == "-":
            correct_answer = num1 - num2
        elif operation == "*":
            correct_answer = num1 * num2

        # Savol va javobni tekshirish
        print(f"{i + 1}-savol: {num1} {operation} {num2} = ?")
        user_answer = int(input("Javobingizni kiriting: "))

        if user_answer == correct_answer:
            print("✅ To‘g‘ri!")
            score += 1
        else:
            print(f"❌ Noto‘g‘ri! To‘g‘ri javob: {correct_answer}")

    # Yakuniy ball
    print("\nO‘yin tugadi!")
    print(f"Yakuniy ballingiz: {score}/5")
    if score == 5:
        print("💯 Ajoyib natija! Matematikani yaxshi bilasiz!")
    elif score >= 3:
        print("👍 Yaxshi natija, lekin hali ustida ishlash kerak!")
    else:
        print("📖 Ko‘proq mashq qiling!")


# O‘yinni ishga tushirish
math_quiz()