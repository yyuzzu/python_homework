# Task 1: Hello
def hello():
    return "Hello!"


# Task 2: Greet with a formatted string
def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator
def calc(first, second, operation="multiply"):
    try:
        if operation == "add":
            return first + second
        elif operation == "subtract":
            return first - second
        elif operation == "multiply":
            return first * second
        elif operation == "divide":
            return first / second
        elif operation == "modulo":
            return first % second
        elif operation == "int_divide":
            return first // second
        elif operation == "power":
            return first ** second
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# Task 4: Data type conversion
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."


# Task 5: Grading system using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."


# Task 6: Repeat using a for loop and range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


# Task 7: Student scores using **kwargs
def student_scores(mode, **kwargs):
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)


# Task 8: Title capitalization
def titleize(title):
    little_words = ("a", "on", "an", "the", "of", "and", "is", "in")
    words = title.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return " ".join(words)


# Task 9: Hangman
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# Task 10: Pig Latin
def pig_latin(sentence):
    translated = []
    for word in sentence.split():
        index = 0
        while index < len(word) and word[index] not in "aeiou":
            if word[index:index + 2] == "qu":
                index += 2
            else:
                index += 1
        translated.append(word[index:] + word[:index] + "ay")
    return " ".join(translated)


if __name__ == "__main__":
    print(hello())
    print(greet("James"))
    print(calc(5, 6))
    print(data_type_conversion("110", "int"))
    print(grade(75, 85, 95))
    print(repeat("up,", 4))
    print(student_scores("best", Tom=75, Angela=91))
    print(titleize("war and peace"))
    print(hangman("alphabet", "ab"))
    print(pig_latin("the quick brown fox"))
# Write your code here.
