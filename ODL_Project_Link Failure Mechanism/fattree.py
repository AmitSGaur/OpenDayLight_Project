

 from mininet.topo import Topo

class MyTopo( Topo ):
 
     def __init__( self ):
         "Create custom topo."
 
         coreSwitchnumber = 2
         aggregateSwitchnumber = 2
         racknumber = 2
         racksize = 2
 
         # Initialize topology
         Topo.__init__( self )
 
         coreSwitches = []
         aggregateSwitches = []
         torSwitches = []
 
         #core
         for x in range(0, coreSwitchnumber):
             coreSwitches.append(self.addSwitch("cs" + str(x)))
         #aggregate
         for x in range(0, aggregateSwitchnumber):
             aggregateSwitches.append(self.addSwitch("as" + str(x)))
         #tor
         for x in range(0, racknumber):
             torswitch = self.addSwitch("ts" + str(x))
             for y in range(0, racksize):
                 self.addLink(torswitch, self.addHost("h-" + str(x) + "-" + str(y)))
             torSwitches.append(torswitch)
 
         #tor -> aggregate
         for x in range(0, len(aggregateSwitches)):
             for y in range(0, len(torSwitches)):
                 self.addLink(torSwitches[y], aggregateSwitches[x])
         #aggreagate -> core
         for x in range(0, len(coreSwitches)):
             for y in range(0, len(aggregateSwitches)):
                 self.addLink(coreSwitches[x], aggregateSwitches[y])
 
 
         # Add hosts and switches
 
topos = { 'mytopo': ( lambda: MyTopo() ) }
 
