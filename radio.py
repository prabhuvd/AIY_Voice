"""
Created on May 10, 2017

Radio Class allows user to configure NXP RF receiver.
 
@author: pdesai
"""
# This is to support python 2 style of print functions.
from __future__ import print_function
import serial
import time
import sys
import irec_config


class Radio:
    """ receiver port """
    __portInstance = 0
    ''' TPM sensor ID's and the corresponding temperature and pressure value.
    '   read_tpm_sensors() method reads the sensors , decodes the pressure and temperature 
    '   and stores into the dictionary.
    '''
    __rx_data=""
    __sensor_ids = {"0d224bff": [00, 00],
                    "0d224bf4": [00, 00],
                    "0d2262b9": [00, 00],
                    "0d22622a": [00, 00]}


    '''
    ' ----------------------------------------------------
    ' Configuration is for MY2012 Mazda 5 sport
    ' ----------------------------------------------------
    '    Signal Parameters are:
    '    Baud Rate : 19200 chips/s
    '    Frequency Deviation : 35kHz
    '    Coding Style for run-in and data :  Manchester
    '    Modulation : FSK
    '    Channel Filter : 10000 Hz
    '    Intermediate Frequency : -20kHz
    '    Data Length :  10bytes
    '    Preamble : 0x0001
    '
    '
    '  The hard coded constants are the register values of NCK2983 for the above configuration. 
    '    
    '''
         
    def __init__(self, portnum, baud=115200):                        
        self.new_message = False
        try:
            self.__portInstance = serial.Serial(portnum, baud, timeout=.01)
        except IOError as e:
            print (e)
            print "Terminating program: Check port assignment /Connections to the Hardware !"
            print "contact: prabhu.desai@aptiv.com"
            sys.exit()
            

    def close(self):
        self.__portInstance.close()

    @staticmethod
    def byte_to_hex(bytestr):
        """
        Convert a byte string to it's hex string representation e.g. for output.
        """
        # Uses list comprehension which is a fractionally faster implementation than
        # the alternative, more readable, implementation below
        #
        #    hex = []
        #    for aChar in bytestr:
        #        hex.append( "%02X " % ord( aChar ) )
        #
        #    return ''.join( hex ).strip()
        return ''.join(["%02X " % ord(x) for x in bytestr]).strip()

    @staticmethod
    def hex_to_byte(hexstr):
        """
        Convert a string hex byte values into a byte string. The Hex Byte values may
        or may not be space separated.
        """
        # The list comprehension implementation is fractionally slower in this case
        #
        #    hexstr = ''.join( hexstr.split(" ") )
        #    return ''.join( ["%c" % chr( int ( hexstr[i:i+2],16 ) ) \
        #                                   for i in range(0, len( hexstr ), 2) ] )

        dbytes = []
        hexstr = ''.join(hexstr.split(" "))

        for i in range(0, len(hexstr), 2):
            dbytes.append(chr(int(hexstr[i:i + 2], 16)))

        return ''.join(dbytes)
 
    
    def write_command(self, command):
        # This flag will decided to Turn ON the receiver again.
        # print "send:",command
        if 0 == self.__portInstance.write(self.hex_to_byte(command)):
            print ("Write error : flushing I/O buffers")
            self.__portInstance.flushInput()
            self.__portInstance.flushOutput()
        # This delay is MUST after every command to Radio  
        time.sleep(.01)
        first_byte, rx_byte = self.read_cmd_response()
        
        return first_byte, rx_byte
    
    def read_cmd_response(self):
        # Reads one byte response which indicates the length of remaining  following bytes
        read_1_byte = self.byte_to_hex(self.__portInstance.read(1))
        read_byte_array = read_1_byte.split()

        # Check if there was at least one byte received.
        if len(read_byte_array) >= 1:
            # The first byte from the receiver indicates the length
            # of the following message
            rsp_length = int(read_byte_array[0], 16)
            rx_byte = self.byte_to_hex(self.__portInstance.read(rsp_length))
            return rsp_length, rx_byte
        else:
            return 0, 0

    def write_list_commands(self, cmdlist):
        for commands in range(len(cmdlist)):            
            self.write_command(cmdlist[commands])

    def configure_device(self,irec_cfg): 
        self.write_list_commands(irec_cfg)
           
    def check_rx_data(self):
        # This is a very crucual part of the interface with RF receiver.
        # Do not modify this without being fully aware of the protocol.
        first_byte, received_data = self.write_command(irec_config.Receiver_READ_DATA_cmd[0])

        if first_byte > 6:
            print first_byte , received_data
            rx_data = received_data.split()
            if(int(rx_data[1],16)==0):
                if( int(rx_data[4],16) & 0x10 )==16:
                    # Ignore the return parameters , this is required to turn on 
                    # the receiver after successful reception.
                    self.write_command(irec_config.Receiver_ON_cmd[0])
                    self.__rx_data = rx_data[6:]
                    self.new_message = True

    def transmit_data(self):        
        self.write_list_commands(irec_config.NCK2984_TX_SEND)
        
#         cmd_str = "06 20 20"
#         hex_interval= "%04X" % interval
#         hex_num_frames  = "%04X" % num_frames
#         print hex_interval , hex_num_frames
#         
#         cmd_str = cmd_str + " " + hex_num_frames[2:4] + " " +hex_num_frames[0:2] + " " +hex_interval[2:4] + " " +hex_interval[0:2] 
#         #print cmd_str      
#         self.write_command(cmd_str)
        
    def read_rx_data_buffer(self):      
        msg_status = self.new_message  
        self.new_message = False
        return msg_status, self.__rx_data


__version = '0.1'

# RADIO_PORT = 'COM8'
# radio_inst = Radio(RADIO_PORT)
# radio_inst.transmit_data(10,20)