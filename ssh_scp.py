#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:47:22 2017

@author: toran
"""
from paramiko import client, Transport, SFTPClient


class SSH:
    client = None
    transport = None
 
    def __init__(self, address, port, username, password):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(address, port, username=username, password=password, look_for_keys=False)
        
        self.transport = Transport((address, 22))
        self.transport.connect(username=username, password=password)
 
 
    def sendCommand(self, command):
        """
        Send command.
        
        The channel will get closed after execution of the command.
        Works like per shell one command.
        """
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata
 
                    return(str(alldata, "utf8"))
        else:
            print("Connection not opened.")
            
    def upload_file(self, localpath, remotepath):
        sftp = SFTPClient.from_transport(self.transport)
        sftp.put(localpath, remotepath)
# =============================================================================
#         from scp import SCPClient
#         scp = SCPClient(self.get_transport())
#         scp.put(source, remote_path=destination)
# =============================================================================
    
    def closeConnection(self):
        """Close COnnection."""
        try:
            if (self.client != None):
                self.client.close()
            else:
                print("Method:",self.closeConnection.__doc__,"No connection")
        except Exception as e:
            print("Method:",self.closeConnection.__doc__,"Something wrong happened while closing connection. Erro:", e)

    

if __name__ == '__main__':
    hostname = '192.168.1.9'
    port = 22
    username = 'toran' 
    password = '\''
    
    results = []
    errors = []
    
    uptime_command = 'uptime -p'
    mem_usage_command = "free -m | awk 'FNR == 2 {usage= $3*100/$2} END {print usage}'"
    cpu_usage_command = "grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"
    
    commands = [uptime_command, mem_usage_command, cpu_usage_command]
    
    try:
        ssh = SSH(hostname,port,username,password)
        for command in commands:
            results.append(ssh.sendCommand(command))
            
        print("Uptime:",results[0], end='')
        print("Memory Usage:",results[1], end='')
        print("CPU Usage:",results[2], end='')
        ssh.upload_file('/mnt/ExternalHDD/test.txt','/mnt/ExternalHDD/E')
    except Exception as e:
        print("Something wrong happened while fetching data from ssh client", e)
    finally:
        ssh.closeConnection()