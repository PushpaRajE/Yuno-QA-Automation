# Yuno QA Automation Assessment

This repository is created as part of the QA Automation assessment for Yuno.
The goal of this project is to design and automate API test scenarios using
Python and Behave based on the provided payment documentation.

The focus of this project is on:
- Understanding the payment lifecycle
- Writing meaningful Gherkin scenarios
- Covering positive, negative, and edge cases
- Maintaining a clean and readable automation structure

## Tech Stack
- Python
- Behave (BDD framework)
- Requests library for API calls

## Project Structure
features/  
- Contains all Gherkin feature files

features/steps/  
- Step definition files for feature scenarios

utils/  
- Common utilities and API helper methods

test_data/  
- Test data such as card numbers and payload samples

## Setup Instructions
1. Install Python (3.9 or above recommended)
2. Install project dependencies by running: pip install -r requirements.txt

## Execute Tests
Run the following command from the project root directory: behave
