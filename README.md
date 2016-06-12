# IBMBluemixFileStorage
This dropbox like storage helps a user to upload their files onto IBM Bluemix and has encryption and decryption facilities for a secure file storage.

Instructions:
pip install python-swiftclient
pip install python-keystoneclient

Set up IBM bluemix account, click on Cloud Foundry App and choose Web App.
Choose Python as the starting point.
Add Object Storage as a service
On the left side, choose environment variables.
You will find the credentials there.
Connect to your app using the following in the python code
In the below code append auth_url + ‘/V3’
update the code with the credentials in the environment variables.

Use Python 2.7 commandline or IDLE by running the file:
python SecureDropBox.py
Take a text file and name it as trial_file.txt and load it in the same directory the SecureDropBox.py file is in.
