#!/usr/bin/perl

use DBI;

my $dbh1 = DBI->connect('dbi:Pg:dbname=postgres;host=192.168.6.2;port=1234','postgres','bolson',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $dbh2 = DBI->connect('dbi:Pg:dbname=postgres;host=192.168.6.2;port=4321','postgres','bolson',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

print "Servidor de escrituras: ".$dbh1->selectrow_array("SELECT inet_server_addr();"),"\n";
print "Servidor de lecturas: ".$dbh2->selectrow_array("SELECT inet_server_addr();"),"\n";