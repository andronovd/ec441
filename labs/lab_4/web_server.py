# web_server.py

from socket import *
import os
import time

#--helper function--#
def getLastMod( fileName ):
    '''
        This function gets the last modified
        time of the file whose path is given
        by "fileName". The time is returned
       as a string in the format
        "Year-Month-Day Hour:Minute:Second".
    '''
    t = os.stat( "web_server.py" )[ 8 ];
    lastmod = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( t ) );
    print( lastmod );
    return lastmod;
  

#--main--#
serverSocket = socket(AF_INET, SOCK_STREAM );
#prepare a server socket
host = "";
port = 6789;
backlog = 5;
size = 1024;

serverSocket.bind( (host, port) );
serverSocket.listen( backlog );

while True:
    #Establish a connection
    print("Ready to server..." );
    connectionSocket, addr = serverSocket.accept();
    print( "Connected" );
    try:
        message = connectionSocket.recv( size );
        filename = message.split()[1];
        #Read file
        f = open( filename[1:] );
        outputdata = f.read();
        #Send HTTP status line into socket
        serverSocket.send( "HTTP/1.1 200 OK".encode() );
        #Send last-modified HTTP header line into socket
        serverSocket.send( gedLastMod( filename[1:] ).encode() );
        #Send the content of the requested file to the client
        for i in range( 0, len(outputdata) ):
            connectionSocket.send( outputdata[i].encode() );
        connectionSocket.send( "\r\n\r\n".encode() );
        #close file and client socket
        f.close();
        connectionSocket.close();
    except IOError:
        #Send reponse message for file not found
        message = "HTTP/1.1 404 File Not Found";
        connectedSocket.send( message.encode() );
        #Close client socket
        connectedSocket.close();
serverSocket.close();

