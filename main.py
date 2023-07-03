import snap7
import struct

myplc = snap7.client.Client()

myplc.connect('192.168.0.15', 0, 1)
print('Connection to PLC = ', myplc.get_connected())

temp = myplc.db_read(1,0,4)
Temperature = struct.unpack('>f', temp)[0]
Cold = struct.unpack('B', myplc.db_read(1, 4, 1))[0]
RPis_to_Buy = struct.unpack('>h', myplc.db_read(1, 6, 2))[0]
Db_test_String = myplc.db_read(1, 8, 8).decode('cp1252')[2:-1]

print('Real variable =', Temperature)
print('Bit variable = ', Cold)
print('Integer variable = ', RPis_to_Buy)
print('String variable = ', Db_test_String)

#print(myplc.get_exec_time())
#print(myplc.get_pdu_length() )
M_bites = bin(struct.unpack('>h',myplc.mb_read(0,2))[0])
print('Markers memory = ',M_bites)

m_write_int = 1
m_write_byte = m_write_int.to_bytes(1,'big')
myplc.mb_write(0,1, m_write_byte)

myplc.db_write(1,4, m_write_byte)

myplc.disconnect()
