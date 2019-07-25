*** Settings ***

*** Variables ***
${MY_VALUE} =   100

*** Test Cases ***
Testing a true IF statement
    run keyword if  ${MY_VALUE} > 50  Keyword 1   ${MY_VALUE}

Testing a false IF statement
    run keyword if  ${MY_VALUE} > 200  Keyword 1   ${MY_VALUE}

Testing a true IF/ELSE statement
    run keyword if  ${MY_VALUE} < 50  Keyword 1    ${MY_VALUE}
    ...  ELSE  Keyword 2

Testing an IF/ELSE IF/ELSE statement
    run keyword if  ${MY_VALUE} > 50  Keyword 1    ${MY_VALUE}
    ...  ELSE IF  ${MY_VALUE} == 10  Keyword 2   ${MY_VALUE}
    ...  ELSE  Keyword 3


*** Keywords ***
Keyword 1
    [Arguments]   ${my_value}
    Log  In Keyword 1
    should be equal  ${my_value}   100

Keyword 2
    [Arguments]   ${my_value}
    Log  In Keyword 2
    should be equal  ${my_value}   200

Keyword 3
    [Arguments]   ${my_value}
    Log  In Keyword 3
    should be equal  ${my_value}   300