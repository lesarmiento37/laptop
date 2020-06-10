#!/usr/bin/expect -f
spawn ssh ubnt@192.168.19.145;
expect "ubnt@192.168.19.145's password:";
send "N3tG3st10n19\n";
expect "XW.v5.6.11#";
send "cd ..\n";
expect "XW.v5.6.11#";
send "scp default.cfg leonardo@10.255.0.70:/home/leonardo\n";
expect "leonardo@10.255.0.70's password:";
send "leonardo\n";
send "\n";
expect "XW.v5.6.11#";
send "exit\n";
spawn mv default.cfg 192.168.19.145.rsc
spawn ftp
send "open 10.255.0.20\n";
expect "Name (10.255.0.20:leonardo):";
send "NOC\n";
expect "Password:";
send "123\n";
expect "ftp>";
send "put 192.168.19.145.rsc\n";
send "bye\n";
expect eof
spawn mv 192.168.19.145.rsc /home/dionis/
