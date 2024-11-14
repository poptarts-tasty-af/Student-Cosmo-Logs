# Push data to server

import paramiko
from scp import SCPClient
import os

def create_ssh_client(hostname, port, username, password):
    """Create and return an SSH client."""
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=port, username=username, password=password)
    return ssh

def upload_folder_to_remote(ssh, local_folder, remote_folder):
    """Upload a local folder to a remote server using SCP."""
    with SCPClient(ssh.get_transport()) as scp:
        # Iterate over files in the local folder
        for root, _, files in os.walk(local_folder):
            remote_path = os.path.join(remote_folder, os.path.relpath(root, local_folder)).replace('\\', '/')
            
            # Create directories on the remote server
            ssh.exec_command(f'mkdir -p {remote_path}')
            
            for file in files:
                local_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_path, file).replace('\\', '/')
                
                # Upload file
                scp.put(local_path, remote_file_path)
                print(f'Uploaded {local_path} to {remote_file_path}')

if __name__ == '__main__':
    # onnection Parameters
    hostname = '192.168.1.36' # IP or Host Name
    port = 22  # SSH Port
    username = 'nvidia'
    password = 'nvidia'

    # Local and remote folder paths
    local_folder = 'Student_Logs'
    remote_folder = 'student_logs'  # The destination folder on the remote server

    # Create SSH connection and upload folder
    ssh_client = create_ssh_client(hostname, port, username, password)
    try:
        upload_folder_to_remote(ssh_client, local_folder, remote_folder)
    finally:
        ssh_client.close()


# git remote add origin https://github.com/poptarts-tasty-af/Student-Cosmo-Logs.git
