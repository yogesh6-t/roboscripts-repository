*** Settings ***
Library   Collections


*** Variables ***
&{DICTVAR} =  item1=value1  item2=value2  item3=value3  item4=value4

*** Test Cases ***

Check Dict Demo
    [Documentation]  this is ademo of dict in robot framework
    log  ${DICTVAR.item1}
    log  ${DICTVAR.item2}
    log  ${DICTVAR.item3}
    log  ${DICTVAR.item3}

    ${dict_keys} =  Get Dictionary Keys  ${DICTVAR}
    log  ${dict_keys}
    ${dict_values} =  get dictionary values  ${DICTVAR}
    log  ${dict_values}

