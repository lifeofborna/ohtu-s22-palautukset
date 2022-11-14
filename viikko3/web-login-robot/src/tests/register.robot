*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  borna
    Set Password  borna
    Set PasswordConf  borna
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  b
    Set Password  b
    Set PasswordConf  b
    Submit Credentials
    Register Should Fail With Message  User with username b is too short!

Register With Valid Username And Too Short Password
    Set username  borna
    Set Password  b
    Set PasswordConf  b
    Submit Credentials
    Register Should Fail With Message  Password should more than 3 values

Register With Nonmatching Password And Password Confirmation
    Set username  borna
    Set Password  bor
    Set PasswordConf  bo
    Submit Credentials
    Register Should Fail With Message  check conf

Login After Successful Registration
    Set Username  borna
    Set Password  borna
    Set PasswordConf  borna
    Submit Credentials
    Go To Login Page
    Set Username  borna
    Set Password  borna
    Submit Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  xx2
    Set Password  borna
    Set PasswordConf  bo
    Submit Credentials
    Register Should Fail With Message  check conf
    Go To Login Page
    Set Username  xx2
    Set Password  borna
    Submit Login
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConf
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
