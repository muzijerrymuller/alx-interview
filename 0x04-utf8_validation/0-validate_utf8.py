#!/usr/bin/python3
def validUTF8(data):
    """
    Method that determines if a given data set represents a validation
    UTF-8 encoding.
    Parameters:
    data (list): List of integers where each integer represents 1 byte.
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    
    number_bytes = 0
    
    for byte in data:
        
        if number_bytes == 0:
            
            if (byte >> 5) == 0b110:
                number_bytes = 1
            elif (byte >> 4) == 0b1110:
                number_bytes = 2
            elif (byte >> 3) == 0b11110:
                number_bytes = 3
            elif byte >> 7
                return False
            else:  # We are expecting continuation bytes
                if (byte >> 6) != 0b10:
                    return False
                number_bytes -= 1
                
                return number_bytes == 0 
