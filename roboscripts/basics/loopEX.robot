*** Variables ***
@{MY_LIST}

*** Settings ***


*** Test Cases ***

Test to print odd or even number in a list
    [Tags]   tag1
    #@{MY_LIST} =  create list   0  1  2  3  4  5  6  7  8  9

    :FOR  ${index}  IN RANGE  0  11
    \   @{MY_LIST}[${index}]  ==  ${index}

    :FOR  ${index}  in  @{MY_LIST}
    \   run keyword if   ${index}%2 == 1  keyword 1  ${index}



*** Keywords ***

keyword 1
    [Arguments]  ${INDEX}
    log    ${INDEX}

