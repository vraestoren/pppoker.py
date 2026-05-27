from hashlib import md5
from random import randint
from base64 import b64encode
from datetime import datetime, timedelta, timezone

DELTA = 0x9E3779B9
DEFAULT_SUFFIX = "d5659066d5"


def _imei() -> str:
	return md5(
		str(randint(0, 999999999)).encode()).hexdigest()


def to_uint32_array(data: bytes, include_len: bool) -> list:
	word_count = (len(data) + 3) // 4
	words = [0] * (word_count + (1 if include_len else 0))
	for byte_index, byte in enumerate(data):
		words[byte_index >> 2] |= byte << ((byte_index & 3) << 3)
	if include_len:
		words[word_count] = len(data)
	return words

def to_bytes(words, include_len: bool) -> bytes:
	byte_count = len(words) << 2
	if include_len:
		original_len = words[-1]
		if original_len < byte_count - 7 or original_len > byte_count - 4:
			return
		byte_count = original_len
		words = words[:-1]

	out = bytearray()
	for word in words:
		out += (word & 0xFFFFFFFF).to_bytes(4, "little")
	return bytes(out[:byte_count])

def fix_key(key: bytes):
	return (to_uint32_array(key, False) + [0, 0, 0, 0])[:4]

def xxtea_encrypt(data: bytes, key: bytes) -> bytes:
	if not data:
		return data

	total = 0
	key_words = fix_key(key)
	data_words = to_uint32_array(data, True)
	last_index = len(data_words) - 1
	previous_word = data_words[last_index]
	rounds = 6 + 52 // (last_index + 1)
	while rounds > 0:
		rounds -= 1
		total = (total + DELTA) & 0xFFFFFFFF
		key_selector = (total >> 2) & 3
		for word_index in range(last_index):
			next_word = data_words[word_index + 1]
			mixed = (
				(((previous_word >> 5) ^ (next_word << 2))
				+ ((next_word >> 3) ^ (previous_word << 4)))
				^ ((total ^ next_word)
				+ (key_words[(word_index & 3) ^ key_selector] ^ previous_word))
			) & 0xFFFFFFFF
			data_words[word_index] = (data_words[word_index] + mixed) & 0xFFFFFFFF
			previous_word = data_words[word_index]

		next_word = data_words[0]
		mixed = (
			(((previous_word >> 5) ^ (next_word << 2))
			+ ((next_word >> 3) ^ (previous_word << 4)))
			^ ((total ^ next_word)
			+ (key_words[(last_index & 3) ^ key_selector] ^ previous_word))
		) & 0xFFFFFFFF
		data_words[last_index] = (data_words[last_index] + mixed) & 0xFFFFFFFF
		previous_word = data_words[last_index]
	return to_bytes(data_words, False)

def crypto_password_v2(password: str) -> str:
	first_md5 = md5(password.encode("utf-8")).hexdigest()
	return md5(first_md5.encode("utf-8")).hexdigest()

def http_key(
		timestamp: int, suffix: str = DEFAULT_SUFFIX, tz_hours: int = 8) -> str:
	request_time = datetime.fromtimestamp(timestamp, timezone.utc)
	target_time = request_time + timedelta(hours=tz_hours)
	return (
		f"{target_time.month:02d}"
		f"{target_time.day:02d}"
		f"{target_time.hour:02d}"
		f"{target_time.minute:02d}"
		f"{target_time.second:02d}"
		f"{suffix}"
	)

def encode_password(password: str, timestamp: int) -> str:
	double_md5 = crypto_password_v2(password)
	key = http_key(timestamp)
	encrypted = xxtea_encrypt(
		double_md5.encode("utf-8"), key.encode("utf-8"))
	return b64encode(encrypted).decode("ascii")
