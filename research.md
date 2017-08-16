**MEASURING LATENCY WITH THE PING UTILITY**
===========================================
*The ping utility is an easy way to measure site latency, How long it takes one packet to get from X to Y.

*Latency information is reported directly by the ping itself

*For each ping recieved, a RTT(Round Trip Time) is reported. It is measured by the local clock in the pinging machine, from when the request left to when the reply arrived.

*The packets sent is called the ICMP-- Internet Control Message Protocol

*The Internet Control Message Protocol (ICMP) is a supporting protocol in the Internet protocol suite. It is used by network devices, including routers, to send error messages and operational information indicating, for example, that a requested service is not available or that a host or router could not be reached.

				RTT-- TIME DIFFERENCE BETWEEN REQUEST AND REPLY
REQUEST----->>>>>>---------------------->>>>>----------------------------------->>>>> REPLY
				USED TO MEASURE LATENCY OF THE SERVER(THE REPLIER) Sends ICMP



*Ping times correlate very roughly with distance between source and destination machines, a machine can ping itself very fast, but pinging another machine within the network can be very fast but not as fast as pinging itself.

*Pinging machines outside the local network will take a longer time, so therefore Ping time increases with geographic distances

*so therefore we can say the ping within a LAN is faster than MAN, and MAN faster than WAN----
									LAN > MAN > WAN
				---------------speed reduces with distance---------> 

* So whenever you run the ping utility, it gives the Round Trip time in this format
Minimum, Average, Maximum----------- the average is what we need to determine the Latency of the server


* Under Ideal condition inside ping time inside a lan should never exceed 1 ms.

* Pinging over a WAN, there are two main factor: Speed of light and latency at each hop
* Satelite links have very long ping times, over 500 ms and upto 1200 ms typically

*ICMP messages are typically used for diagnostic or control purposes or generated in response to errors in IP operations. ICMP errors are directed to the source IP address of the originating packet.