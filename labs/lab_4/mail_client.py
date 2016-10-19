from socket import *;
import sys;

#message to be sent

msg = "\r\n Subject: Good Luck\n Good luck on your exam!".encode();
endmsg = "\r\n.\r\n".encode();

#Choose a BU Mail server and call it mailserver
mailserver = "relay.bu.edu";

#Create a socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket( AF_INET, SOCK_STREAM );
port = 25;
backlog = 5;
size = 1024;

clientSocket.bind( (mailserver, port) );
recv = clientSocket.recv( 1024 ).decode();
print( recv );
if( recv[:3] != '220' ):
    print( '220 reply not received from server.' );
    sys.exit(1);

#Send HELO command and print server response.
heloCommand = 'HELO relay.bu.edu \r\n.';
clientSocket.send( heloCommand );
recv1 = clientSocket.recv( size ).decode();
print( recv1 );
if( recv1[:3] != '250' ):
    print( "250 replay not received from server." );
    sys.exit( 1 );

#Send MAIL FROM command and print server response.
#Only use your own e-mail address!
mfCommand = 'MAIL FROM: <andronov@bu.edu> \r\n.';
clientSocket.send( mfCommand );
recv2 = clientSocket.recv( size ).decode();
print( recv2 );

#Send RCPT TO command and the print the server response.
rcptCommand = 'RCPT TO:<ssheng.bu.edu> \r\n.';
clientSocket.send( rcptCommand );
recv3 = clientSocket.recv( size ).decode();
print( recv2 );

#Send DATA command and print server response.
dataCommand = 'Data \r\n.';
clientSocket.send( dataCommand );
recv4 = clientSocket.recv( size ).decode();
print( recv4 );

#Send message data.
clientSocket.send( msg );
recv5 = clientSocket.recv( size ).decode();
print( recv5 );

#Message ends with a single period.
clientSocket.send( endmsg );
recv6 = clientSocket.recv( size ).decode();
print( recv6 );

#Send QUIT command and get server response.
clientSocket.send( "QUIT \r\n." );
recv7 = clientSocket.recv( size ).decode();
print( recv7 );

#Close client socket
socket.close();
