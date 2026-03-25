# <img src="https://play-lh.googleusercontent.com/nvRcbo4P0CNuDvsnZYxtTMPTdIL2TtTlI8j70-5P8UcaGbbHTMHA5iNE397fc5ZEOA=s96-rw" width="28" style="vertical-align:middle;" /> pppoker.py

> Mobile-API for [PPPoker](https://play.google.com/store/apps/details?id=com.lein.pppoker.android) automate and interact with the PPPoker mobile poker platform including authentication, profiles, forum, and game videos.

## Quick Start
```python
from pppoker import PPPoker

pppoker = PPPoker()
pppoker.login(username="your_username", password="your_password")
```

---

## Constructor Options
```python
PPPoker(
    app_id="globle",    # app identifier
    app_type=1,         # app type
    language="ru",      # language code
    platform="android", # platform identifier
    region=2,           # region ID
    country="RU"        # country code
)
```

> On instantiation, `PPPoker` automatically fetches the latest client version — no extra setup needed.

---

## Authentication

| Method | Description |
|--------|-------------|
| `login(username, password, login_type)` | Sign in with credentials |
| `login_as_guest()` | Sign in as a guest |
| `register(username, password)` | Create a new account |
| `get_verification_code(email, valid_type)` | Request email verification code |
| `link_email(email, verification_code)` | Link an email to your account |
| `unlink_email(email, password)` | Unlink email from your account |
| `change_password(new_password, old_password)` | Change account password |

---

## Profile

| Method | Description |
|--------|-------------|
| `edit_profile(country)` | Update profile country |
| `get_portraits()` | Get available profile portraits |
| `change_portrait(icon_name)` | Set a profile portrait |
| `get_user_invite_code()` | Get your invite code |
| `get_user_tasks()` | Get new user tasks |
| `check_username(username)` | Check if a username is available |
| `get_ip_address()` | Get your current IP address |

---

## Forum

| Method | Description |
|--------|-------------|
| `get_forum_featured(recommend_id)` | Get featured forum posts |
| `get_forum_hot(tag_id)` | Get hot forum posts |
| `get_forum_latest(post_id, tag_id)` | Get latest forum posts |
| `get_forum_mine(post_id, tag_id)` | Get your own forum posts |
| `create_forum_post(title, tag_name, invited_user_data)` | Create a new forum post |

---

## Game Videos

| Method | Description |
|--------|-------------|
| `get_user_game_videos(user_id, post_id)` | Get game videos by a user |
| `get_game_video_info(share_key, post_id)` | Get info about a game video |
| `play_game_video(share_key, position)` | Mark a game video as played |
| `comment_game_video(topic_id, content)` | Comment on a game video |
| `like_game_video(topic_id)` | Like a game video |
| `like_comment(topic_id, comment_id)` | Like a comment on a game video |

---

## Notifications

| Method | Description |
|--------|-------------|
| `get_unread_notifications()` | Get unread notification count |
| `get_comment_notifications(message_id)` | Get comment notifications |
| `get_system_notifications(message_id)` | Get system notifications |

---

## Misc

| Method | Description |
|--------|-------------|
| `get_client_version()` | Get latest client version info |
| `get_hand_review_version()` | Get hand review version |
| `get_hand_review()` | Get hand review dictionary |
