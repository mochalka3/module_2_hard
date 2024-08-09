def generate_password(n):
    password = ""

    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j

            if n % pair_sum == 0:
                password += f"{i}{j}"

    return password


for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - {result}")
