import os
import sys

from playwright.sync_api import sync_playwright


def create_project_structure(project_name):
    # Create the main directory
    project_dir = os.path.join(os.getcwd(), project_name)
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)

    # Create the 'tests' subdirectory
    tests_dir = os.path.join(project_dir, "tests")
    if not os.path.exists(tests_dir):
        os.makedirs(tests_dir)

        # Create the 'main.py' file with a multiline string
    main_file = os.path.join(project_dir, "main.py")
    if not os.path.exists(main_file):
        with open(main_file, "w") as f:
            f.write(
                """\
def solution():
    pass

solution()
"""
            )

    return tests_dir


# FIXME: only works in headless=False
def scrape_problem_samples(problem_number, tests_dir):
    url = f"https://www.acmicpc.net/problem/{problem_number}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        index = 1
        while True:
            try:
                # Set the timeout to 0 for immediate error if element is not found
                input_selector = f"pre#sample-input-{index}"
                output_selector = f"pre#sample-output-{index}"

                # Try to locate the input element with a 0ms timeout
                page.wait_for_selector(input_selector, timeout=1000)
                input_content = page.locator(input_selector).text_content()
                if not input_content:
                    raise Exception("Input not found")

                # Try to locate the output element with a 0ms timeout
                page.wait_for_selector(output_selector, timeout=1000)
                output_content = page.locator(output_selector).text_content()
                if not output_content:
                    raise Exception("Input not found")

                # Write input to a file
                input_file_path = os.path.join(tests_dir, f"{index}.in")
                with open(input_file_path, "w") as input_file:
                    input_file.write(input_content)

                # Write output to a file
                output_file_path = os.path.join(tests_dir, f"{index}.out")
                with open(output_file_path, "w") as output_file:
                    output_file.write(output_content)

                print(f"Sample {index}: Input and Output scraped.")
                index += 1

            except Exception as e:
                # If element is not found (immediate error), stop the loop
                print(f"Sample input/output {index} not found, stopping scraping.")
                break

        browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python prep.py <problem_number>")
        sys.exit(1)

    problem_number = sys.argv[1]
    project_name = problem_number
    tests_dir = create_project_structure(project_name)

    # Scrape the sample inputs/outputs
    scrape_problem_samples(problem_number, tests_dir)
