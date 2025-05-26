def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        salaries.append(salary)
                    except ValueError:
                        continue
                else:
                    continue

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total / len(salaries)
        return total, average

    except FileNotFoundError:
        return (0, 0)
    except Exception:
        return (0, 0)
