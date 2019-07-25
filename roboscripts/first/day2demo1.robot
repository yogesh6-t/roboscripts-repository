*** Settings ***
Documentation  "This is my test suite documentation"

*** Variables ***

*** Test Cases ***
Test my first test case
    [Documentation]  "This is my first demo test case"
    Log  "Logging string in first test case"

Test my second test case
    [Documentation]  "Second test case"
    [Tags]  tag1
    Log  "Logging string in first second case"

Test my third test case
    [Documentation]  "third test case"
    [Tags]  tag2
    Log  "Logging string in third test case"