*** Settings ***
Library   String


*** Test Cases ***
For Loop with upper bound
    [Documentation]   this gives us a 0 based range
    [Tags]  tag1
    :FOR  ${index}   IN RANGE   5
    \   DO Something  ${index}
    \   ${RANDOM_STRING} =  generate random string   ${index}
    \   Log  ${RANDOM_STRING}

For Loop with start and finish range bound
    [Documentation]   no longer a 0 based range because start is provided
    [Tags]  tag2
    :FOR  ${index}   IN RANGE   1   5
    \   DO Something  ${index}
    \   ${RANDOM_STRING} =  generate random string   ${index}
    \   Log  ${RANDOM_STRING}

For Loop with start finish and step range
    [Documentation]   this count will jump by 2 each time
    [Tags]  tag3
    :FOR  ${index}   IN RANGE   1  5   2
    \   DO Something  ${index}
    \   ${RANDOM_STRING} =  generate random string   ${index}
    \   Log  ${RANDOM_STRING}

FOR Loop with List
     @{ITEMS} =    Create List  Item 1 Item 2 Item 3
    :FOR  ${MyItem}  IN   @{ITEMS}
    \   log  ${MyItem}

Exit a FOR Loop
    [Tags]  tag4
    @{ITEMS} =    Create List  Item 1  Item 2  Item 3  Item 4

    :FOR  ${MyItem}  IN   @{ITEMS}
    \   log  ${MyItem}
    \   run keyword if  "${MyItem}" == "Item 4"  exit for loop
    \   log   Didn't exit yet

    log  now we are out of the loop

Repeat a keyword many times
    [Tags]  tag5
    repeat keyword  1   a repeatable keyword
    repeat keyword  2 times   a repeatable keyword
    repeat keyword  3 s   a repeatable keyword

*** Keywords ***

Do Something
    [Arguments]    ${PassedIndex}
    log  I was passd a value of ${PassedIndex}!

A Repeatable Keyword
    log  I am being repeated!