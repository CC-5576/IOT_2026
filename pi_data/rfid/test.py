from mfrc522.src.mfrc522 import MFRC522
from time import sleep

reader = MFRC522()
s = None
while s != reader.MI_OK:
    (s, TagType) = reader.Request(reader.PICC_REQIDL)
    if s == reader.MI_OK:
        print(f"Connection Success!\n Status: {s}\nTagType: {TagType}")

sleep(1)

(s, uid) = reader.Anticoll()
print(f" status: {s}")
print(f"    uid: {uid}")

reader.SelectTag(uid)
b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
d = []
for a in b:
    sleep(1)
    c = reader.ReadTag(a)
    if c:
        d += c
print(''.join(chr(i) for i in d))
