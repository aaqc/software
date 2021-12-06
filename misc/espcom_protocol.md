# ESP Communications Protocl (espcom)

## Packet byte structure

	+-+-----------+------------+-+
	|S| OP-HEADER | PARAMETERS |0|
	+-+-----------+------------+-+
	
	S: Packet size (read S segments)
	OP-HEADER: Operation Header (4b)
	INSTRUCTIONS: Operation parameters & instructions (nb)
	0: Null byte

### OP-HEADER

	Size: 1 Byte (8 bits)
	Type: unsigned 
	Range: 0-255
	Desc: Each integer in the range is a special instruction. 

### INSTRUCTIONS

	Size: n Byte(s)
