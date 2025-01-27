# 백준

## Scripts

### Preparing for the question

1. `docker build -t <name of the image> .` to build the image
2. `docker container run -v .:/app <name of the image> <language> <problem number>` to populate boilerplate code and the sample inputs and outputs.

### Testing the solution

1. `python3 test_runner.py <command to run the solution file>`
    - for example, `python3 test_runner.py python 1001/main.py`. It has to follow such exact format.
