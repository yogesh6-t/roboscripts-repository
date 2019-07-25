*** Settings ***

*** Variables ***
${MY_STR} =   "abcd"


*** Test Cases ***

Test regular expression
    Validate input String     ${MY_STR}


*** Keywords ***

Validate Input String
    [Arguments]    ${my_str}
    should match regexp  ${my_str}   "abc"