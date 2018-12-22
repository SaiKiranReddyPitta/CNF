import socket 

def Main():
	host = '10.10.9.158'
	port = 9999
	soc = socket.socket()
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.connect((host, port))
	file = open('data.csv', 'rb')
	printp =  file.read(409600)


	while true:
		print("roll number found")
		message = input("Secret Question")
		print(printp)
		soc.send(message.encode())
		data_information = soc.received().decode()
		print("Received Secret Question" + str(data_information))
	file.close()
	soc.close()

if __name__ == '__main__':
    Main()

