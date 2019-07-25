*** Settings ***
Documentation  This is about setting section on test suites Library SelenimLibrary

*** Variables ***
#robot -d Results --critical tag1 Tests/demo1.robot


*** Test Cases ***
Validate Understanding of First Test
    [Documentation]  This is my first test case
    [Tags]  tag1
    Log  "Hello World!"

Validate Understanding of Second Test
    [Documentation]  This is my second test case
    [Tags]  tag2
    Log  "Executing second test case"




