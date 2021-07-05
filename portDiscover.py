import socket
import sys
import optparse
import threading

class portScanner:

	def __init__(self, reqPortScan, target):
		self.reqPortScan = reqPortScan
		self.target = target
		self.open_ports = []
		self.threads = []
		for i in range(1, self.reqPortScan):
			threading.Thread(target=scan, args=(i, self)).start()

	def displayResults(self):
		print('''After scanning all {requested_ports} requested ports, {open_port_count} port(s) have been found to be open on {target_machine}'''.format(
		requested_ports=self.reqPortScan, 
		open_port_count=len(self.open_ports), 
		target_machine=self.target))
		print(self.open_ports)

def scan(port_num, scanner):
		portConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			portConnection.connect((scanner.target, port_num))
			print('[+] Port: {port} is open!'.format(port=port_num))
			scanner.open_ports.append(port_num)
		except socket.error:
			print('[-] Port: {port} is not open!'.format(port=port_num))

def main():
	command = optparse.OptionParser()
	command.add_option('-t', action='store', dest='target', type='string',help='identify target machine that you would like to port scan')
	command.add_option('-c', action='store', dest='port_count', type='int', help='identify how many of the ports you would like scanned starting from 1')
	options, args = command.parse_args()
	reqPortScan = options.port_count
	target = options.target
	scanner = portScanner(reqPortScan, target)

if __name__ == '__main__':
	main()
