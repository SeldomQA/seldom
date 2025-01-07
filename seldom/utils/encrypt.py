"""
Encryption Utility Module

Provides comprehensive encryption and decryption functionalities, supporting the following features:

Features:
    - Hash Algorithms
        * MD5
        * SHA1/SHA224/SHA256/SHA384/SHA512
        * HMAC
    - Symmetric Encryption
        * AES (CBC/ECB/CFB/OFB/CTR)
        * DES
        * 3DES
    - Asymmetric Encryption
        * RSA
    - Encoding Conversion
        * Base16/Base32/Base64/Base85
        * URL Encoding
        * HTML Encoding
    - Random Number Generation
        * Secure Random Numbers
        * UUID Generation
"""

import base64
import hashlib
import hmac
import html
import urllib.parse
import uuid
from enum import Enum, auto
from functools import wraps
from typing import Optional, Type

from Crypto.Cipher import AES, DES, DES3, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from seldom.logging import log


class CipherMode(Enum):
    """Cipher Mode Enumeration"""
    ECB = auto()
    CBC = auto()
    CFB = auto()
    OFB = auto()
    CTR = auto()


def encrypt_handler(func):
    """Decorator for encryption operations"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            log.info(f"✅ [{func.__name__}] method, generated data: {result}")
            return result
        except Exception as e:
            log.error(f"❌ [{func.__name__}] operation failed: {str(e)}")
            raise

    return wrapper


class HashUtil:
    """Hash Algorithm Utility Class"""

    @staticmethod
    @encrypt_handler
    def md5(text: str, encoding: str = 'utf-8') -> str:
        """MD5 Hash"""
        return hashlib.md5(str(text).encode(encoding)).hexdigest()

    @staticmethod
    @encrypt_handler
    def sha1(text: str, encoding: str = 'utf-8') -> str:
        """SHA1 Hash"""
        return hashlib.sha1(str(text).encode(encoding)).hexdigest()

    @staticmethod
    @encrypt_handler
    def sha256(text: str, encoding: str = 'utf-8') -> str:
        """SHA256 Hash"""
        return hashlib.sha256(str(text).encode(encoding)).hexdigest()

    @staticmethod
    @encrypt_handler
    def sha512(text: str, encoding: str = 'utf-8') -> str:
        """SHA512 Hash"""
        return hashlib.sha512(str(text).encode(encoding)).hexdigest()

    @staticmethod
    @encrypt_handler
    def hmac_sha256(key: str, text: str, encoding: str = 'utf-8') -> str:
        """HMAC-SHA256"""
        return hmac.new(
            key.encode(encoding),
            text.encode(encoding),
            hashlib.sha256
        ).hexdigest()


class AESUtil:
    """AES Encryption Utility Class"""

    @staticmethod
    def _pad_key(key: bytes) -> bytes:
        """Adjust key length to 16/24/32 bytes"""
        key_length = len(key)
        if key_length <= 16:
            return key.ljust(16, b'\0')
        elif key_length <= 24:
            return key.ljust(24, b'\0')
        else:
            return key.ljust(32, b'\0')

    @staticmethod
    @encrypt_handler
    def encrypt(key: str, text: str, mode: CipherMode = CipherMode.CBC,
                encoding: str = 'utf-8') -> str:
        """
        AES Encryption

        Args:
            key: Key (automatically adjusted to 16/24/32 bytes)
            text: Text to encrypt
            mode: Encryption mode
            encoding: Character encoding

        Returns:
            str: Base64-encoded encrypted result
        """
        # Process key
        padded_key = AESUtil._pad_key(key.encode(encoding))

        # Generate random IV
        iv = get_random_bytes(16)

        # Create cipher
        if mode == CipherMode.ECB:
            cipher = AES.new(padded_key, AES.MODE_ECB)
        else:
            cipher = AES.new(padded_key, getattr(AES, f'MODE_{mode.name}'), iv)

        # Encrypt
        padded_data = pad(text.encode(encoding), AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)

        # Combine IV and encrypted data
        result = iv + encrypted_data if mode != CipherMode.ECB else encrypted_data

        return base64.b64encode(result).decode(encoding)

    @staticmethod
    @encrypt_handler
    def decrypt(key: str, encrypted_text: str, mode: CipherMode = CipherMode.CBC,
                encoding: str = 'utf-8') -> str:
        """
        AES Decryption

        Args:
            key: Key (automatically adjusted to 16/24/32 bytes)
            encrypted_text: Base64-encoded encrypted text
            mode: Encryption mode
            encoding: Character encoding

        Returns:
            str: Decrypted original text
        """
        # Process key
        padded_key = AESUtil._pad_key(key.encode(encoding))

        # Decode Base64
        encrypted_data = base64.b64decode(encrypted_text)

        # Extract IV and encrypted data
        if mode == CipherMode.ECB:
            iv = b''
            cipher_text = encrypted_data
        else:
            iv = encrypted_data[:16]
            cipher_text = encrypted_data[16:]

        # Create cipher
        if mode == CipherMode.ECB:
            cipher = AES.new(padded_key, AES.MODE_ECB)
        else:
            cipher = AES.new(padded_key, getattr(AES, f'MODE_{mode.name}'), iv)

        # Decrypt
        decrypted_data = cipher.decrypt(cipher_text)
        unpadded_data = unpad(decrypted_data, AES.block_size)

        return unpadded_data.decode(encoding)


class DESUtil:
    """DES Encryption Utility Class"""

    @staticmethod
    def _pad_key(key: bytes) -> bytes:
        """Adjust key length to 8 bytes"""
        return key[:8].ljust(8, b'\0')

    @staticmethod
    @encrypt_handler
    def encrypt(key: str, text: str, mode: CipherMode = CipherMode.CBC,
                encoding: str = 'utf-8') -> str:
        """
        DES Encryption

        Args:
            key: Key (automatically adjusted to 8 bytes)
            text: Text to encrypt
            mode: Encryption mode
            encoding: Character encoding

        Returns:
            str: Base64-encoded encrypted result
        """
        # Process key
        padded_key = DESUtil._pad_key(key.encode(encoding))

        # Generate random IV
        iv = get_random_bytes(8)

        # Create cipher
        if mode == CipherMode.ECB:
            cipher = DES.new(padded_key, DES.MODE_ECB)
        else:
            cipher = DES.new(padded_key, getattr(DES, f'MODE_{mode.name}'), iv)

        # Encrypt
        padded_data = pad(text.encode(encoding), DES.block_size)
        encrypted_data = cipher.encrypt(padded_data)

        # Combine IV and encrypted data
        result = iv + encrypted_data if mode != CipherMode.ECB else encrypted_data

        return base64.b64encode(result).decode(encoding)

    @staticmethod
    @encrypt_handler
    def decrypt(key: str, encrypted_text: str, mode: CipherMode = CipherMode.CBC,
                encoding: str = 'utf-8') -> str:
        """
        DES Decryption

        Args:
            key: Key (automatically adjusted to 8 bytes)
            encrypted_text: Base64-encoded encrypted text
            mode: Encryption mode
            encoding: Character encoding

        Returns:
            str: Decrypted original text
        """
        # Process key
        padded_key = DESUtil._pad_key(key.encode(encoding))

        # Decode Base64
        encrypted_data = base64.b64decode(encrypted_text)

        # Extract IV and encrypted data
        if mode == CipherMode.ECB:
            iv = b''
            cipher_text = encrypted_data
        else:
            iv = encrypted_data[:8]
            cipher_text = encrypted_data[8:]

        # Create cipher
        if mode == CipherMode.ECB:
            cipher = DES.new(padded_key, DES.MODE_ECB)
        else:
            cipher = DES.new(padded_key, getattr(DES, f'MODE_{mode.name}'), iv)

        # Decrypt
        decrypted_data = cipher.decrypt(cipher_text)
        unpadded_data = unpad(decrypted_data, DES.block_size)

        return unpadded_data.decode(encoding)


class TripleDESUtil:
    """3DES Encryption Utility Class"""

    @staticmethod
    def _pad_key(key: bytes) -> bytes:
        """Adjust key length to 24 bytes"""
        return key[:24].ljust(24, b'\0')

    @staticmethod
    @encrypt_handler
    def encrypt(key: str, text: str, mode: CipherMode = CipherMode.CBC,
                encoding: str = 'utf-8') -> str:
        """
        3DES Encryption

        Args:
            key: Key (automatically adjusted to 24 bytes)
            text: Text to encrypt
            mode: Encryption mode
            encoding: Character encoding

        Returns:
            str: Base64-encoded encrypted result
        """
        # Process key
        padded_key = TripleDESUtil._pad_key(key.encode(encoding))

        # Generate random IV
        iv = get_random_bytes(8)

        # Create cipher
        if mode == CipherMode.ECB:
            cipher = DES3.new(padded_key, DES3.MODE_ECB)
        else:
            cipher = DES3.new(padded_key, getattr(DES3, f'MODE_{mode.name}'), iv)

        # Encrypt
        padded_data = pad(text.encode(encoding), DES3.block_size)
        encrypted_data = cipher.encrypt(padded_data)

        # Combine IV and encrypted data
        result = iv + encrypted_data if mode != CipherMode.ECB else encrypted_data

        return base64.b64encode(result).decode(encoding)

    @staticmethod
    @encrypt_handler
    def decrypt(key: str, encrypted_text: str, mode: CipherMode = CipherMode.CBC,
                encoding: str = 'utf-8') -> str:
        """
        3DES Decryption

        Args:
            key: Key (automatically adjusted to 24 bytes)
            encrypted_text: Base64-encoded encrypted text
            mode: Encryption mode
            encoding: Character encoding

        Returns:
            str: Decrypted original text
        """
        # Process key
        padded_key = TripleDESUtil._pad_key(key.encode(encoding))

        # Decode Base64
        encrypted_data = base64.b64decode(encrypted_text)

        # Extract IV and encrypted data
        if mode == CipherMode.ECB:
            iv = b''
            cipher_text = encrypted_data
        else:
            iv = encrypted_data[:8]
            cipher_text = encrypted_data[8:]

        # Create cipher
        if mode == CipherMode.ECB:
            cipher = DES3.new(padded_key, DES3.MODE_ECB)
        else:
            cipher = DES3.new(padded_key, getattr(DES3, f'MODE_{mode.name}'), iv)

        # Decrypt
        decrypted_data = cipher.decrypt(cipher_text)
        unpadded_data = unpad(decrypted_data, DES3.block_size)

        return unpadded_data.decode(encoding)


class RSAUtil:
    """RSA Encryption Utility Class"""

    def __init__(self, public_key: Optional[str] = None,
                 private_key: Optional[str] = None):
        """
        Initialize RSA Utility

        Args:
            public_key: PEM-format public key
            private_key: PEM-format private key
        """
        self.public_key = RSA.import_key(public_key) if public_key else None
        self.private_key = RSA.import_key(private_key) if private_key else None

    @staticmethod
    @encrypt_handler
    def generate_key_pair(bits: int = 2048) -> tuple[str, str]:
        """
        Generate RSA Key Pair

        Args:
            bits: Key length

        Returns:
            tuple: (Public key, Private key) in PEM format
        """
        key = RSA.generate(bits)
        private_key = key.export_key().decode()
        public_key = key.publickey().export_key().decode()
        return public_key, private_key

    @encrypt_handler
    def encrypt(self, text: str, encoding: str = 'utf-8') -> str:
        """
        RSA Encryption

        Args:
            text: Text to encrypt
            encoding: Character encoding

        Returns:
            str: Base64-encoded encrypted result
        """
        if not self.public_key:
            raise ValueError("Public key not set")

        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_data = cipher.encrypt(text.encode(encoding))
        return base64.b64encode(encrypted_data).decode(encoding)

    @encrypt_handler
    def decrypt(self, encrypted_text: str, encoding: str = 'utf-8') -> str:
        """
        RSA Decryption

        Args:
            encrypted_text: Base64-encoded encrypted text
            encoding: Character encoding

        Returns:
            str: Decrypted original text
        """
        if not self.private_key:
            raise ValueError("Private key not set")

        cipher = PKCS1_OAEP.new(self.private_key)
        encrypted_data = base64.b64decode(encrypted_text)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode(encoding)


class EncodeUtil:
    """Encoding Utility Class"""

    @staticmethod
    @encrypt_handler
    def base64_encode(text: str, encoding: str = 'utf-8') -> str:
        """Base64 Encoding"""
        return base64.b64encode(text.encode(encoding)).decode(encoding)

    @staticmethod
    @encrypt_handler
    def base64_decode(text: str, encoding: str = 'utf-8') -> str:
        """Base64 Decoding"""
        return base64.b64decode(text).decode(encoding)

    @staticmethod
    @encrypt_handler
    def url_encode(text: str) -> str:
        """URL Encoding"""
        return urllib.parse.quote(text)

    @staticmethod
    @encrypt_handler
    def url_decode(text: str) -> str:
        """URL Decoding"""
        return urllib.parse.unquote(text)

    @staticmethod
    @encrypt_handler
    def html_encode(text: str) -> str:
        """HTML Encoding"""
        return html.escape(text)

    @staticmethod
    @encrypt_handler
    def html_decode(text: str) -> str:
        """HTML Decoding"""
        return html.unescape(text)

    @staticmethod
    @encrypt_handler
    def base16_encode(text: str, encoding: str = 'utf-8') -> str:
        """Base16 Encoding"""
        return base64.b16encode(text.encode(encoding)).decode(encoding)

    @staticmethod
    @encrypt_handler
    def base16_decode(text: str, encoding: str = 'utf-8') -> str:
        """Base16 Decoding"""
        return base64.b16decode(text).decode(encoding)

    @staticmethod
    @encrypt_handler
    def base32_encode(text: str, encoding: str = 'utf-8') -> str:
        """Base32 Encoding"""
        return base64.b32encode(text.encode(encoding)).decode(encoding)

    @staticmethod
    @encrypt_handler
    def base32_decode(text: str, encoding: str = 'utf-8') -> str:
        """Base32 Decoding"""
        return base64.b32decode(text).decode(encoding)

    @staticmethod
    @encrypt_handler
    def base85_encode(text: str, encoding: str = 'utf-8') -> str:
        """Base85 Encoding"""
        return base64.b85encode(text.encode(encoding)).decode(encoding)

    @staticmethod
    @encrypt_handler
    def base85_decode(text: str, encoding: str = 'utf-8') -> str:
        """Base85 Decoding"""
        return base64.b85decode(text).decode(encoding)


class RandomUtil:
    """Random Number Utility Class"""

    @staticmethod
    @encrypt_handler
    def random_bytes(length: int) -> bytes:
        """Generate random bytes of specified length"""
        return get_random_bytes(length)

    @staticmethod
    @encrypt_handler
    def random_str(length: int) -> str:
        """Generate random string of specified length"""
        return base64.b64encode(get_random_bytes(length)).decode()[:length]

    @staticmethod
    @encrypt_handler
    def uuid4() -> str:
        """Generate UUID4"""
        return str(uuid.uuid4())


class EncryptUtil:
    """Encryption Utility Class"""

    # Create static instances
    hash = HashUtil()
    encode = EncodeUtil()
    random = RandomUtil()

    @staticmethod
    def aes() -> Type[AESUtil]:
        """Return AES Utility Class"""
        return AESUtil

    @staticmethod
    def des() -> Type[DESUtil]:
        """Return DES Utility Class"""
        return DESUtil

    @staticmethod
    def des3() -> Type[TripleDESUtil]:
        """Return 3DES Utility Class"""
        return TripleDESUtil

    @staticmethod
    def rsa(public_key: Optional[str] = None,
            private_key: Optional[str] = None) -> RSAUtil:
        """Create RSA Utility Instance"""
        return RSAUtil(public_key, private_key)


# Create default encryption utility instance
encrypt_util = EncryptUtil()
