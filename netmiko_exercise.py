#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# Prompt user for password to lab devices...
lab_password = getpass("Enter password for lab devices: ")

# Lab device information:
nxos1 = {
	'device_type': 'cisco_nxos',
	'host': 'nxos1.lasthop.io',
	'username': 'pyclass',
	'password': lab_password
	}

nxos2 = {
	'device_type': 'cisco_nxos',
	'host': 'nxos2.lasthop.io',
	'username': 'pyclass',
	'password': lab_password
	}

devices = [ nxos1, nxos2 ]

# Log into each device and display the prompt for each:
for switch in devices:
	myLabHandler = ConnectHandler(**switch)
	output = myLabHandler.find_prompt()
	print(output)

# On the last device, save off the 'show version' output to a log file:
show_version_output = myLabHandler.send_command("show version")

show_version_logfile = open('netmiko_exercise_output.log', 'w')
show_version_logfile.write(show_version_output)
show_version_logfile.close()

