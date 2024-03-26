from app import read_user_input, read_file_default, read_file_pandas
from app import output_to_console, output_to_file

def main():
    while True:

        user_choice = input("1 - input from console, 2 - input from file default, 3 - input from file pandas, 4 - break ")

        if user_choice == "1":
            user_text = read_user_input()
        elif user_choice == "2":
            user_text = read_file_default()
        elif user_choice == "3":
            user_text = read_file_pandas()
        elif user_choice == "4":
            break

        output_to_console(user_text)
        output_to_file(user_text, "output_sample.txt")
    
    return

if __name__ == "__main__":
    main()