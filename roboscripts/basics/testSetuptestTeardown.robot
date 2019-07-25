*** Settings ***
Test Setup   keyword1
Test Teardown   keyword2

*** Test Cases ***
Test Case 1
    [Documentation]  test case 1
    keyword1

Test Case 2
    [Documentation]  test case 2
    keyword2

*** Keywords ***
keyword1
    log  In Keyword 1

keyword2
    log  In Keyword 2