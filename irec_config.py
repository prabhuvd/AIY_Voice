'''
This configuration is extracted from the command log sent to IREC.
Created on Mar 27, 2018

@author: gjpqbv
'''

''' Turn on the receiver '''
Receiver_ON_cmd = ["03 20 30 01"]
''' Read the sensor '''
Receiver_READ_DATA_cmd = ["03 20 38 00"]
 
NCK2984_TX_SEND = ["06 20 20 00 00 01 00"  # Select the # of frames and interval & RC_CMD_RADIO_TX_ON 
                   "02 20 21"]

NCK2984_FCA_RKE_TRANSMIT_config = [
    "03 20 22 01", #RC_CMD_RADIO_TX_DEFAULTS
    "19 20 24 50 B6 02 00 00 00 00 00 32 00 00 00 00 00 FF 00 FF 17 00 08 00 00 00", #RC_CMD_RADIO_TX_STATIC_NCK2982 
    "03 20 29 00", #RC_CMD_RADIO_TX_DBG_CTRL 
    "08 20 25 08 38 02 28 00 FF", #RC_CMD_RADIO_TX_WUP  
    "08 20 26 08 28 00 28 00 F1", #RC_CMD_RADIO_TX_PREAMBLE  
    "12 20 28 60 A8 00 28 22 11 44 33 66 55 88 77 AA 99 CC BB", #RC_CMD_RADIO_TX_DATA 
    "0B 20 13 10 3E 8C 03 00 EE 03 1F 02", #RC_CMD_RADIO_LO_FREQUENCY
    "06 20 20 00 00 01 00"  # Select the # of frames and interval & RC_CMD_RADIO_TX_ON 
    "02 20 21"
    ]
 
NCK2984_FCA_RKE_RECEIVE_config = [
        "02 20 10", # RC_CMD_RADIO_OFF
        "03 20 32 01", #RC_CMD_RADIO_RX_DEFAULTS 
        "0B 20 13 10 90 6E 03 00 EE 03 1F 02", # RC_CMD_RADIO_LO_FREQUENCY 
        "03 20 34 01", # RC_CMD_RADIO_RX_INPUT
        "05 20 39 00 02 00", # RC_CMD_RADIO_RX_DBG_CTRL 
        "05 20 3F 01 07 07", #RC_CMD_RADIO_RX_CONFIG_RSSI
        "11 20 3B 00 0F 04 00 00 AE 1D 2E 00 01 01 05 01 00 00", #RC_CMD_RADIO_RX_CONFIG_2
        "13 20 3D 00 55 BE 01 00 07 00 46 00 09 00 66 26 00 01 00 0A", #RC_CMD_RADIO_RX_CDREC_2_NCK2982
        "21 20 3C 00 F1 00 00 00 07 00 FF 00 00 00 07 00 00 00 60 00 00 01 80 4C 40 01 01 05 02 03 01 01 01 01", #RC_CMD_RADIO_RX_DPROC_2 
        "19 20 3E 00 02 00 78 00 66 CD 3B 00 1D 00 03 00 57 02 0D 11 5E 0B 63 0C 02 08", #RC_CMD_RADIO_RX_SM_2_NCK2983
        "03 20 30 41",   #RC_CMD_RADIO_RX_ON    
        ]
    
NCK2984_FCA_PEPS_RECEIVE_config = [
        "02  20  10",#RC_CMD_RADIO_OFF
        "03  20  32  01",#RC_CMD_RADIO_RX_DEFAULTS
        "0B  20  13  10  90  6E  03  00  EE  03  1F  02",#RC_CMD_RADIO_LO_FREQUENCY  
        "03  20  34  01",#RC_CMD_RADIO_RX_INPUT  
        "05  20  39  00  02  00",#RC_CMD_RADIO_RX_DBG_CTRL  
        "05  20  3F  01  07  07",#RC_CMD_RADIO_RX_CONFIG_RSSI  
        "11  20  3B  00  8A  EC  00  00  AE  1D  5C  01  00  00  01  01  00  01",#RC_CMD_RADIO_RX_CONFIG_2  
        "13  20  3D  00  C0  CE  00  00  05  00  46  00  09  00  66  26  00  01  00  0A",#RC_CMD_RADIO_RX_CDREC_2_NCK2982  
        "21  20  3C  00  FE  01  00  00  0F  00  00  00  00  00  05  00  00  00  A0  00  00  01  B6  4C  66  01  01  05  02  03  01  01  01  01",#RC_CMD_RADIO_RX_DPROC_2  
        "19  20  3E  00  D5  07  16  00  66  CD  16  00  16  00  03  00  E1  00  65  09  02  00  DA  00  05  08",#RC_CMD_RADIO_RX_SM_2_NCK2983   
        "03  20  30  41",#RC_CMD_RADIO_RX_ON              
        ]


TRANSMIT_DICT = {"RKE" :NCK2984_FCA_RKE_TRANSMIT_config,
                 "PKE" :NCK2984_FCA_RKE_TRANSMIT_config,
                 "TPM" :NCK2984_FCA_RKE_TRANSMIT_config }

RECEIVE_DICT = {"RKE" :NCK2984_FCA_RKE_RECEIVE_config,
                "PKE" :NCK2984_FCA_PEPS_RECEIVE_config,
                "TPM" :NCK2984_FCA_RKE_RECEIVE_config }