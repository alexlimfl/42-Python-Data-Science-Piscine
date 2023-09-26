def count_characters(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count

def main():
    user_input = input("Enter a string: ")
    character_count = count_characters(user_input)
    print(f"Total number of characters: {character_count}")

if __name__ == "__main__":
    main()
