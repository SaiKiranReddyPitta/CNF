import socket
def Main():

	host = '10.10.9.158'
	port = 9999

	soc = socket.socket()
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.connect((host, port))

	soc.listen(1)
	connection, address =soc.accept();
	print("got connected")

	while true:
		data_information = soc.received().decode()
		connection.send(data_information.encode())
		connection.close()
if __name__ == '__main__':
    Main()



