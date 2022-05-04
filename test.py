length_header = 32
def encode():
    audio = open("audio.wav",'rb').read()
    
    message  = "LeThanhTrung"
    ending = "END!!~~"
    frame_bytes = list(map(int,''.join(["{0:08b}".format(ord(i)) for i in message+ending])))
    write_bytes = []
    length_frame_bytes = len(frame_bytes)
    for byte, bit in zip(audio[length_header:length_frame_bytes], frame_bytes):
        write_bytes.append((byte & 254) | bit)
    outfile = open('outfile_.wav','wb')
    outfile.write(audio[:length_header] + ''.join([chr(i) for i in write_bytes]).encode() + audio[length_frame_bytes:])
    outfile.close()

def decode():
    audio = open("outfile_.wav",'rb').read()[length_header:100]
    frame_bytes = [ byte & 1 for byte in audio]
    string = "".join(chr(int("".join(map(str,frame_bytes[i:i+8])),2)) for i in range(0,len(frame_bytes),8))
    print(string)
    

decode()