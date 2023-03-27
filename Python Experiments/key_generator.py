import os
import datetime
import OpenSSL.crypto

key = OpenSSL.crypto.PKey()
key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

common_name = input("Enter common name for key (e.g. example.com): ")
organizationalUnitName = input("Enter organizational unit name for key (e.g. mc): ")
organization = input("Enter organization for key (e.g. MyCompany): ")
country_code = input("Enter 2-letter country code for key (e.g. US): ")

req = OpenSSL.crypto.X509Req()
subj = req.get_subject()
subj.commonName = common_name
subj.organizationalUnitName = organizationalUnitName
subj.organizationName = organization
subj.countryName = country_code
req.set_pubkey(key)
req.sign(key, 'sha256')

cert = OpenSSL.crypto.X509()
cert.set_subject(subj)
cert.set_serial_number(int.from_bytes(os.urandom(16), byteorder='big'))

valid_from = datetime.datetime.utcnow()
valid_until = valid_from + datetime.timedelta(days=3651)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(int((valid_until - valid_from).total_seconds()))

cert.set_issuer(cert.get_subject())
cert.set_pubkey(key)
cert.sign(key, 'sha256')

# Write the private key and certificate to PEM files
with open('private_key.pem', 'wb') as f:
    f.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key))
    
with open('certificate.pem', 'wb') as f:
    f.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
