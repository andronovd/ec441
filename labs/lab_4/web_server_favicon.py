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
    return lastmod;
  

#--main--#
serverSocket = socket(AF_INET, SOCK_STREAM );
#prepare a server socket
host = "";
port = 47221;
backlog = 5;
size = 1024;

serverSocket.bind( (host, port) );
serverSocket.listen( backlog );

while True:
    #Establish a connection
    print("Ready to server..." );
    connectionSocket, addr = serverSocket.accept();
    #print( "Connected" );
    try:
        message = connectionSocket.recv( size );
        #print( "message: ", message.split() );
        filename = message.split()[1];
        filename = filename.replace( "/", "" );
        
        #Read file
        #first get the extension
        #if its an ico file, read it in binary mode
        #else read normally
        ext = filename.split(".")[1];
        if( ext == "ico" ):
        	f = open( filename, 'rb' );
        else:
        	f = open( filename );
        outputdata = f.read();
        #print( outputdata );
        
        #Send HTTP status line into socket
        connectionSocket.send( "HTTP/1.1 200 OK\n".encode() );
        
        #Send last-modified HTTP header line into socket
        date = "Last-Modified: " + getLastMod( filename[1:] ) + "\n"; #get the last modified time of the file
        connectionSocket.send( date.encode() );
        
        #Send the content of the requested file to the client
        
        #if its an ico file, there is no need to encode the information
        #else, encode as per usual
        if( ext == "ico" ):
		      for i in range( 0, len(outputdata) ):
				        connectionSocket.send( outputdata[i] );
        else:        
		      for i in range( 0, len(outputdata) ):
		          connectionSocket.send( outputdata[i].encode() );
				
        connectionSocket.send( "\n\r\n\r\n".encode() ); #end message
        
        #close file and client socket
        f.close();
        connectionSocket.close();
    except IOError:
			print( "there was an error" );
			#Send reponse message for file not found
			message = "HTTP/1.1 404 File Not Found\n"; #send error message, file not found
			connectionSocket.send( message.encode() );
			connectionSocket.send( "\r\n\r\n".encode() );

			#Close client socket
			connectionSocket.close();
serverSocket.close();

