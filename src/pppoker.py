from time import time
from uuid import uuid4
from hashlib import md5
from random import randint
from requests import Session

class PPPoker:
    def __init__(
            self,
            app_id: str = "globle", 
            app_type: int = 1,
            language: str = "ru",
            platform: str = "android",
            region: int = 2,
            country: str = "RU") -> None:
        self.public_api = "http://www.pppoker.club"
        self.api = "https://api.pppoker.club"
        self.bbs_api = "http://bbs.pppoker.net"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; RMX3551 Build/PQ3A.190705.003)"
        }
        self.rd_key = None
        self.user_id = None
        self.app_id = app_id
        self.region = region
        self.country = country
        self.app_type = app_type
        self.language = language
        self.platform = platform
        self.imei = self.generate_imei()
        self.version = self.get_client_version()["latest_version"]

    def md5_hash(self, string: str) -> str:
        return md5(md5(string.encode()).hexdigest().encode()).hexdigest()

    def generate_imei(self) -> int:
        return randint(1000_0000_0000_000, 9000_0000_0000_000)

    def get_client_version(self) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/version.php").json()

    def login(
            self, 
            username: str, 
            password: str, 
            type: int = 4) -> dict:
        data = {
            "app_type": self.app_type,
            "appid": self.app_id,
            "apple_full_name": "nil",
            "apple_identity_token": "nil",
            "apple_user": "nil",
            "clientvar": self.version,
            "country": self.country,
            "distributor": 0,
            "imei": self.imei,
            "lang": self.language,
            "languagecode": self.language,
            "operating_company": self.platform,
            "os": self.platform,
            "password": self.md5_hash(password),
            "platform_type": 2,
            "region": self.region,
            "sub_distributor": 0,
            "type": type,
            "username": username
        }
        response = self.session.post(
            f"{self.public_api}/poker/api/login.php",  data=data).json()
        if "uid" in response:
            self.user_id = response["uid"]
            self.rd_key = response["rdkey"]
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
            "type": 1,
        }
        response = self.session.post(
            f"{self.public_api}/poker/api/login.php", 
            data=data).json()
        if "uid" in response:
            self.user_id = response["uid"]
            self.rd_key = response["rdkey"]
        return response

    def register(
            self,
            username: str,
            password: str) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/register.php?username={username}&password={self.md5_hash(password)}&distributor=0&sub_distributor=0&country={self.country}&appid={self.app_id}&os={self.platform}&imei={self.imei}&clientvar={self.version}&ad_id={uuid4()}&region={self.region}&app_type={self.app_type}").json()

    def get_verification_code(self, email: str, valid_type: int = 1) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/mail/send_valid_code.php?mail={email}&valid_type={valid_type}&lang={self.language}").json()

    def edit_profile(self, country: str) -> dict:
        data = {
            "country": country,
            "rdkey": self.rd_key,
            "uid": self.user_id
        }
        return self.session.post(
            f"{self.public_api}/poker/api/modify_userinfo.php",
            data=data).json()

    def get_portraits(self) -> dict:
        return self.session.get(
            f"{self.public_api}/poker-api/portrait/list?uid={self.user_id}&rdkey={self.rd_key}").json()

    def change_portrait(self, icon_name: str) -> dict:
        data = {
            "icon_name": icon_name,
            "rdkey": self.rd_key,
            "uid": self.user_id
        }
        return self.session.post(
            f"{self.public_api}/poker-api/portrait/choice",
            data=data).json()

    def get_user_invite_code(self) -> dict:
        return self.session.get(
            f"{self.public_api}/server_api/user_invite/code?uid={self.user_id}&rdkey={self.rd_key}").json()

    def get_user_tasks(self) -> dict:
        return self.session.get(
            f"{self.public_api}/server_api/new_user_task/tasks?uid={self.user_id}&rdkey={self.rd_key}").json()

    def link_email(
            self,
            email: str,
            verification_code: int) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/mail/valid_mail.php?mail={email}&valid_code={verification_code}&rdkey={self.rd_key}&uid={self.user_id}").json()

    def unlink_email(
            self,
            email: str,
            password: str) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/mail/unlink_mail.php?mail={email}&password={self.md5_hash(password)}&uid={self.user_id}").json()

    def change_password(
            self,
            new_password: str,
            old_password: str) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/mail/change_pw.php?uid={self.user_id}&password={self.md5_hash(new_password)}&old_password={self.md5_hash(old_password)}").json()

    def get_ip_address(self) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/getip.php").json()

    def check_username(self, username: str) -> dict:
        return self.session.get(
            f"{self.public_api}/poker/api/check_username.php?username={username}").json()

    def get_hand_review_version(self) -> dict:
        return self.session.post(
            f"{self.api}/poker/api/hand_review_version.php").json()

    def get_hand_review(self) -> dict:
        return self.session.get(
            f"{self.api}/poker/api/handreview/dict.json").json()

    def get_forum_featured(self, recommend_id: int = 0) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/game_video/recommend_list?uid={self.user_id}&rdkey={self.rd_key}&lang={self.language}&recommend_id={recommend_id}&updated_at={int(time() * 1000)}").json()

    def get_forum_hot(self, tag_id: int = 0) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/game_video/hot_list?uid={self.user_id}&rdkey={self.rd_key}&updated_at={int(time() * 1000)}&tag_id={tag_id}").json()

    def get_forum_latest(
            self,
            post_id: int = 0,
            tag_id: int = 0) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/game_video/newest_list?rdkey={self.rd_key}&uid={self.user_id}&post_id={post_id}&updated_at={int(time() * 1000)}&tag_id={tag_id}").json()

    def get_forum_mine(
            self,
            post_id: int = 0,
            tag_id: int = 0) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/game_video/personal_list?rdkey={self.rd_key}&uid={self.user_id}&post_id={post_id}&updated_at={int(time() * 1000)}&personal_uid={self.user_id}&tag_id={tag_id}").json()

    def get_user_game_videos(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/game_video/personal_list?rdkey={self.rd_key}&uid={self.user_id}&post_id={post_id}&updated_at={int(time() * 1000)}&personal_uid={user_id}").json()

    def get_game_video_info(
            self,
            share_key: str,
            post_id: int = -1) -> dict:
        data = {
            "user_id": self.user_id,
            "post_id": post_id,
            "share_key": share_key,
            "lang": self.language
        }
        return self.session.post(
            f"{self.bbs_api}/api/game_video/info",
            data=data).json()

    def play_game_video(
            self,
            share_key: str,
            position: int) -> dict:
        data = {
            "share_key": share_key,
            "uid": self.user_id,
            "rdkey": self.rd_key,
            "position": position
        }
        return self.session.post(
            f"{self.bbs_api}/api/game_video/play", data=data).json()

    def comment_game_video(
            self,
            topic_id: int,
            content: str) -> dict:
        data = {
            "user_id": self.user_id,
            "content": content,
            "topic_id": topic_id,
            "share_type": -1,
            "share_platform": -1
        }
        return self.session.post(
            f"{self.bbs_api}/api/game_video/submit_comment",
            data=data).json()

    def like_game_video(self, topic_id: int) -> dict:
        data = {
            "comment_id": 0,
            "user_id": self.user_id,
            "topic_id": topic_id,
            "share_type": -1,
            "share_platform": -1
        }
        return self.session.post(
            f"{self.bbs_api}/api/game_video/like",
            data=data).json()

    def like_comment(
            self,
            topic_id: int,
            comment_id: int) -> dict:
        data = {
            "comment_id": comment_id,
            "user_id": self.user_id,
            "topic_id": topic_id,
            "share_type": -1,
            "share_platform": -1
        }
        return self.session.post(
            f"{self.bbs_api}/api/game_video/like",
            data=data).json()

    def get_unread_notifications(self) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/notification/unread?uid={self.user_id}&rdkey={self.rd_key}").json()

    def get_comment_notifications(
            self,
            message_id: int = 0) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/notification/comment_msg_list?uid={self.user_id}&rdkey={self.rd_key}&msg_id={message_id}").json()

    def get_system_notifications(
            self,
            message_id: int = 0) -> dict:
        return self.session.get(
            f"{self.bbs_api}/api/notification/system_msg_list?uid={self.user_id}&rdkey={self.rd_key}&msg_id={message_id}").json()

    def create_forum_post(
            self,
            title: str,
            tag_name: str = None,
            invited_user_data: list = []) -> dict:
        data = {
            "uid": self.user_id,
            "rdkey": self.rd_key,
            "title": title,
            "invited_user_data": invited_user_data
        }
        if tag_name:
            data["tag_name"] = tag_name
        return self.session.post(
            f"{self.bbs_api}/api/game_video/submit_post", data=data).json()
