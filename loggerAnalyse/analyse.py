
def analyse_file(filename: str) -> list:
    try:
        with open(filename,'r') as f:
            lines = f.readlines()
            # Clean up the lines
            lines = [line.strip() for line in lines]
    except FileNotFoundError:
        print("File couldn't be found :<\nExiting program...")
        exit()
    else:
        # Loop through each character and adjust flags where needed. The flags should help in finding potential passwords
        password_flags = []
        for line in lines:
            has_number = False
            has_special = False
            for char in line:
                if char.isdigit():
                    has_number = True
                if char != ' ':
                    if not char.isalpha():
                        has_special = True
            if has_number or has_special:
                print(has_number, has_special)
                password_flags.append(line)
        return password_flags
