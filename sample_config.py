import os

api_id = 3498045
api_hash = os.environ.get("API_HASH", "229441a8b355de58ba025be657c82ea3")
bot_token = os.environ.get("BOT_TOKEN" "6685547719:AAHRce4N90dhZu-Kx2cJm_KO_wvV_Sdtzco")
auth_users = os.environ.get("AUTH_USERS", "6478217960")
sudo_users = [int(num) for num in auth_users.split("6478217960")]
osowner_users = os.environ.get("OWNER_USERS", "6478217960")
owner_users = [int(num) for num in osowner_users.split(",")]
