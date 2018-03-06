import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', password='123')

ssh = paramiko.SSHClient()
ssh.get_transport = transport
stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()