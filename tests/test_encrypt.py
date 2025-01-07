import unittest

# 导入待测试的模块
from seldom.utils.encrypt import (
    CipherMode,
    HashUtil,
    AESUtil,
    DESUtil,
    TripleDESUtil,
    RSAUtil,
    EncodeUtil,
    RandomUtil,
    EncryptUtil,
    encrypt_util
)


class TestHashUtil(unittest.TestCase):
    """测试 HashUtil 类"""

    def test_md5(self):
        text = "hello world"
        expected = "5eb63bbbe01eeed093cb22bb8f5acdc3"
        self.assertEqual(HashUtil.md5(text), expected)

    def test_sha1(self):
        text = "hello world"
        expected = "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"
        self.assertEqual(HashUtil.sha1(text), expected)

    def test_sha256(self):
        text = "hello world"
        expected = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
        self.assertEqual(HashUtil.sha256(text), expected)

    def test_sha512(self):
        text = "hello world"
        expected = "309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f" \
                   "989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f"
        self.assertEqual(HashUtil.sha512(text), expected)

    def test_hmac_sha256(self):
        key = "secret"
        text = "hello world"
        expected = "734cc62f32841568f45715aeb9f4d7891324e6d948e4c6c60c0621cdac48623a"
        self.assertEqual(HashUtil.hmac_sha256(key, text), expected)


class TestAESUtil(unittest.TestCase):
    """测试 AESUtil 类"""

    def test_encrypt_decrypt_cbc(self):
        key = "mysecretkey"
        text = "hello world"
        encrypted = AESUtil.encrypt(key, text, mode=CipherMode.CBC)
        decrypted = AESUtil.decrypt(key, encrypted, mode=CipherMode.CBC)
        self.assertEqual(decrypted, text)

    def test_encrypt_decrypt_ecb(self):
        key = "mysecretkey"
        text = "hello world"
        encrypted = AESUtil.encrypt(key, text, mode=CipherMode.ECB)
        decrypted = AESUtil.decrypt(key, encrypted, mode=CipherMode.ECB)
        self.assertEqual(decrypted, text)


class TestDESUtil(unittest.TestCase):
    """测试 DESUtil 类"""

    def test_encrypt_decrypt_cbc(self):
        key = "mysecretkey"
        text = "hello world"
        encrypted = DESUtil.encrypt(key, text, mode=CipherMode.CBC)
        decrypted = DESUtil.decrypt(key, encrypted, mode=CipherMode.CBC)
        self.assertEqual(decrypted, text)

    def test_encrypt_decrypt_ecb(self):
        key = "mysecretkey"
        text = "hello world"
        encrypted = DESUtil.encrypt(key, text, mode=CipherMode.ECB)
        decrypted = DESUtil.decrypt(key, encrypted, mode=CipherMode.ECB)
        self.assertEqual(decrypted, text)


class TestTripleDESUtil(unittest.TestCase):
    """测试 TripleDESUtil 类"""

    def test_encrypt_decrypt_cbc(self):
        key = "mysecretkey123456789012"
        text = "hello world"
        encrypted = TripleDESUtil.encrypt(key, text, mode=CipherMode.CBC)
        decrypted = TripleDESUtil.decrypt(key, encrypted, mode=CipherMode.CBC)
        self.assertEqual(decrypted, text)

    def test_encrypt_decrypt_ecb(self):
        key = "mysecretkey123456789012"
        text = "hello world"
        encrypted = TripleDESUtil.encrypt(key, text, mode=CipherMode.ECB)
        decrypted = TripleDESUtil.decrypt(key, encrypted, mode=CipherMode.ECB)
        self.assertEqual(decrypted, text)


class TestRSAUtil(unittest.TestCase):
    """测试 RSAUtil 类"""

    def setUp(self):
        self.public_key, self.private_key = RSAUtil.generate_key_pair()

    def test_encrypt_decrypt(self):
        rsa = RSAUtil(self.public_key, self.private_key)
        text = "hello world"
        encrypted = rsa.encrypt(text)
        decrypted = rsa.decrypt(encrypted)
        self.assertEqual(decrypted, text)


class TestEncodeUtil(unittest.TestCase):
    """测试 EncodeUtil 类"""

    def test_base64_encode_decode(self):
        text = "hello world"
        encoded = EncodeUtil.base64_encode(text)
        decoded = EncodeUtil.base64_decode(encoded)
        self.assertEqual(decoded, text)

    def test_url_encode_decode(self):
        text = "hello world"
        encoded = EncodeUtil.url_encode(text)
        decoded = EncodeUtil.url_decode(encoded)
        self.assertEqual(decoded, text)

    def test_html_encode_decode(self):
        text = "<html>hello world</html>"
        encoded = EncodeUtil.html_encode(text)
        decoded = EncodeUtil.html_decode(encoded)
        self.assertEqual(decoded, text)


class TestRandomUtil(unittest.TestCase):
    """测试 RandomUtil 类"""

    def test_random_bytes(self):
        length = 16
        random_bytes = RandomUtil.random_bytes(length)
        self.assertEqual(len(random_bytes), length)

    def test_random_str(self):
        length = 10
        random_str = RandomUtil.random_str(length)
        self.assertEqual(len(random_str), length)

    def test_uuid4(self):
        uuid_str = RandomUtil.uuid4()
        self.assertEqual(len(uuid_str), 36)


class TestEncryptUtil(unittest.TestCase):
    """测试 EncryptUtil 类"""

    def test_hash_util(self):
        self.assertIsInstance(encrypt_util.hash, HashUtil)

    def test_encode_util(self):
        self.assertIsInstance(encrypt_util.encode, EncodeUtil)

    def test_random_util(self):
        self.assertIsInstance(encrypt_util.random, RandomUtil)

    def test_aes_util(self):
        self.assertEqual(encrypt_util.aes(), AESUtil)

    def test_des_util(self):
        self.assertEqual(encrypt_util.des(), DESUtil)

    def test_des3_util(self):
        self.assertEqual(encrypt_util.des3(), TripleDESUtil)

    def test_rsa_util(self):
        rsa = encrypt_util.rsa()
        self.assertIsInstance(rsa, RSAUtil)


if __name__ == "__main__":
    unittest.main()
