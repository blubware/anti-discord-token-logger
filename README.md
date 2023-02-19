# Setup
```
Run 'setup.bat' to install required modules
Put your discord token in 'config.json' in the 'token' field
Run 'start.bat'
```
Now you should be setup for anti token-logging!

# Configuring
```
{
    "token": "your-token-here",
    "delay": 30,

    "password_changing": true,
    "password": "",
    "another_password": "",
    "email": "",

    "webhook_logging": true,
    "webhook_url": ""
}
```
```
- 'token' 
-- Your discord token

- 'delay'
-- Delay at which antilogger checks for new sessions

- 'password_changing'
-- Changes password on an unauthorized user logging in

    - 'password'
    -- If 'password_changing' is set to true, fill this out with your current discord password

    - 'another_password'
    -- If 'password_changing' is set to true, fill this out with another password

    - 'email'
    -- If 'password_changing' is set to true, fill this out with your current discord email

- 'webhook_logging'
-- Sends a message with information about any unauthroized user

    - 'webhook_url'
    -- The webhook url to use with webhook logging
```
# Channel-log
```
v0.0.2
- Password change on detection
- Webhook notifications
- Send new discord token to webhook

v0.0.1
- Basic Functionality
```
# To-do
```
Better looking console
Send all potential attacker information available
Panic button for account deletion
```