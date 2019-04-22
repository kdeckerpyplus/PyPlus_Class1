#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

lab_password = getpass("Enter password for lab devices: ")

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

for switch in devices:
	myLabHandler = ConnectHandler(**switch)
	output = myLabHandler.find_prompt()
	print(output)

show_version_output = myLabHandler.send_command("show version")

show_version_logfile = open('netmiko_exercise_output.log', 'w')
show_version_logfile.write(show_version_output)
show_version_logfile.close()

