# ASC (AAQC-Serial-Communcation)
## ESP Communications Protocl (espcom)

## Packet byte structure

	< 2B >< 2B><  1B  ><  SB  >
	+----+-----+--------+------+
	|  S  |  C | OPCODE | DATA |
	+----+-----+--------+------+
		
	S: Data size (read n bytes) (2B)
	C: Checksum (2B)
	OPCODE: Operation code (1B)
	DATA: Operation parameters & instructions (nB)

### Data size

	Size: 2 Bytes
	Type: unsigned
	Range: 0-511
	Desc: Size of the data (n).

### C (Checksum)
	
	Size: 2 Bytes
	Type: unsigned dchar 
	Range: 2 bytes (16 bits)
	Desc: Checksum 

### OPCODE 

	Size: 1 Byte or 8 Bits
	Type: unsigned 
	Range: 0-255
	Desc: Each integer in the range is a special instruction. 

### DATA 

	Size: n Byte(s)
	Desc: Data/parameters for the opcode


## OPCODES:
 - FORWARD
 - RIGHT
 - UP
 - LIGHTS
 