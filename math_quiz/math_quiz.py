import random

def get_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value, inclusive.

    Args:
        min_value (int): The minimum value.
        max_value (int): The maximum value.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Choose a random mathematical operator among '+', '-', or '*'.

    Returns:
        str: A randomly selected operator.
    """
    operators = ['+', '-', '*']
    return random.choice(operators)

def generate_math_problem():
    """
    Generate a random math problem with two numbers and an operator.

    Returns:
        tuple: A tuple containing the math problem as a string and the correct answer.
    """
    num1 = get_random_integer(1, 10)
    num2 = get_random_integer(1, 5)
    operator = get_random_operator()

    problem = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        problem, answer = generate_math_problem()
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
