#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

class red1 (Topo):
# Creando la primera RED y agregando sus hosts a cada sw con un for.
 def build (self, n=4):
  sw1 = self.addSwitch('s1')
  sw2 = self.addSwitch('s2')
  sw3 = self.addSwitch('s3')
  sw4 = self.addSwitch('s4')
  sw5 = self.addSwitch('s5')
  for h in range (n) :
   host1 = self.addHost('h%s' %(h+1))
   self.addLink(host1,sw1)
   host2 = self.addHost('h%s' %(h+5))
   self.addLink(host2,sw2)
   host3 = self.addHost('h%s' %(h+9))
   self.addLink(host3,sw3)
   host4 = self.addHost('h%s' %(h+13))
   self.addLink(host4,sw4)
   host5 = self.addHost('h%s' %(h+17))
   self.addLink(host5,sw5)
  self.addLink(sw1,sw2)
  self.addLink(sw2,sw3)
  self.addLink(sw3,sw4)
  self.addLink(sw4,sw5)
   
class  red2 (Topo) :
 def build (self, n=4):
  sw6 = self.addSwitch('s6')
  sw7 = self.addSwitch('s7')
  sw8 = self.addSwitch('s8')
  sw9 = self.addSwitch('s9')
  sw10 = self.addSwitch('s10')
  for h in range (n):
   host6 = self.addHost('h%s' %(h+21))
   self.addLink(host6,sw6)
   host7 = self.addHost('h%s' %(h+25))
   self.addLink(host7,sw7)
   host8 = self.addHost('h%s' %(h+29))
   self.addLink(host8,sw8)
   host9 = self.addHost('h%s' %(h+33))
   self.addLink(host9,sw9)
   host10 =self.addHost('h%s' %(h+37))
   self.addLink(host10,sw10)
  self.addLink(sw6,sw7)
  self.addLink(sw7,sw8)
  self.addLink(sw8,sw9)
  self.addLink(sw9,sw10)
   
class red3 (Topo):
 def build (self, n=4):
  sw11 = self.addSwitch('s11')
  sw12 = self.addSwitch('s12')
  sw13 = self.addSwitch('s13')
  sw14 = self.addSwitch('s14')
  sw15 = self.addSwitch('s15')
  for h in range (n) :
   host11 = self.addHost('h%s' %(h+41))
   self.addLink(host11,sw11)
   host12 = self.addHost('h%s' %(h+45))
   self.addLink(host12,sw12)
   host13 = self.addHost ('h%s' %(h+49))
   self.addLink(host13,sw13)
   host14 = self.addHost ('h%s' %(h+53))
   self.addLink(host14,sw14)
   host15 = self.addHost ('h%s' %(h+57))
   self.addLink(host15,sw15)
  self.addLink(sw11,sw12)
  self.addLink(sw12,sw13)
  self.addLink(sw13,sw14)
  self.addLink(sw14,sw15)
#Funcion Main la cual llama a la clases creadas y crea las 3 redes con sus respectivos host y switches
def main() :
 topo1  = red1(n=4)
 topo2 = red2(n=4)
 topo3 = red3(n=4)
 net1= Mininet(topo1)
 net2 = Mininet(topo2)
 net3 = Mininet(topo3)
 net1.start()
 net2.start()
 net2.start()
 print("******* ***** *******")
 dumpNodeConnections(net1.hosts)
 dumpNodeConnections(net2.hosts)
 dumpNodeConnections(net3.hosts)
 CLI( net1 )
 CLI( net2 )
 CLI( net3 )
 print("--- Stop Network ---")
 net1.stop( )
 net2.stop( )
 net3.stop()
 
if __name__ == '__main__' :
   setLogLevel('info')
   main()
