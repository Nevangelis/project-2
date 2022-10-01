def main():
    user_file = open("project2.txt", "r")
    all_lines = user_file.readlines()
    for line in all_lines:
        split_line = line.split(':')
        print(f"{all_lines}")