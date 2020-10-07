import boto3
import paramiko
import time

def launch_app(host_id='3.91.202.234', key_name='Ansible', github_repo='https://github.com/dantso/grafana.git'):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.load_system_host_keys()
    client.connect(hostname=host_id, username="ubuntu", key_filename='./key/'+key_name+'.pem')
    print ("Connected!")
    #stdin, stdout, stderr = client.exec_command('sudo su')
    #print (stdout.readlines())
    stdin, stdout, stderr = client.exec_command('sudo git clone '+github_repo)
    print (stdout.readlines())
    time.sleep(3)
    stdin, stdout, stderr = client.exec_command('sudo bash /home/ubuntu/grafana/shell.sh')
    print (stdout.readlines())
    #time.sleep(3)
    #stdin, stdout, stderr = client.exec_command('python ~/flask-app/app.py &')
    #print (stdout.readlines())
    #client.close()

    print ("Finished")

launch_app()