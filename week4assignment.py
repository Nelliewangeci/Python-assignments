# This program reads a file, modifies its content, and writes the modified content to a new file and handles errors.

def read_and_modify_file():
    # Ask the user to enter the name of the file to read
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try to open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read all lines from the file into a list
            lines = infile.readlines()
        
        # Modify the lines (in this case, convert each line to uppercase)
        modified_lines = [line.upper() for line in lines]

        # Create a new filename for the output
        output_filename = "modified_" + input_filename

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            # Write the modified lines to the new file
            outfile.writelines(modified_lines)

        # Let the user know the operation was successful
        print(f"Modified file has been saved as '{output_filename}'")

    # Handle the case where the input file does not exist
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    
    # Handle other I/O related errors
    except IOError:
        print("❌ Error: Could not read or write the file.")
    
    # Catch any other unexpected errors
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Call the function to run the program
read_and_modify_file()
