from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 6534175982
bot_user = "albranssbot"
api_id = 27114545
api_hash = "4d697dc98a6c882527aab3f72b25479d"
session = "1BJWap1sBu5k4lkQOQNYrqMYcMP4BjYoxVVNCYRkJEDHYoL1RGBg8FZe4Y6NUQ5FIU9yEKHaurZH_4Hdp7dHZLwSqZAfjXtKJI8sP9I9VG9Br3eDgqg2JTvDUK4Qhw4tk5tvPKu5HuxrcRFHIV4HuTEXJ8VP-PmksHBU0Ovn3KblPGzCMnjLXxxPvx5KznXLdBQylMM1G3WWqsxBnISK4j_mV_OBAZHPqimZ7xIf31awjRCEoAYZKOU9Ca0TQmUQ2kmTL93UExDZlKZ6YBeVkYxMWU3uFw4VSlXaOsKR0x3ZetyksUzdgDgDxxYYLvHHjlRu3KfwXrVN8eIHaHl2NTBFRYPIYmQc="
token = "(6195572424:AAEvLKD6uqhhYQObWo5CX11bvb1z5F1EBhY)"
sudo_command = [6534175982, 6534175982]
pm = "6534175982"
mention = "6534175982"
plugins = dict(root="plugins")
app = Client("user:albranssbot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("albranssbot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
