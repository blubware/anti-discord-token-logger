<img src="https://blubware.xyz/assets/screenshots/R891M3h5U9b8.png">

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
    "token": "",
    "delay": 30,

    "password_changing": false,
    "password": "",
    "another_password": "",
    "email": "",

    "webhook_logging": true,
    "webhook_url": "",

    "panic": false
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

- 'panic'
-- Automatically disable/delete your account when an unauthorized user logs into your account
```
# Channel-log
```
v0.0.4
- Added attacker information in logfiles/webhook notifications
- Change password rapidly, can be used for trolling loggers ;)

v0.0.3
- Checks last access time for Discord, DiscordPTB and Discord Canary, useful for checking if you've been logged or checking programs you may suspect to be loggers
- Panic Disable option

v0.0.2
- Password change on detection
- Webhook notifications
- Send new discord token to webhook

v0.0.1
- Basic Functionality
```
# To-do
```
- Send all potential attacker information available
```