# Task 2: Ansible Test
Manage WebServers through Ansible

## Preparation

- 2 VMs can ping to each other

## Implementation

1. Prepare Webserver

    `IP: 192.168.0.107`

![WebServer](ansible_2.png)

2. Install Ansible on host

    `python3 -m pip install --user ansible`
    `ansible --version`

3. Create inventory file with credentials

![Inventory file](ansible_4.png)

4. Create WEBSERVER INSTALLATION AND TESTING file (playbook file)

![Config file](ansible_5.png)

5. Config the webserver role in main.yml

![Role Config file](ansible_6.png)

6. Create index.html

![index.html](ansible_7.png)

7. Start the Ansible

![Ansible started](ansible_1.png)

## Troubleshooting

- Need to define the ansible_ssh_pass and ansible_ssh_user inside Inventory in order to connect to client

## Verification

![Result](ansible_3.png)

