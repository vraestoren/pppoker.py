import utils
from time import time
from uuid import uuid4
from random import randint
from requests import Session


class PPPoker:
	def __init__(
			self,
			imei: str = None,
			app_id: str = "globle",
			app_type: int = 1,
			language: str = "ru",
			platform: str = "android",
			region: int = 2,
			country: str = "RU") -> None:
		self.api = "https://api.pppoker.club"
		self.login_api = "https://www.cozypoker.net"
		self.public_api = "http://www.pppoker.club"
		self.bbs_api = "http://bbs.pppoker.net"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "UnityPlayer/2022.3.62f3 (UnityWebRequest/1.0, libcurl/8.10.1-DEV)",
			"X-Unity-Version": "2022.3.62f3",
			"Accept": "*/*",
			"Accept-Encoding": "deflate, gzip"}
		self.rd_key = None
		self.user_id = None
		self.app_id = app_id
		self.region = region
		self.country = country
		self.app_type = app_type
		self.language = language
		self.platform = platform
		self.imei = utils._imei() if not imei else imei
		self.version = "4.2.116"

	def _post(
			self, base: str, endpoint: str, data: dict = None) -> dict:
		return self.session.post(f"{base}{endpoint}", data=data).json()

	def _get(
			self, base: str, endpoint: str, params: dict = None) -> dict:
		return self.session.get(
			f"{base}{endpoint}",
			params=params or {}).json()

	def get_client_version(self) -> dict:
		return self._get(self.public_api, "/poker/api/version.php")

	def login(
			self,
			username: str,
			password: str,
			login_type: int = 4) -> dict:
		timestamp = int(time())
		data = {
			"type": login_type,
			"region": self.region,
			"username": username,
			"password": utils.encode_password(password, timestamp),
			"t": str(timestamp),
			"os": self.platform,
			"distributor": 0,
			"country": self.country,
			"appid": self.app_id,
			"clientvar": self.version,
			"imei": self.imei,
			"platform_type": 2,
			"lang": self.language,
			"languagecode": self.language,
			"app_build_code": "223",
			"operating_company": self.platform,
			"app_type": self.app_type
		}
		response = self._post(self.login_api, "/poker/api/login.php", data)
		if "uid" in response:
			try:
				self.user_id = response["uid"]
				self.rd_key = response["rdkey"]
			except BaseException:
				pass
		return response

	def login_as_guest(self) -> dict:
		data = {
			"ad_id": str(uuid4()),
			"app_type": self.app_type,
			"appid": self.app_id,
			"apple_full_name": "nil",
			"apple_identity_token": "nil",
			"apple_user": "nil",
			"clientvar": self.version,
			"code": self.imei,
			"country": self.country,
			"distributor": 0,
			"imei": self.imei,
			"lang": self.language,
			"languagecode": self.language,
			"operating_company": self.platform,
			"os": self.platform,
			"platform_type": 2,
			"region": self.region,
			"sub_distributor": 0,
			"type": 1
		}
		response = self._post(self.public_api, "/poker/api/login.php", data)
		if "uid" in response:
			self.user_id = response["uid"]
			self.rd_key = response["rdkey"]
		return response

	def register(self, username: str, password: str) -> dict:
		params = {
			"username": username,
			"password": self.md5_hash(password),
			"distributor": 0,
			"sub_distributor": 0,
			"country": self.country,
			"appid": self.app_id,
			"os": self.platform,
			"imei": self.imei,
			"clientvar": self.version,
			"adid": str(uuid4()),
			"region": self.region,
			"app_type": self.app_type
		}
		return self._get(self.public_api, "/poker/api/register.php", params)

	def get_reset_code(self, email: str, valid_type: int = 2) -> dict:
		params = {
			"mail": email,
			"valid_type": valid_type,
			"lang": self.language}
		return self._get(
			self.login_api,
			"/poker/api/mail/send_valid_code.php",
			params)

	def get_email_code(self, uid: str) -> dict:
		data = {
			"uid": uid,
			"imei": self.imei,
			"lang": self.language
		}
		return self._post(self.login_api, "/poker-api/device/code", data)

	def verify_email_code(self, uid: str, code: str) -> dict:
		data = {
			"uid": uid,
			"code": code,
			"imei": self.imei,
			"lang": self.language
		}
		return self._post(self.login_api, "/poker-api/device/data", data)

	def edit_profile(self, country: str) -> dict:
		data = {"country": country, "rdkey": self.rd_key, "uid": self.user_id}
		return self._post(
			self.public_api,
			"/poker/api/modify_userinfo.php",
			data)

	def get_portraits(self) -> dict:
		params = {"uid": self.user_id, "rdkey": self.rd_key}
		return self._get(self.public_api, "/poker-api/portrait/list", params)

	def change_portrait(self, icon_name: str) -> dict:
		data = {
			"icon_name": icon_name,
			"rdkey": self.rd_key,
			"uid": self.user_id}
		return self._post(self.public_api, "/poker-api/portrait/choice", data)

	def get_user_invite_code(self) -> dict:
		params = {"uid": self.user_id, "rdkey": self.rd_key}
		return self._get(
			self.public_api,
			"/server_api/user_invite/code",
			params)

	def get_user_tasks(self) -> dict:
		params = {"uid": self.user_id, "rdkey": self.rd_key}
		return self._get(
			self.public_api,
			"/server_api/new_user_task/tasks",
			params)

	def link_email(self, email: str, code: int) -> dict:
		params = {
			"mail": email,
			"valid_code": code,
			"uid": self.user_id,
			"rdkey": self.rd_key}
		return self._get(
			self.public_api,
			"/poker/api/mail/valid_mail.php",
			params)

	def unlink_email(self, email: str, password: str) -> dict:
		params = {
			"mail": email,
			"password": self.md5_hash(password),
			"uid": self.user_id}
		return self._get(
			self.public_api,
			"/poker/api/mail/unlink_mail.php",
			params)

	def change_password(self, new_password: str, old_password: str) -> dict:
		params = {
			"old_password": self.md5_hash(old_password),
			"password": self.md5_hash(new_password),
			"uid": self.user_id}
		return self._get(
			self.public_api,
			"/poker/api/mail/change_pw.php",
			params)

	def get_ip_address(self) -> dict:
		return self._get(self.public_api, "/poker/api/getip.php")

	def check_username(self, username: str) -> dict:
		params = {"username": username}
		return self._get(
			self.public_api,
			"/poker/api/check_username.php",
			params)

	def get_hand_review_version(self) -> dict:
		return self._post(self.api, "/poker/api/hand_review_version.php")

	def get_hand_review(self) -> dict:
		return self._get(self.api, "/poker/api/handreview/dict.json")

	def get_forum_featured(self, recommend_id: int = 0) -> dict:
		params = {
			"uid": self.user_id,
			"rdkey": self.rd_key,
			"lang": self.language,
			"recommend_id": recommend_id,
			"updated_at": int(
				time() * 1000)}
		return self._get(
			self.bbs_api,
			"/api/game_video/recommend_list",
			params)

	def get_forum_hot(self, tag_id: int = 0) -> dict:
		params = {
			"uid": self.user_id,
			"rdkey": self.rd_key,
			"updated_at": int(
				time() * 1000),
			"tag_id": tag_id}
		return self._get(self.bbs_api, "/api/game_video/hot_list", params)

	def get_forum_latest(self, post_id: int = 0, tag_id: int = 0) -> dict:
		params = {
			"uid": self.user_id,
			"post_id": post_id,
			"rdkey": self.rd_key,
			"updated_at": int(
				time() * 1000),
			"tag_id": tag_id}
		return self._get(self.bbs_api, "/api/game_video/newest_list", params)

	def get_forum_mine(self, post_id: int = 0, tag_id: int = 0) -> dict:
		params = {
			"uid": self.user_id,
			"post_id": post_id,
			"rdkey": self.rd_key,
			"updated_at": int(
				time() * 1000),
			"tag_id": tag_id,
			"personal_uid": self.user_id}
		return self._get(self.bbs_api, "/api/game_video/personal_list", params)

	def get_user_game_videos(self, user_id: int, post_id: int = 0) -> dict:
		params = {
			"uid": self.user_id,
			"post_id": post_id,
			"rdkey": self.rd_key,
			"updated_at": int(
				time() * 1000),
			"personal_uid": self.user_id}
		return self._get(self.bbs_api, "/api/game_video/personal_list", params)

	def get_game_video_info(self, share_key: str, post_id: int = -1) -> dict:
		data = {
			"user_id": self.user_id,
			"post_id": post_id,
			"share_key": share_key,
			"lang": self.language}
		return self._post(self.bbs_api, "/api/game_video/info", data)

	def play_game_video(self, share_key: str, position: int) -> dict:
		data = {
			"share_key": share_key,
			"uid": self.user_id,
			"rdkey": self.rd_key,
			"position": position}
		return self._post(self.bbs_api, "/api/game_video/play", data)

	def comment_game_video(self, topic_id: int, content: str) -> dict:
		data = {
			"user_id": self.user_id,
			"content": content,
			"topic_id": topic_id,
			"share_type": -1,
			"share_platform": -1}
		return self._post(self.bbs_api, "/api/game_video/submit_comment", data)

	def like_game_video(self, topic_id: int) -> dict:
		data = {
			"comment_id": 0,
			"user_id": self.user_id,
			"topic_id": topic_id,
			"share_type": -1,
			"share_platform": -1}
		return self._post(self.bbs_api, "/api/game_video/like", data)

	def like_comment(self, topic_id: int, comment_id: int) -> dict:
		data = {
			"comment_id": comment_id,
			"user_id": self.user_id,
			"topic_id": topic_id,
			"share_type": -1,
			"share_platform": -1}
		return self._post(self.bbs_api, "/api/game_video/like", data)

	def get_unread_notifications(self) -> dict:
		params = {"uid": self.user_id, "rdkey": self.rd_key}
		return self._get(self.bbs_api, "/api/notification/unread", params)

	def get_comment_notifications(self, message_id: int = 0) -> dict:
		params = {
			"uid": self.user_id,
			"rdkey": self.rd_key,
			"msg_id": message_id}
		return self._get(
			self.bbs_api,
			"/api/notification/comment_msg_list",
			params)

	def get_system_notifications(self, message_id: int = 0) -> dict:
		params = {
			"uid": self.user_id,
			"rdkey": self.rd_key,
			"msg_id": message_id}
		return self._get(
			self.bbs_api,
			"/api/notification/system_msg_list",
			params)

	def create_forum_post(
			self,
			title: str,
			tag_name: str = None,
			invited_user_data: list = []) -> dict:
		data = {
			"uid": self.user_id,
			"rdkey": self.rd_key,
			"title": title,
			"invited_user_data": invited_user_data}
		if tag_name:
			data["tag_name"] = tag_name
		return self._post(
			self.bbs_api, "/api/game_video/submit_post", data)
