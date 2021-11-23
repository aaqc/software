# ESP Communications Protocl (espcom)

## Packet byte structure

	+-+-----------+------------+
	|S| OP-HEADER | PARAMETERS |
	+-+-----------+------------+
	
	S: Packet size (read S segments)
	OP-HEADER: Operation Header (1B)
	INSTRUCTIONS: Operation parameters & instructions (nb)

### OP-HEADER

	Size: 1 Byte (8 bits)
	Type: unsigned 
	Range: 0-255
	Desc: Each integer in the range is a special instruction. 

### INSTRUCTIONS

	Size: n Byte(s)
