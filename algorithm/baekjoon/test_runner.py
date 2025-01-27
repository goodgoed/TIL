import os
import subprocess
import sys
from glob import glob

# Check if the user has provided the correct arguments
if len(sys.argv) < 3:
    print("Usage: python3 my_script.py <language> <program_path> [additional arguments]")
    print("Example: python3 my_script.py java 1001/Main.java")
    sys.exit(1)

# Extract the language and program path from the command
command = sys.argv[1:]
program_path = sys.argv[2]

# Check if the program path exists
if not os.path.exists(program_path):
    print(f"Error: The file '{program_path}' does not exist.")
    sys.exit(1)

# Get the problem number (extract it from the program path)
problem_number = os.path.dirname(program_path)

# Get any additional arguments passed by the user (after the program path)
additional_args = sys.argv[3:]  # Everything after the second argument

# Define your input and output file paths
input_files = sorted(glob(f"{problem_number}/tests/*.in"))  # Find all .in files

for input_file in input_files:
    # Derive the expected output file name by replacing .in with .out
    output_file = input_file.replace(".in", ".out")

    # Extract the test case number (filename without extension)
    test_case_number = os.path.basename(input_file).replace(".in", "")

    # Read the expected output (the return code) from the .out file
    with open(output_file, "r") as f_out:
        expected_output = f_out.read().strip()

    # Run the program using the .in file as input and additional arguments
    with open(input_file, "r") as f_in:
        process = subprocess.run(
            command,  # Pass the command with additional arguments
            stdin=f_in,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    # Get the actual output (stdout)
    actual_output = process.stdout

    # Normalize both actual and expected output
    def normalize(output):
        # Split into lines, strip each line of trailing spaces, and rejoin with newline
        return "\n".join([line.rstrip() for line in output.splitlines()])

    normalized_actual_output = normalize(actual_output)
    normalized_expected_output = normalize(expected_output)

    # Compare the actual output with the expected output
    if normalized_actual_output == normalized_expected_output:
        print(f"Test case {test_case_number} - Success!")
    else:
        print(f"Test case {test_case_number} - Failure:")
        print(f"  Expected: {expected_output}")
        print(f"  Got: {actual_output}")

