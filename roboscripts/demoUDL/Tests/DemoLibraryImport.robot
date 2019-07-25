*** Settings ***
Resource   ../Resources/LibraryResource.robot

*** Variables ***
${CSV_FILENAME} =   ../Resources/DemoCSVFile.csv
${VAL} =   Value13
#robot -d Rsults -i currentRun Tests/DemoLibraryImport.robot

*** Test Cases ***
Validated Successful addition of Numbers
    [Documentation]  Test case fto validate user defined library import
    [Tags]  lastRun
    ${param1} =  set variable  2
    ${param2} =  set variable  3

    ${value1} =  convert to number  ${param1}
    ${value2} =  convert to number  ${param2}

    ${result} =  Calculate Addition  ${value1}   ${value2}
    should be equal as numbers  5  ${result}


Read from CSV file
    [Documentation]  this is a test to read from CSV file
    [Tags]  currentRun
    ${fileObj} =  Open CSV File  ${CSV_FILENAME}
    should not be equal  ${None}  ${fileObj}


    ${line} =   Read First Line from File  ${fileObj}
    should not be empty   ${line}
    #Log  ${VAL} ${line}[2]
    should be equal   ${line}[2]   ${VAL}
    Close CSV file  ${fileObj}
