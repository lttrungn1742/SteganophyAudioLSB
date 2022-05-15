import sys

class ExtensionAudio:
    @staticmethod
    def getLengthHeader(name):
        data = {'wav':44}
        try:
            return data[name]
        except KeyError as e:
            raise "NonExtension"


class SteganophyLSB:
    @staticmethod
    def encrypt(secret : str, inFile, outFile):
        inStream = open(inFile,'rb').read()

        try:
            lenHeader = ExtensionAudio.getLengthHeader(inFile.split('.')[-1])
        except:
            return "Can not detect audio file"

        outStream = open(outFile,'wb')
        outStream.write(inStream[:lenHeader])

        block4lenSecret = inStream[lenHeader: lenHeader + len(secret)]

        block4Secret = inStream[lenHeader:lenHeader + len(secret) * 8]

        for element in  secret:
            for byte, bit in zip(block, '{0:08b}'.format(ord(element))):
                bit = int(bit)
                """
                    Neu 'bit = 1' thi se 'bitwise or' neu 'bit = 0' thi se thuc hien toan tu 'bitwise and'
                """
                new_byte = byte|bit if bit == 1 else byte&bit 
                outStream.write(chr(new_byte).encode()) 

        outStream.write(inStream[lenHeader+len(secret)*8:])

    @staticmethod
    def decrypt():
        lengthHeader = ExtensionAudio.getLengthHeader('wav')
        block = open('audio/outFile.wav','rb').read()[lengthHeader:lengthHeader+5*8]

        plain = ""
        for step in range(0, len(block)//8):
            character = []
            for bit in block[step * 8 : (step+1) * 8]:
                character.append('%s'%(bit&1))
            plain += chr(int(''.join(character),2))
        return plain
   