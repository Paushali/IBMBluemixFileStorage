import swiftclient.client as swiftclient
auth_url = 'https://identity.open.softlayer.com/v3'
project_id = ''
user_id ='****'
region_name = 'dallas'
password = '****'
conn = swiftclient.Connection(
        key=password,
        authurl=auth_url,
        auth_version='3',
        os_options={"project_id": project_id,
                             "user_id": user_id,
                             "region_name": region_name})
container_name = 'yet-another-container'
file_name = 'trial_file.txt'

#create container in IBM bluemix
conn.put_container(container_name)
print "\nContainer %s created successfully." % container_name
print ("\nContainer List:")
for container in conn.get_account()[1]:
    print container['name']

#encryption
import gnupg
gpg = gnupg.GPG(gnupghome = 'C:\Program Files (x86)\GNU\GnuPG/.gnupg')
input_data = gpg.gen_key_input(key_type ="RSA",key_length = 1024,name_email='paushali.kundu@mavs.uta.edu',
                                   passphrase='frozen')
key=gpg.gen_key(input_data)
with open(file_name,'rb') as trial_file:
    status = gpg.encrypt_file(trial_file, recipients=['paushali.kundu@mavs.uta.edu'],output= 'G:\encrypted.txt.gpg')
print 'ok: ', status.ok
print 'status: ', status.status
print 'stderr: ', status.stderr
	
with file(file_name) as f:
    s = f.read()

#uploads file to container
with open(file_name, 'r') as trial_file:
    conn.put_object(container_name,
    file_name,
    contents= s,
    content_type='text/plain')

#lists objects in the container
print ("\nObject List:")
for container in conn.get_account()[1]:
    for data in conn.get_container(container['name'])[1]:
        print 'object: {0}\t size: {1}\t date: {2}'.format(data['name'], data['bytes'], data['last_modified'])

#download file
file_name2='download_file.txt'
obj = conn.get_object(container_name, file_name)
with open(file_name2, 'w') as download_file:
       download_file.write(obj[1])
       print "\nObject %s downloaded successfully." % file_name2

#decryption
with open('G:\encrypted.txt.gpg', 'rb') as f:
    status = gpg.decrypt_file(f, passphrase='frozen', output='G:\my-decrypted.txt')

print 'ok: ', status.ok
print 'status: ', status.status
print 'stderr: ', status.stderr


