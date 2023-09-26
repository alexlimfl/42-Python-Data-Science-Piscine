import sys

def count_characters(input_string):
	count = 0
	for char in input_string:
		count += 1
	return count




def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_string>")
        sys.exit(1)

    user_input = sys.argv[1]
    character_count = count_characters(user_input)
    print(f"Total number of characters: {character_count}")

if __name__ == "__main__":
    main()
