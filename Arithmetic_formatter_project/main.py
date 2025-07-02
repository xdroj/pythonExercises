def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_operands = []
    second_operands = []
    operators = []
    answers = []
    widths = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator."

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        first_operands.append(operand1)
        second_operands.append(operand2)
        operators.append(operator)

        width = max(len(operand1), len(operand2)) + 2
        widths.append(width)

        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers.append(answer)

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for i in range(len(problems)):
        line1.append(first_operands[i].rjust(widths[i]))
        line2.append(operators[i] + ' ' + second_operands[i].rjust(widths[i] - 2))
        line3.append('-' * widths[i])
        if show_answers:
            line4.append(answers[i].rjust(widths[i]))

    arranged_problems = '    '.join(line1) + '\n'+'    '.join(line2) + '\n' + '    '.join(line3)
    if show_answers:
        arranged_problems += '\n' + '    '.join(line4)

    return arranged_problems
