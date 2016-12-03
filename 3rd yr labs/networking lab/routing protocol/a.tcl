set ns [new Simulator]
$ns color 1 Blue
$ns color 2 Red

set tracefile1 [open out.tr w]
$ns trace-all $tracefile1

set namfile [open out.nam w]
$ns namtrace-all $namfile

proc finish { } {
	global ns tracefile1 namfile
	$ns flush-trace
	close $tracefile1
	close $namfile
	exec nam out.nam &
	exit 0


}
#creating 6 nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]


$ns duplex-link $n0 $n1 3Mb 5ms DropTail
$ns duplex-link $n1 $n2 3Mb 5ms DropTail
$ns duplex-link $n2 $n3 3Mb 5ms DropTail
$ns duplex-link $n3 $n4 3Mb 5ms DropTail
$ns duplex-link $n4 $n5 3Mb 5ms DropTail
$ns duplex-link $n5 $n6 3Mb 5ms DropTail
$ns duplex-link $n6 $n0 3Mb 5ms DropTail


$ns cost $n0 $n1 10 
$ns cost $n1 $n0 5 

$ns cost $n1 $n2 10 
$ns cost $n2 $n1 5 

$ns cost $n2 $n3 10 
$ns cost $n3 $n2 5 

$ns cost $n3 $n4 10 
$ns cost $n4 $n3 5 

$ns cost $n4 $n5 10 
$ns cost $n5 $n4 5 

$ns cost $n5 $n6 10 
$ns cost $n6 $n5 5 

$ns cost $n6 $n0 10 
$ns cost $n0 $n6 5 

set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp $sink
$tcp set fid_ 1
$tcp set packetSize_ 1000

set ftp [new Application/FTP]
$ftp attach-agent $tcp

set udp [new Agent/UDP]
$ns attach-agent $n0 $udp
set null [new Agent/Null]
$ns attach-agent $n4 $null
$ns connect $udp $null
$udp set fid_ 2

$udp set packetSize_ 1000
$udp set rate_ 1Mb



set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp


 # $ns rtproto Static
 # #Enable static route strategy for the Simulation
 # $ns rtproto Session
 # #Enable session routing for this simulation
 # $ns rtproto DV $n1 $n2 $n3 
 # #Run DV agents on nodes $n1, $n2, and $n3
$ns rtproto LS  
#Run link state routing on specified nodes


$ns rtmodel-at 1.0 down $n4 $n5
$ns rtmodel-at 3.0 up $n4 $n5


$ns rtmodel-at 1.0 down $n6
$ns rtmodel-at 3.0 up $n6


$ns at 0.5 "$cbr start"
$ns at 0.5 "$ftp start"
$ns at 4.9 "$ftp stop"
$ns at 4.9 "$cbr stop"
$ns at 5.0 "finish"

$ns run













