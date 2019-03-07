# import json
# from base64 import b64encode
import binascii
#from aes_ccm import AesCcm
import AesCcm
# from Crypto.Random import get_random_bytes

print("Hello AES-CCM")

# Key: 1AE1CC81F39199114EB794C944E655DF
# Timestamp: 5c52184b
# Plain payload: 7036A81BC8DF9CBF1542CDFBCE427E1EB996DD935C9E38E269AE82E85CF7245B
# Init vector: 3438343373369509000001
# Header: 34383433733695095C52184B
# Clear tag: 3AA2DCC6
# Crypted payload: BC9305C19CEF104CE6ABC6CEEACFA92073A39AF9A5F55F83DEF8A539D262F231
# R: 34383433733695095C52184B000001BC9305C19CEF104CE6ABC6CEEACFA92073A39AF9A5F55F83DEF8A539D262F2317EFE87F9

# header = binascii.unhexlify('34383433733695095C52184B'.replace(' ',''))
# data = binascii.unhexlify('7036A81BC8DF9CBF1542CDFBCE427E1EB996DD935C9E38E269AE82E85CF7245B'.replace(' ',''))
# key = binascii.unhexlify('1AE1CC81F39199114EB794C944E655DF'.replace(' ',''))
# nonce = binascii.unhexlify('3438343373369509000001'.replace(' ',''))
# header = bytes.fromhex('34383433733695095C52184B'.replace(' ',''))
# data = bytes.fromhex('7036A81BC8DF9CBF1542CDFBCE427E1EB996DD935C9E38E269AE82E85CF7245B'.replace(' ',''))
# key = bytes.fromhex('1AE1CC81F39199114EB794C944E655DF'.replace(' ',''))
# nonce = bytes.fromhex('3438343373369509000001'.replace(' ',''))
header = bytes( binascii.unhexlify('34383433733695095C52184B'.replace(' ','')) )
data = bytes( binascii.unhexlify('7036A81BC8DF9CBF1542CDFBCE427E1EB996DD935C9E38E269AE82E85CF7245B'.replace(' ','')) )
key = bytes( binascii.unhexlify('1AE1CC81F39199114EB794C944E655DF'.replace(' ','')) )
nonce = bytes( binascii.unhexlify('3438343373369509000001'.replace(' ','')) )

cipher = AesCcm.new(key, nonce=nonce, mac_len=4)
cipher.update(header)
ciphertext, tag = cipher.encrypt_and_digest(data)

json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
#json_v = [ b64encode(x).decode('utf-8') for x in [cipher.nonce, header, ciphertext, tag] ]
#json_v = [ binascii.hexlify(x) for x in [cipher.nonce, header, ciphertext, tag] ]
json_v = [ x.hex() for x in [cipher.nonce, header, ciphertext, tag] ]
result = json.dumps(dict(zip(json_k, json_v)))
print(result)
