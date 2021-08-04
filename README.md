# ssl validation
This is used for checking SSL Expiry for a given list of domains.
If domains are found that are expired, or within the provided grace period, they will be sent via an email.






* In addition to the ssl_validator.py file, you will need to create two files in your venv, settings.py which will contain connection information for SMTP, and sites.txt which will be the domains you wish to check. 
* Please ensure that you install the requirements.txt file as well as the script will fail to run due to the missing packages.
