import serial



def tc_initialize(ser):
    cmd_name = ["1. INPUT1 (reads the temperature of the primary thermistor)","2. DESIRED CONTROL VALUE (set value)","3. POWER OUTPUT","4. ALARM STATUS","5. INPUT 2","6. OUTPUT CURRENT COUNTS","7. ALARM TYPE",
                "8. SET TYPE DEFINE (the desired control temperature or “set temp” input definition)","9. SENSOR TYPE","10. CONTROL TYPE","11. CONTROL OUTPUT POLARITY","12. POWER ON/OFF",
                "13. OUTPUT SHUTDOWN IF ALARM","14. FIXED DESIRED CONTROL SETTING","15. PROPORTIONAL BANDWIDTH","16. INTEGRAL GAIN","17. DERIVATIVE GAIN","18. LOW EXTERNAL SET RANGE",
                "19. HIGH EXTERNAL SET RANGE","20. ALARM DEADBAND","21. HIGH ALARM SETTING","22. LOW ALARM SETTING","23. CONTROL DEADBAND SETTING","24. INPUT1 OFFSET","25. INPUT2 OFFSET","26. HEAT MULTIPLIER",
                "27. COOL MULTIPLIER","28. OVER CURRENT COUNT COMPARE VALUE","29. ALARM LATCH ENABLE","30. COMMUNICATIONS ADDRESS (reserved command, do not use)","31. ALARM LATCH RESET","32. CHOOSE SENSOR FOR ALARM FUNCTION",
                "33. CHOOSE °C or °F TEMPERATURE WORKING UNITS","34. EEPROM WRITE ENABLE","35. OVER CURRENT CONTINUOUS","36. OVER CURRENT RESTART ATTEMPS","37. JP3 DISPLAY ENABLE"]
    read_cmd = ["01","03","02","05","06","07","41","42","43","44","45","46","47","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","48",None,None,"4a","4b","4c","4d","5f","4e"]
    write_cmd = [None,None,None,None,None,None,"28","29","2a","2b","2c","2d","2e","1c","1d","1e","1f","20","21","22","23","24","25","26","27","0c","0d","0e","2f",None,"33","31","32","34","35","0f","36"]
    init_val = [2043,0,0,0,15566,130,0,0,1,2,1,0,1,0,500,0,0,0,10000,100,10000,0,100,0,0,20,20,14,0,None,0,0,1,1,0,300,0]

    for cmd_i in range(len(read_cmd)):
        if read_cmd[cmd_i] != None:
            print('\n\n%s: read %s' %(cmd_name[cmd_i], read_cmd[cmd_i]))
            val_back, _ = tc_talk(ser, [c for c in read_cmd[cmd_i]], 0)
            if write_cmd[cmd_i] != None and val_back != init_val[cmd_i]:
                print("Reset %s from %d to %d." % (cmd_name[cmd_i], val_back, init_val[cmd_i]))
                _ = tc_talk(ser, [c for c in write_cmd[cmd_i]], init_val[cmd_i])
                val_back_check,_ = tc_talk(ser, [c for c in read_cmd[cmd_i]], 0)
                
                print(val_back_check)

def tc_talk(ser, cmd_address, cmd_val):
    """
    Args:
        cmd_address - list of 2, specify the type of cmd
        cmd_val - decimal value for write
    Returns:
        val_back - int, converted decimal
        buf - list of length 8, original msg form TC
    """
    buf = [0,0,0,0,0,0,0,0,0,0,0,0]

    msg = tc_encoder(cmd_address, cmd_val)
    print('send: %s' % ''.join(msg))

    for pn in range(0,16):
        ser.write((msg[pn]).encode())

    for pn in range(0,12):
        buf[pn]=ser.read(1).decode()
        #print(buf[pn])

    print('back: %s' % ''.join(buf))

    val_back = tc_decoder(buf, msg)

    return val_back, buf

def tc_encoder(cmd_address, cmd_val):
    """
    Args:
        cmd_address - list of 2, specify the type of cmd
        cmd_val - int, decimal value for write
    Returns:
        cmd_str - list of char, final command to send to TC3625
    """
    # convert value
    val_hex = dec2hex(cmd_val)

    # device address + command address + hex value
    cmd_str_core = ['0', '0'] + cmd_address + val_hex

    # check sum
    cmd_str_core_ascii = [ord(char) for char in cmd_str_core]
    cmd_sum = hex(sum(cmd_str_core_ascii))[2:]
    cmd_sum = cmd_sum[-2:].zfill(2)

    # complete string
    cmd_str = ['*'] + cmd_str_core + [char.lower() for char in cmd_sum] + ['\r']
    return cmd_str

def tc_decoder(cmd_back, cmd_str):
    """
    Returns:
        val_back - int, decimal
    """
    if cmd_back == [0,0,0,0,0,0,0,0,0,0,0,0]:
        print(cmd_str)
        print('Cannot hear from COM.')
        val_back = None
    elif cmd_back == ['*','X','X','X','X','X','X','X','X','c','0','\r']:
        print(cmd_str)
        print('Check sum for the input is incorrect.')
        val_back = None
    else:
        back_sum = hex(sum([ord(char) for char in cmd_back[1:-3]]))[2:]
        back_sum = back_sum[-2:].zfill(2)
        
        if back_sum != (cmd_back[-3] + cmd_back[-2]):
            print('back checksum: %s' % back_sum)
            print(cmd_back)
            print('Checksum of the command returned from COM is incorrect.')
            val_back = None
        else:
            print(cmd_back[1:9])
            val_back = int(''.join(cmd_back[1:9]), 16)
            print('value back: %d' % val_back)

    return val_back


def hexc2dec(bufp):
    """
    Args:
        bufp - list of len 8
    Returns:
        newval - int in decimal
    """
    newval=0
    divvy=pow(16,7)
    #sets the word size to DDDDDDDD
    for pn in range (1,7):
            vally=ord(bufp[pn])
            if(vally < 97):
                    subby=48
            else:
                    subby=87
                # ord() converts the character to the ascii number value
            newval += ((ord(bufp[pn])-subby)*divvy)
            divvy/=16
            if(newval > pow(16,8)/2-1):
                    newval=newval-pow(16,8)
                #distinguishes between positive and negative numbers
    return newval

def dec2hex(val):
    """
    Args:
        val - int, decimal
    Returns:
        list of len 8, hex value
    """
    hexval = hex(val)[2:].zfill(8)
    return [char.lower() for char in hexval]




if __name__ == "__main__":
    # tc = TC()
    # tc.talk()
    # tc.listen()
    # tc.close()

    ser = serial.Serial('com3', 9600, timeout=1)
    tc_initialize(ser)

    # _ = tc_talk(ser, ['1','c'], 1000)
    # set_temp, _ = tc_talk(ser, ['5','0'], 0)
    # print(set_temp/100.0)
    # val_back, buf = tc_talk(ser, ['0','1'], 0)
    # print(val_back/100.0)
    ser.close()

    

    print("PORT CLOSED")        
    