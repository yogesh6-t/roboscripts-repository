*** Settings ***

*** Variables ***
${MY_STR} =   "bbabbbcbb"
#${MY_CHAR} =   "ab"


*** Test Cases ***

Test regular expression
    Validate input String     ${MY_STR}

*** Keywords ***

Validate Input String
    [Arguments]    ${my_str}
    #should match regexp  ${my_str}    "b(bb)*"
    should match regexp  ${my_str}    "(a|c)*b((b(a|c)*b)*(a|c)*)*"
    #should match regexp  ${my_str}    "((a|c)*b(a|c)*(bb)*(a|c)*)*"
    #should match regexp  ${my_str}    "*b(b*b)"
    #should match regexp  ${my_str}    "*b*(bb*)"
    #should match regexp  ${my_str}    "b"
    #should contain x times   ${my_str}   ${my_char}    1
    #get element count