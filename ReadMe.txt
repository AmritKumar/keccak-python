Content
-------

List of files:
	- Keccak.py : the Keccak and KeccakError classes
	- demo_KeccakF.py : example of use of Keccak_f function on a 0-filled 5×5 matrix
	- demo_TestVectors.py : verification of Short/Long test vectors. The test vectors must be copied in the same location as the Python files


Few words of explanation
------------------------

The Keccak module is stateless. It takes your inputs, performs the computation and returns the result.


Typical uses
------------

1) Compute a hash using Keccak[r=1152, c=448] (224 bits of output) on '00112233445566778899AABBCCDDEEFF' (8*16bits=128 bits)

>>> import Keccak
>>> myKeccak=Keccak.Keccak()
>>> myKeccak.Keccak((128,'00112233445566778899AABBCCDDEEFF'),1152,448,224,True)

Create a Keccak function with (r=1152, c=448 (i.e. w=64))

String ready to be absorbed: 00112233445566778899AABBCCDDEEFF0100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080 (will be completed by 56 x '00')

Current value of state: Before first round
	['0x7766554433221100', '0xffeeddccbbaa9988', '0x1', '0x0', '0x0']
	['0x0', '0x0', '0x0', '0x0', '0x0']
	['0x0', '0x0', '0x0', '0x0', '0x0']
	['0x0', '0x0', '0x8000000000000000', '0x0', '0x0']
	['0x0', '0x0', '0x0', '0x0', '0x0']
Current value of state: Satus end of round #1/24
	['0xdc77ae5456dd06dd', '0x2110377665444332', '0x7e6e5e6e7e6e5e6e', '0x8019e64c44470000', '0xba208b329807a91']
	['0x5669988982a11005', '0xa8864666600eeaaa', '0xe3304ddaaffcc99e', '0x42206eecc2a88664', '0xb77bbffbb77bbffb']
	['0x1111111110111117', '0x371dfb48ae8462d1', '0x224555108b45ff10', '0xddba8867553200ef', '0x4c3bf7a26e19d5e']
	['0xcb3621d00772611c', '0x13f17c0eb95b8bb5', '0x985510cc88440ddd', '0x2cd47cc54bb25aa3', '0x35c1100ff8899883']
	['0x5deab70448bfe251', '0x88a62388992232cc', '0x7788547722dd0032', '0x8804819c9915908c', '0xdd995510cc88440d']
<...>
Current value of state: Satus end of round #24/24
	['0xd89c919ce8078903', '0x92ff885abc7f0af9', '0xa0cdebf3ae8d1078', '0xde568902e183b3ce', '0xe3d1096857dc5b35']
	['0xc5f432f2633d3da0', '0x6a0094e2d96f8f35', '0xff92be8c648edc5a', '0xb87fe7012b84523a', '0xb8b7e144e77b3096']
	['0xf4832b396a99f318', '0xd8c10bcbaed2e2cf', '0x7d0f5ff34fc95a2e', '0x404281a6b9b3c2a2', '0xa758a863c74aecbe']
	['0x5b0f0672fcebc63e', '0xfca88e2204aa233e', '0xb62ef1ba33bc5a69', '0x795abef031f2d7dd', '0x7b7dc16e91fff6cd']
	['0x677823df6ebd0544', '0xd2a1fc63c7702e0e', '0x49b07e16adc62d95', '0x6bdb0b4f074e8b2b', '0xc27f39383b4799b5']

Value after absorption : 038907E89C919CD8F90A7FBC5A88FF9278108DAEF3EBCDA0CEB383E1028956DE355BDC576809D1E3A03D3D63F232F4C5358F6FD9E294006A5ADC8E648CBE92FF3A52842B01E77FB896307BE744E1B7B818F3996A392B83F4CFE2D2AECB0BC1D82E5AC94FF35F0F7DA2C2B3B9A6814240BEEC4AC763A858A73EC6EBFC72060F5B3E23AA04228EA8FC695ABC33BAF12EB6DDD7F231F0BE5A79CDF6FF916EC17D7B4405BD6EDF2378670E2E70C763FCA1D2952DC6AD167EB0492B8B4E074F0BDB6BB599473B38397FC2

