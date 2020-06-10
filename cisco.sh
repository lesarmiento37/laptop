#!/usr/bin/expect -f

spawn telnet 192.168.5.252;
expect "Username:";
send "NOC\n";
expect "Password:";
send "S3W*N0C2019*\n";
send "enable\n";
expect "Password:";
send "S32019G3st10n*\n";
send "configure terminal\n";
send "ip ftp username NOC\n";
send "ip ftp password 123\n";
send "exit\n";
send "copy running-config ftp:\n";
expect "Address or name of remote host []?";
send "10.255.0.20\n";
send "192.168.5.252.rsc\n";
send "end\n";
send "exit\n";
expect eof

spawn telnet 192.168.1.254;
expect "Username:";
send "NOC\n";
expect "Password:";
send "S3W*N0C2019*\n";
send "enable\n";
expect "Password:";
send "S32019G3st10n*\n";
send "configure terminal\n";
send "ip ftp username NOC\n";
send "ip ftp password 123\n";
send "exit\n";
send "copy running-config ftp:\n";
expect "Address or name of remote host []?";
send "10.255.0.20\n";
send "\n";
send "\r";  
expect eof

spawn telnet 192.168.5.253;
expect "Username:";
send "NOC\n";
expect "Password:";
send "S3W*N0C2019*\n";
send "enable\n";
expect "Password:";
send "S32019G3st10n*\n";
send "configure terminal\n";
send "ip ftp username NOC\n";
send "ip ftp password 123\n";
send "exit\n";
send "copy running-config ftp:\n";
expect "Address or name of remote host []?";
send "10.255.0.20\n";
send "\n";
send "\r";  
expect eof

spawn telnet 192.168.16.250;
expect "Username:";
send "NOC\n";
expect "Password:";
send "S3W*N0C2019*\n";
send "enable\n";
expect "Password:";
send "S32019G3st10n*\n";
send "configure terminal\n";
send "ip ftp username NOC\n";
send "ip ftp password 123\n";
send "exit\n";
send "copy running-config ftp:\n";
expect "Address or name of remote host []?";
send "10.255.0.20\n";
send "\n";
send "\r";  
expect eof


spawn telnet 192.168.21.254;
expect "Username:";
send "NOC\n";
expect "Password:";
send "S3W*N0C2019*\n";
send "enable\n";
expect "Password:";
send "S32019G3st10n*\n";
send "configure terminal\n";
send "ip ftp username NOC\n";
send "ip ftp password 123\n";
send "exit\n";
send "copy running-config ftp:\n";
expect "Address or name of remote host []?";
send "10.255.0.20\n";
send "\n";
send "\r";  
expect eof

spawn telnet 192.168.35.254;
expect "Username:";
send "NOC\n";
expect "Password:";
send "S3W*N0C2019*\n";
send "enable\n";
expect "Password:";
send "S32019G3st10n*\n";
send "configure terminal\n";
send "ip ftp username NOC\n";
send "ip ftp password 123\n";
send "exit\n";
send "copy running-config ftp:\n";
expect "Address or name of remote host []?";
send "10.255.0.20\n";
send "\n";
send "\r";  
expect eof

