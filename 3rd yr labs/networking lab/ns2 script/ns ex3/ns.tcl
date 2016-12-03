#Create a simulator object
set ns [new Simulator]
#Open the output trace file


set f0 [open out0.tr w]
$ns trace-all $f0

#Open the NAM trace file
set nf [open out.nam w]
$ns namtrace-all $nf

#Create 2 nodes
set n0 [$ns node]
set n1 [$ns node]
#Connect the nodes using duplex link
$ns duplex-link $n0 $n1 1Mb 100ms DropTail
#Define a 'finish' procedure
proc finish {} {
         global ns nf
        $ns flush-trace
        #Close the NAM trace file
        close $nf
        #Execute NAM on the trace file
        exec nam out.nam &

        #Call xgraph to display the results
        exec xgraph out0.tr -geometry 800x400 &
        exit 0
}
#Define a procedure which periodically records the bandwidth received by the
#the traffic sink0 and writes it to the file f0.
proc record {} {
        global sink0 nf
    #Get an instance of the simulator
    set ns [Simulator instance]
    #Set the time after which the procedure should be called again
        set time 0.5
    #How many bytes have been received by the traffic sinks?
        set bw0 [$sink0 set bytes_]
    #Get the current time
        set now [$ns now]
    #Calculate the bandwidth (in MBit/s) and write it to the files
        puts $nf "$now [expr $bw0/$time*8/1000000]"
    #Reset the bytes_ values on the traffic sinks
        $sink0 set bytes_ 0
    #Re-schedule the procedure
        $ns at [expr $now+$time] "record"
}
#Create three traffic sinks and attach them to the node n4
set sink0 [new Agent/LossMonitor]
#Start logging the received bandwidth
$ns at 0.0 "record"
$ns at 60.0 "finish"
#Run the simulation
$ns run