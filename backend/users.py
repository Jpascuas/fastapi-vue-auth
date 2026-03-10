import os

def get_users():
    users = []

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "users.txt")

    with open(file_path) as f:
        lines = f.readlines()[1:]

        for line in lines:
            id, name, email, password = line.strip().split(",")

            users.append({
                "id": id,
                "name": name,
                "email": email,
                "password": password
            })

    return users