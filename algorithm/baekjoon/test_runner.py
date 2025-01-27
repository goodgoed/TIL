import os
import subprocess
import sys
from glob import glob

# Check if the user has provided the correct arguments
if len(sys.argv) < 3:
    print("Usage: python3 my_script.py <problem_number> <command> [additional arguments]")
    print("Example: python3 my_script.py 1001 'python3' 1001/Main.py")
    sys.exit(1)

# Extract the problem number and the command from the arguments
problem_number = sys.argv[1]
command = sys.argv[2:]  # The command itself can have multiple parts

# Check if the problem number directory exists
if not os.path.isdir(problem_number):
    print(f"Error: The problem number '{problem_number}' does not exist as a directory.")
    sys.exit(1)

# Define the input files for testing
input_files = sorted(glob(f"{problem_number}/tests/*.in"))  # Find all .in files

# Loop through each input file and run the test cases
for input_file in input_files:
    # Derive the expected output file name by replacing .in with .out
    output_file = input_file.replace(".in", ".out")

    # Extract the test case number (filename without extension)
    test_case_number = os.path.basename(input_file).replace(".in", "")

    # Read the expected output from the .out file
    with open(output_file, "r") as f_out:
        expected_output = f_out.read().strip()

    # Run the command using the .in file as input and additional arguments (if provided)
    with open(input_file, "r") as f_in:
        process = subprocess.run(
            command,  # Run the provided command directly
            stdin=f_in,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    # Get the actual output from the program's stdout
    actual_output = process.stdout

    # Normalize both actual and expected output (strip trailing spaces, etc.)
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

