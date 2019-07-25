*** Settings ***
Library  ../Library/addition.py
Library  ../Library/CSVreader.py

*** Keywords ***
Calculate Addition
    [Arguments]   ${arg1}   ${arg2}
    ${result} =   addition demo  ${arg1}  ${arg2}
    [Return]  ${result}


Open CSV File
    [Arguments]  ${filename}
    ${fileObj} =  open csv file from device  ${filename}
    [Return]  ${fileObj}

Read First Line from File
    [Arguments]  ${fileobject}
    ${line} =  read first line from device  ${fileobject}
    [Return]  ${line}

Close CSV File
    [Arguments]  ${fileobject}
    close csv file from device  ${fileobject}

    