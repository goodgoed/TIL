import os
import subprocess
import sys
from glob import glob

# Check if problem number is provided
if len(sys.argv) < 2:
    print("Please provide the problem number as the first argument.")
    sys.exit(1)

# Get the problem number from the first argument
problem_number = sys.argv[1]

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

    # Run your program using the .in file as input
    with open(input_file, "r") as f_in:
        process = subprocess.run(
            ["python3", f"{problem_number}/main.py"],  # Replace with your command
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
