# IntroTel Set of Tools:

Here you will find a set of tools mentioned during the course, also this tools will be usefull for the final exercise.

# Knowledge and concepts:

For the last exercise, you need to apply all the concepts and tools used during the course, here you will find a brief summary of the conceptos and commands used during the course.

## Python Installation Steps
To install Python on your system, follow these steps:

- **Check if Python is already installed:** Open a terminal or command prompt and enter the command `python --version` or `python3 --version`. If Python is already installed, it will display the version number. If not, proceed to the next step.

- **Download Python:** Go to the official Python website at python.org and click on the "Downloads" tab. Choose the appropriate version for your operating system (Windows, macOS, or Linux) and download the installer. If you are using MacOS consider using brew as package manager, and (install python using brew)[https://www.scaler.com/topics/python/how-to-install-python-on-macos/]

- **Run the Installer:** After the download is complete, run the installer executable. On Windows, make sure to check the box that says "Add Python to PATH" during the installation process. This will allow you to use Python from any directory in the command prompt or terminal.

- **Verify the Installation:** Open a new terminal or command prompt and enter the command `python --version` or `python3 --version` again. It should now display the version number of the installed Python.

## SSH (Secure Shell)
SSH stands for Secure Shell, and it is a network protocol that allows secure remote access to a computer or server over an unsecured network. It provides a secure encrypted connection between the client and the server, ensuring that the data transmitted between them cannot be intercepted or tampered with.

SSH is commonly used by system administrators, developers, and users who need to remotely manage or access computers and servers. It provides a secure alternative to traditional remote login methods such as telnet or FTP.

### How to connect to SSH

By default SSH uses the 22 port, the sintax to use SSH using a user, ip and password is, after pressing the enter key, we will be asked for a password.
```
ssh <user>@<ip-address>
```

Example

```
ssh root@85.123.123.123
```

## Basic Linux SSH Commands
Once you have SSH access to a remote server, you can use the following basic Linux SSH commands:

- ls: Lists files and directories in the current directory.
```
ls
```

- cd: Changes the current directory.
```
cd directory_name
```

- pwd: Prints the current working directory.
```
pwd
```

- cat: Displays the contents of a file.
```
cat file_name
```

- touch: Creates a new file.
```
touch file_name
```

- mkdir: Creates a new directory.
```
mkdir directory_name
```

- rm: Removes a file.
```
rm file_name
```

- rmdir: Removes an empty directory.
```
rmdir directory_name
```

- cp: Copies a file or directory.
```
cp source_file destination_file
```

- mv: Moves or renames a file or directory.
```
mv source_file destination_file
```

These are just a few examples of basic SSH commands. There are many more commands available for various tasks and operations in Linux.

## UFW (Uncomplicated Firewall)
UFW is a front-end for iptables, which is the standard firewall configuration tool for Linux. UFW aims to simplify the process of managing firewall rules by providing a user-friendly interface.

Here are the basic steps to allow and deny ports using UFW:

- Check UFW Status: Open a terminal and enter the command:
```
sudo ufw status
```

This will display the current status of UFW and show if it is active or inactive.

- Enable UFW: If UFW is not enabled, you can enable it by running the command:
```
sudo ufw enable
```
This will activate the firewall and start enforcing the configured rules.

- Allow Ports: To allow incoming connections on a specific port, you can use the following command:
```
sudo ufw allow <port>/<optional_protocol>
```

Replace <port> with the port number you want to allow, and <optional_protocol> with the protocol (e.g., tcp, udp) if you want to specify it. For example, to allow incoming TCP connections on port 80, you would run:
Example:
```
sudo ufw allow 80/tcp
```

- Block Ports: To block incoming connections on a specific port, you can use the following command:
```
sudo ufw deny <port>/<optional_protocol>
```
Replace <port> with the port number you want to block, and <optional_protocol> with the protocol if you want to specify it. For example, to block incoming TCP connections on port 22 (SSH), you would run:
```
sudo ufw deny 22/tcp
```

- Delete Rules: If you want to remove a rule that allows or denies a specific port, you can use the delete command with the rule number. First, list the rules along with their numbers using the command:
```
sudo ufw status numbered
```
Identify the rule number you want to delete, and then use the following command to remove it:
```
sudo ufw delete <rule_number>
```

- Reload UFW: After making changes to the firewall rules, you need to reload UFW to apply the modifications. Run the comman
```
sudo ufw reload
```
Remember to be cautious when modifying firewall rules, as incorrect configurations can block legitimate traffic or leave your system vulnerable. Always double-check your changes and test them to ensure the desired functionality.

# Scanning ports:

To run a port scanning on a IP objectivo, you could use the python script in the file `scanning_ports.py`
Remember to run the python script step by step to get a proper result.

# Sending message to a Open Socket using Python

To send a message to a socket waiting for connections and messages, you could use the `message2server-socket.py`. Remember to update the host and port with the valid destionation to connect.

# Steganography: Hiding info in messages

To encrypt and decrypt sensitive information in images, you could use the `steganography.py` script, to run this script you need the Pillow library, to install it you need to run the below command:
```
pip install Pillow
```
Then you will need to run the script
```
python steganography.py
```

Remember to update the `image_path` and secret variables