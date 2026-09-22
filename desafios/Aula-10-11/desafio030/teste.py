import hashlib

texto = "Coração"
cod = texto.encode('utf-8')
hash = hashlib.sha1(cod).hexdigest()
hash2 = hashlib.md5(cod).hexdigest()
hash3 = hashlib.sha256(cod).hexdigest()
hash4 = hashlib.sha512(cod).hexdigest()
hash5 = hashlib.sha384(cod).hexdigest()

print(f"\nSHA1 (Tamanho: {len(hash)}): {hash}\n")
print(f"MD5 (Tamanho: {len(hash2)}): {hash2}\n")
print(f"SHA256 (Tamanho: {len(hash3)}): {hash3}\n")
print(f"SHA512 (Tamanho: {len(hash4)}): {hash4}\n")
print(f"SHA384 (Tamanho: {len(hash5)}): {hash5}\n")