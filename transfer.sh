#!/usr/bin/expect -f
spawn ftp
send "open 10.255.0.20\n";
send "NOC\n";
send "123\n";
send "put 192.168.9.198.rsc\n"
send "\n";
send "\r";  
expect eof

