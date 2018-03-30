'''
Created on Mar 27, 2018

@author: gjpqbv
'''
# This is to support python 2 style of print functions.
from __future__ import print_function
import re
import time
import irec_config

from radio import Radio
from AI import AICommands
from time import gmtime, strftime

RADIO_PORT = 'COM8'
radio_dev = Radio(RADIO_PORT)
 

def receive_data():
    radio_dev.check_rx_data()
    
    if(radio_dev.read_rx_data_buffer()):
        # Until the rx_data_buffer is acknowledged , it will not clear
        # the new message flag.
        print radio_dev.read_rx_data_buffer()
        
def transmit_data(tx_interval,num_frames):
    for x in range(num_frames):
        print strftime("%H:%M:%S", gmtime()) , "sending Frame #" , x
        radio_dev.transmit_data()
        time.sleep(tx_interval)
 

print "Radio Configuration completed..."
    
# while (True):
#     #transmit_data(.01,10)
#     receive_data()

ai_device = AICommands()

cmd_string =  ai_device.get_voice_command(1)
command, protocol, tx_num , tx_rate ,unit = ai_device.decipher_cmd(cmd_string)
 
print command, protocol, tx_num , tx_rate ,unit 

if(command != "INVALID" and protocol !="INVALID"):  
    if(command == "TRANSMIT"):
        #radio_dev.configure_device(irec_config.NCK2984_FCA_RKE_RECEIVE_config)
        print irec_config.TRANSMIT_DICT[protocol]
    elif(command == "RECEIVE"):
        print irec_config.RECEIVE_DICT[protocol]
else:
    ai_device.unknown_command()    

