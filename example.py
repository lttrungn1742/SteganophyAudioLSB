import wave, argparse

class Steganophy:
    characters_padding = "#%&~en@"
    bytes_padding = b"#$end$#"
    def __init__(self, audioIn, audioOut=None, plaintext=None, file=None) -> None:
        self.audio = audioIn
        self.plaintext = plaintext
        self.audioOut = audioOut
        self.file = file

    def encrytMessage(self):
        audio = wave.open(self.audio,mode="rb")
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        lenght_padding = (len(frame_bytes)-(len(self.plaintext)*8*8))//8 - len(self.characters_padding)
        if lenght_padding  < 0:
            return False, "Plaintext is really long"
  
        bits = list(map(int, ''.join(["{0:08b}".format(ord(i)) for i in (self.plaintext + self.characters_padding)]))) 
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        path_outfile = self.audioOut
        outfile = wave.open(path_outfile,'wb')
        outfile.setparams(audio.getparams())
        outfile.writeframes(bytes(frame_bytes))
        outfile.close()
        audio.close()
        
        return True, path_outfile

    def decrytMessage(self):
        audio = wave.open(self.audio, mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        return string.split(self.characters_padding)[0]

    def encrytFile(self):
        audio = wave.open(self.audio,mode="rb")
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        file = open(self.file,mode='rb').read()
        lenght_padding = (len(frame_bytes)-(len(file)*8*8))//8 - len(self.bytes_padding)
        if lenght_padding  < 0:
            return False, "File is really larger"
  
        bits = list(map(int, ''.join(["{0:08b}".format(i) for i in (file + self.bytes_padding)]))) 
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        path_outfile = self.audioOut
        outfile = wave.open(path_outfile,'wb')
        outfile.setparams(audio.getparams())
        outfile.writeframes(bytes(frame_bytes))
        outfile.close()
        audio.close()
        
        return True, path_outfile

    def decrytMessage(self):
        audio = wave.open(self.audio, mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        return string.split(self.characters_padding)[0]


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--infile", action="store",
                        help="audio file need to be steganography", dest="infile")
    parser.add_argument("-o","--outfile", action="store", 
                        help="out file need be exported", dest="outfile")
    parser.add_argument("-m","--message", action="store",
                        help="message", dest="message")    
    parser.add_argument("-e","--encode",action="store_true", dest="encode") 
    parser.add_argument("-d","--decode", action="store_true", dest="decode")
    parser.add_argument("-f","--file", action="store", type=str, dest="file")

    argv = parser.parse_args()      
    if argv.file != None and argv.message != None:
        exit("Message or file")
    if argv.encode:
        if argv.message != None:
            isSuccess, message =  Steganophy(argv.infile, argv.outfile, argv.message).encrytMessage()
            print(f"Success, path file: {message}" if isSuccess else message )
        else:
            isSuccess, message =  Steganophy(argv.infile, argv.outfile, argv.file)
            print(f"Success, path file: {message}" if isSuccess else message )    
    elif argv.decode:
        message =  Steganophy(argv.infile).decrytMessage()
        print(f"message has been decrypted: {message}" )