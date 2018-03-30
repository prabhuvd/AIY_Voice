'''
Created on Mar 28, 2018

@author: gjpqbv
'''
# This is to support python 2 style of print functions.
from __future__ import print_function
from numpy.random import random
class AICommands:
    _list_of_commands=["Send 100 RKE frames every 100 ms",
                       "Transmit 100 TPM frames every 1 seconds",
                       "Send 100 RKE frames at 100 millisecond rate",
                       "Send 100 RKE frames every 200 ms",
                       "Send 100 PEPS frames every 1 seconds",
                       "Transmit 100 PEPS frames every 100 ms",
                       "Count the number of RKE received frames",
                       "Count the number of TPMS received frames",
                       "Count the number of PEPS received frames",
                       "How many RKE frames did you receive",
                       "How many RKE frames did you receive",
                       "send only one",
                       "transmit frames",
                       "transmit frames",
                       ]
    _unknown_cmd_messages = ["I do not understand the command , try again ! ",
                             "Hmm... i'm trying to get better at this task , say it differently ",]
    
    def unknown_command(self):
        print self._unknown_cmd_messages[random.randint(0,len(self._unknown_cmd_messages))]
        
    def get_voice_command(self,index):
        if (index<len(self._list_of_commands)):
            return self._list_of_commands[index]
        else :
            return "NO command"
     
    def decipher_cmd(self,cmd_string):
        rate_unit = "None" 
        number_of_frames = 0
        rate_of_frames=  0          
        execute_cmd = "None"
        frame_type  = "None" 
        
        # Keywords to look for in the voice command. 
        receive_cmd = ["received","get","received"]
        transmit_cmd = ["send" , "transmit"]
        
        rke_cmd = ["rke","remote keyless entry","remote key"]
        tpm_cmd = ["tpm","tpms","tire pressure","tire pressure sensor"]
        peps_cmd = ["peps","passive entry"]
        
        tx_units_ms =["ms","millisecond","milliseconds"]
        tx_units_second =["sec","second","seconds"]
        
        cnvrt_cmd_str = cmd_string.lower()
        

        #Decode whether it is a transmit or receive operation.    

        if any(x in cnvrt_cmd_str for x in receive_cmd):     
            execute_cmd = "RECEIVE"
        # The unit of time and the number of frames matter only for 
        # Transmit operation.
        elif any(x in cnvrt_cmd_str for x in transmit_cmd):
            execute_cmd = "TRANSMIT"
            
            #Decode the unit of Transmit time.                   
            if any(x in cnvrt_cmd_str for x in tx_units_second):
                rate_unit ="second"    
            
            if any(x in cnvrt_cmd_str for x in tx_units_ms):
                rate_unit ="ms"
                            
            #Decode the numbers in the voice cmd and assign it to number of frames & rate of transmission.                      
            numbers_in_str = [int(s) for s in cnvrt_cmd_str.split() if s.isdigit()]
 
            if(2 == len(numbers_in_str)):                
                number_of_frames = numbers_in_str[0]
                rate_of_frames = numbers_in_str[1]
            elif(1 == len(numbers_in_str)):
                number_of_frames = numbers_in_str[0]                
            else :
                number_of_frames= rate_of_frames=0
        else:
            execute_cmd = "INVALID"

           
        if any(x in cnvrt_cmd_str for x in rke_cmd):
            frame_type = "RKE" 
        elif any(x in cnvrt_cmd_str for x in tpm_cmd):    
            frame_type ="TPM"
        elif any(x in cnvrt_cmd_str for x in peps_cmd):  
            frame_type ="PEPS"
        else: 
            frame_type = "INVALID"

           
        return execute_cmd, frame_type,number_of_frames,rate_of_frames,rate_unit


# ai_dev = AICommands()
#  
# for x in range (10):
#     ai_device = ai_dev.get_voice_command(x)
#     print ai_device, "----->",ai_dev.decipher_cmd(ai_device)
    