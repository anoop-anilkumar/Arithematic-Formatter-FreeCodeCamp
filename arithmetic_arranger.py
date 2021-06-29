def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
      return "Error: Too many problems."

    arranged_problems = []

    for index , value in enumerate(problems):
      operation = value.split(" ")

      if operation[1] not in "+-":
        return "Error: Operator must be '+' or '-'."

      if len(operation[0]) > 4 or len(operation[2]) > 4:
        return "Error: Numbers cannot be more than four digits."

      try:
        value1 = int(operation[0])
        value2 = int(operation[2])
      except:
        return "Error: Numbers must only contain digits."

      width = max(len(operation[0]) , len(operation[2])) + 2
      L1 = f"{operation[0]:>{width}}"
      L2 = operation[1] + f"{operation[2]:>{width-1}}"
      line = "-" * width

      try:
        arranged_problems[0] += ('    ') + L1
      except IndexError:
        arranged_problems.append(L1)
      
      try:
        arranged_problems[1] += ('    ') + L2
      except IndexError:
        arranged_problems.append(L2)
      
      try:
        arranged_problems[2] += ('    ') + line
      except IndexError:
        arranged_problems.append(line)

      if args:
        if operation[1] == "+":
          result = value1 + value2
        else:
          result = value1 - value2
        a =f"{str(result):>{width}}"

        try:
          arranged_problems[3] += ('    ') + a
        except:
          arranged_problems.append(a)

      output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
      output = output + f"\n{arranged_problems[3]}" if args else output

    return output
