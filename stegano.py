import sys

class ExtensionAudio:
    @staticmethod
    def getLengthHeader(name):
        data = {'wav':45}
        try:
            return data[name]
        except KeyError as e:
            raise "NonExtension"


class SteganophyLSB():
    
    padding=  '\xff\xfe\xfd\xfc'

    @staticmethod
    def encrypt(secret : str, inFile, outFile):
        inStream = open(inFile,'rb').read()

        try:
            lenHeader = ExtensionAudio.getLengthHeader(inFile.split('.')[-1])
        except:
            return "Can not detect audio file"

        outStream = open(outFile,'wb')
        outStream.write(inStream[:lenHeader])


         
        lenSecret = len(secret) # lay do dai cua secret
        
        secret = f"{lenSecret}{SteganophyLSB.padding}{secret}"

        block4Secret = inStream[lenHeader:lenHeader + len(secret) * 8]
        outStream.write(block4Secret)
        for element in  secret:
            for byte, bit in zip(block4Secret, '{0:08b}'.format(ord(element))):
                bit = int(bit)
                """
                    Neu 'bit = 1' thi se 'bitwise or' neu 'bit = 0' thi se thuc hien toan tu 'bitwise and'
                """
                new_byte =  byte|bit if bit == 1 else byte&bit 
                outStream.write(chr(new_byte).encode())  

        outStream.write(inStream[lenHeader+len(secret)*8:])

    @staticmethod
    def detectLengthSecret(inStream):
        p = SteganophyLSB.block2str(inStream[:(len('%s'%(len(inStream)//8)) + len(SteganophyLSB.padding)) * 8])
        print(p)
        return p.split(SteganophyLSB.padding)[0]

    @staticmethod
    def block2str(block):
        return ''.join([chr(int(''.join(['%s'%(bit&1) for bit in block[step * 8 : (step+1) * 8]]),2)) for step in range(0, len(block)//8) ])

    @staticmethod
    def decrypt(inFile):
        lengthHeader = ExtensionAudio.getLengthHeader('wav')
        inStream = open(inFile,'rb').read()[lengthHeader:]
        lengthSecret = SteganophyLSB.detectLengthSecret(inStream)

        a = len(lengthSecret)+ len(SteganophyLSB.padding)

        block = inStream[a*8:(int(lengthSecret)+a)*8]
        return SteganophyLSB.block2str(block)
        

        

SteganophyLSB.encrypt('trung','audio/audio.wav','audio/outFile.wav')

a = SteganophyLSB.decrypt('audio/outFile.wav')

print('decrypt: ',a)