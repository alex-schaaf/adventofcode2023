def get_lines(fn: str):
    with open(fn, "r") as file:
        lines = file.readlines()
    data = [line.strip() for line in lines]
    return data


def task1(lines: list[str]) -> int:
    calibration_values_sum = 0

    for line in lines:
        calibration_value = ""

        for char in line:
            if char.isdigit():
                calibration_value += char
                break

        for char in line[::-1]:
            if char.isdigit():
                calibration_value += char
                break

        calibration_values_sum += int(calibration_value)

    return calibration_values_sum


def task2(lines: list[str]) -> int:

    def convert_to_digits(line: str) -> str:
        digits = ""

        digits_lut = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

        for i, ch in enumerate(line):
            if ch.isdigit():
                digits += ch

            for number in digits_lut.keys():
                if line[i:].startswith(number):
                    digits += digits_lut[number]

        return digits

    calibration_values_sum = 0
    for line in lines:
        digits = convert_to_digits(line)
        calibration_values_sum += int(digits[0] + digits[-1])

    return calibration_values_sum


if __name__ == "__main__":
    lines = get_lines("input.txt")

    print(f"Task 1: {task1(lines)}")
    print(f"Task 2: {task2(lines)}")
