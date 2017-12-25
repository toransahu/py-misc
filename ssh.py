#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:42:46 2017

@author: toran
"""

import paramiko

def ssh(server,port,username,password):
    try:
        client = paramiko.Transport((server, port))
        client.connect(username=username, password=password)
        return client
    except SSHException as e:
        print("Request rejected by",server)


def ssh_command(client,command):
    """
    Send command.
    
    The channel will get closed after execution of the command.
    Works like per shell one command.
    """
    result = []
    err_msg = []
    nbytes = 4096
    stdout_data = []
    stderr_data = []
    try:
        session = client.open_channel(kind='session')
        session.exec_command(command)
        while True:
            if session.recv_ready():
                stdout_data.append(session.recv(nbytes))
            if session.recv_stderr_ready():
                stderr_data.append(session.recv_stderr(nbytes))
            if session.exit_status_ready():
                break
        
        # check exit status
        if session.recv_exit_status() != 0:
            err_msg = ''.join(i.decode('utf-8') for i in stderr_data)
        elif session.recv_exit_status() == 0:
            result = ''.join(i.decode('utf-8') for i in stdout_data)
        return result, err_msg
    except Exception as e:
        return print("Oops! Something wrong happened while ssh", e)
    finally:
        session.close()



if __name__ == '__main__':
    server = '192.168.1.9'
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
        client = ssh(server,port,username,password)   
        for command in commands:
            res, err = ssh_command(client, command)
            results.append(res)
            errors.append(err)
            
        print("Uptime:",results[0], end='')
        print("Memory Usage:",results[1], end='')
        print("CPU Usage:",results[2], end='')
    except Exception as e:
        print("Something wrong happened while fetching data from ssh client", e)
    finally:
        client.close()