# Test-Driven-Development
Test Driven Development is a software development approach where one only writes new code if there exists at least one failing unit test. 
In TDD, developers follow a cycle of writing failing tests, implementing the minimum code necessary to pass those tests, and then refactoring the code as needed.
The steps for TDD are as follows:

1. Write a test
2. Run all currently written tests
  - If the tests all pass, return to Step 1
  - If a test fails, proceed to Step 3
3. Write the bare minimum of code to make the test pass
4. Run all the currently written tests
  - If tests all pass, return to Step 1
  - If the failing test is still failing, return to Step 3
5. Occasionally evaluate if the code can be refactored to reduce duplication or eliminate no longer used parts of the code
6. Eventually, stop development after adding "enough" tests without triggering a new failure

## Benefits of TDD
### It Forces You to Think About the Requirements
TDD forces the developers to really think about the specifications and expected behavior for each feature. 
In order to write the unit tests first, the developer really has to think about appropriate user stories and use cases.

### Sets a Good Indicator of "Done"
For Agile development, where teams conduct sprints between frequent releases, knowing when the code meets the bare requirements helps not waste time.

### Reduces Duplicate Code
With TDD, if a feature is to be added to existing code, unit tests are developed first, based on the requirements of the feature. 
New code is only written if these new tests fail, otherwise, it means the functionality already exists. 
This helps keep multiple developers from implementing the same functionality and thus wasting time.

## Project Description
The purpose of this project is to utilize Test Driven Development to implement a program that checks the validity of a password given the following specifications:

check_pwd accepts a string and returns a boolean: True if it meets the criteria listed below, otherwise it returns False:
* Must be between 8 and 20 characters (inclusive)
* Must contain at least one lowercase letter (standard English alphabet)
* Must contain at least one uppercase letter (standard English alphabet)
* Must contain at least one digit
* Must contain at least one symbol from: ~`!@#$%^&*()_+-=

To demonstrate the steps taken when using TDD, a new commit was created each time either one of the following occurred:

1. A failing test is written or code is implemented
2. Implemented code caused a failing test to pass

For each commit, there is a message describing the changes made. 

## Observing the Test Driven Development Proccess
* Begin by clicking on "commits" in the Test-Driven-Development repository
* Navigate to the bottom of the page to find the earliest commit and open it
* Observe the changes made to code
* Click back to the previous page and open the next commit
The final commit will contain a complete test suite and code that meets all required specifications.

