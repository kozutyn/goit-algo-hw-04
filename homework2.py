def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat = {
                        "id": parts[0].strip(),
                        "name": parts[1].strip(),
                        "age": parts[2].strip()
                    }
                    cats_info.append(cat)
            return cats_info
    except Exception:
        return []
