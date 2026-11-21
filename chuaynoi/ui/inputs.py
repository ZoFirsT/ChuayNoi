def input_int(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print("[!] กรุณาพิมพ์ตัวเลข")
            continue

        if number < min_value or number > max_value:
            print(f"[!] ต้องอยู่ระหว่าง {min_value} ถึง {max_value}")
            continue

        return number


def input_text(prompt, min_len, max_len):
    while True:
        text = input(prompt).strip()
        if len(text) < min_len or len(text) > max_len:
            if min_len == 0:
                print(f"[!] ต้องไม่เกิน {max_len} ตัวอักษร")
            else:
                print(f"[!] ต้องยาว {min_len} ถึง {max_len} ตัวอักษร")
            continue

        return text


def input_choice(prompt, options):
    print(prompt)
    for number in range(1, len(options) + 1):
        print("  [" + str(number) + "] " + options[number - 1])

    choice = input_int(
        "พิมพ์หมายเลข (1-" + str(len(options)) + "): ", 1, len(options)
    )
    return options[choice - 1]


def input_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer == "y" or answer == "yes":
            return True
        if answer == "n" or answer == "no":
            return False
        print("[!] กรุณาพิมพ์ y หรือ n")
