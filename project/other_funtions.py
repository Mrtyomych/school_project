import json
import random

class Functions:
    def get_the_fourth_task() -> tuple:
        with open("files/ex4.json", "r", encoding="utf-8") as file:
            data = list(json.load(file).items())

            amount_true_answers = random.randint(2,4)
            true_answers = [random.choice(data)[0] for i in range(amount_true_answers)]  
            false_answers = [random.choice(random.choice(data)[1]) for i in range(5-amount_true_answers)]  
            result = true_answers.copy() + false_answers.copy()
            random.shuffle(result)
            #result - список слов, в которых выделено ударение

            answer = ""
            for i in range(len(result)):
                if result[i] in true_answers:
                    answer += str(i+1)
            #answer - номера верно выделенных в словах ударений 

            list_with_wrong_anwers = []
            while len(list_with_wrong_anwers) < 3:
                numbers = "12345"
                temp = ""
                for i in numbers:
                    temp_2 = random.randint(0,2)
                    if temp_2:
                        temp += i
                if (temp != "") and (temp != result) and (temp not in list_with_wrong_anwers):
                    list_with_wrong_anwers.append(temp)
            #list_with_wrong_anwers - список со случайными числами, которые состоят из цифр от 1 до 5. 

            return (result, answer, list_with_wrong_anwers)
        
    def get_the_fifth_task():
        with open("files/ex5.json", "r", encoding="utf-8") as file:
            f = list(json.load(file).items())
            data = random.choice(f)
            words = data[0].split()
            values = data[1]
            random_value = random.choice(values)
            number_of_random_value = values.index(random_value) + 1
            return (words, random_value, number_of_random_value)
