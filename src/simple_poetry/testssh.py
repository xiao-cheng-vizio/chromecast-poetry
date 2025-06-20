import pychromecast
import paramiko
import subprocess

VIDEO_URL = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
TV_INTERNAL_IP = "10.64.156.22 8009"

def main():
    # Create an SSH client and connect to the remote server
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.64.156.22', port=22, username='root', password='root')

    # Execute the bash script on the remote server
    # stdin, stdout, stderr = client.exec_command('SysRegInspector -o GET -k /current/power_manager/appindex/mdns/googlecast/port')
    stdin, stdout, stderr = client.exec_command('echo "mem" > /sys/power/state')

    # # Read and process the output of the command
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

   # print(stdout.readlines())
    print('Output:', output)
    print('Error:', error)

    # Close the SSH connection
    client.close()

if __name__ == '__main__':
    main()