Value after squeezing : 038907E89C919CD8F90A7FBC5A88FF9278108DAEF3EBCDA0CEB383E1028956DE355BDC576809D1E3A03D3D63F232F4C5358F6FD9E294006A5ADC8E648CBE92FF3A52842B01E77FB896307BE744E1B7B818F3996A392B83F4CFE2D2AECB0BC1D82E5AC94FF35F0F7DA2C2B3B9A6814240BEEC4AC763A858A73EC6EBFC72060F5B3E23AA04228EA8FC695ABC33BAF12EB6DDD7F231F0BE5A79CDF6FF916EC17D7B4405BD6EDF2378670E2E70C763FCA1D2952DC6AD167EB0492B8B4E074F0BDB6BB599473B38397FC2

'038907E89C919CD8F90A7FBC5A88FF9278108DAEF3EBCDA0CEB383E1'


2) Computation of the Keccak-f function on an all-zero state

>>> import Keccak
>>> A=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
>>> myKeccak=Keccak.Keccak(1600)
>>> myKeccak.Keccakf(A, True)
>>> myKeccak.printState(A,'Final result')

Current value of state: Before first round
        ['0x0', '0x0', '0x0', '0x0', '0x0']
        ['0x0', '0x0', '0x0', '0x0', '0x0']
        ['0x0', '0x0', '0x0', '0x0', '0x0']
        ['0x0', '0x0', '0x0', '0x0', '0x0']
        ['0x0', '0x0', '0x0', '0x0', '0x0']
Current value of state: Satus end of round #1/24
        ['0x1L', '0x0L', '0x0L', '0x0L', '0x0L']
        ['0x0L', '0x0L', '0x0L', '0x0L', '0x0L']
        ['0x0L', '0x0L', '0x0L', '0x0L', '0x0L']
        ['0x0L', '0x0L', '0x0L', '0x0L', '0x0L']
        ['0x0L', '0x0L', '0x0L', '0x0L', '0x0L']
<...>
Current value of state: Satus end of round #24/24
        ['0xf1258f7940e1dde7L', '0x84d5ccf933c0478aL', '0xd598261ea65aa9eeL', '0xbd1547306f80494dL', '0x8b284e056253d057L']
        ['0xff97a42d7f8e6fd4L', '0x90fee5a0a44647c4L', '0x8c5bda0cd6192e76L', '0xad30a6f71b19059cL', '0x30935ab7d08ffc64L']
        ['0xeb5aa93f2317d635L', '0xa9a6e6260d712103L', '0x81a57c16dbcf555fL', '0x43b831cd0347c826L', '0x1f22f1a11a5569fL']
        ['0x5e5635a21d9ae61L', '0x64befef28cc970f2L', '0x613670957bc46611L', '0xb87c5a554fd00ecbL', '0x8c3ee88a1ccf32c8L']
        ['0x940c7922ae3a2614L', '0x1841f924a2c509e4L', '0x16f53526e70465c2L', '0x75f644e97f30a13bL', '0xeaf1ff7b5ceca249L']

[[17376452488221285863L, 18417369716475457492L, 16959053435453822517L, 424854978622500449L, 10668034807192757780L], [9571781953733
019530L, 10448040663659726788L, 12224711289652453635L, 7259519967065370866L, 1747952066141424100L], [15391093639620504046L, 101139
17136857017974L, 9342009439668884831L, 7004910057750291985L, 1654286879329379778L], [13624874521033984333L, 12479658147685402012L,
 4879704952849025062L, 13293599522548616907L, 8500057116360352059L], [10027350355371872343L, 3500241080921619556L, 140226327413610
143L, 10105770293752443592L, 16929593379567477321L]]







