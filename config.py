import tokens

# Discord
discord_token   = tokens.discord_token
prefix          = "+"

# Names
coin_name       = "Ryou D-Coins"

# RPG
level_cap       = 9

# RNG
weights         = {"tier_1": [25, 20, 15, 10, 10, 20], # Probability % out of 100 for each capsule respectively. (Must add up to 100 total!)
                   "tier_2": [25, 20, 20, 15, 15, 5],
                   "tier_3": [25, 20, 19, 18, 3, 15],
                   "tier_4": [20, 20, 20, 19, 20, 1]}
weight_mods     = [0, 0.1, 0.9, 1] # Applied respectively according to how many times prize has been rolled. 0 rolled = weight_mods[0], 1 rolled = weight_mods[1], etc.
encouragement   = {"tier_1": [32, 25, 18, 12, 8, 5],
                   "tier_2": [32, 25, 18, 12, 8, 5],
                   "tier_3": [32, 25, 18, 12, 8, 5],
                   "tier_4": [32, 25, 18, 12, 8, 5]}

# Server
ip              = "137.220.33.63"
serve_dir       = "u"

# Permissions
admin_list      = [462763810365898783, 859699653128486912, 629713896747433995, 458993054674583556, 889201372636004432, 343431814347751445, 886841560275234856, 559568144033906708]
admin_role      = "Catheon Core"
wl_role         = "Kamikui (WL)"
og_role         = "OniOG"
gacha_mod_role  = 999762450570285076

# Channels
channels = {
    "roll": [969165756489171001, 1002074803336908860],
    "tavern": [1005908816061288539],
    "quests": [1005915625912279050],
    "dungeons": [1002074803336908860],
    "chat_earn": [969165756237504575, 969165757839728641, 969165757839728640, 969165757613228051, 969165757613228048, 969165757613228049, 969165757613228050, 969165757839728642, 969165757839728643, 969165757839728645, 969165757839728644, 969165757839728646, 969165757839728647, 969165757839728648, 969165757839728649, 981464673184538634, 982197991731515402],
    "exp": [999759477026852955],
    "history": [1005908816061288539, 1005915625912279050, 969165756489171001],
    "craft": [1005908816061288539, 1005915625912279050, 969165756489171001],
    "inv": [1005908816061288539, 1005915625912279050, 969165756489171001],
    "leaderboard": [1005908816061288539, 1005915625912279050, 969165756489171001]
}

# UI
menu_top        = "┌───────────────────────┐"
menu_separator  = "├───────────────────────┤"
menu_bottom     = "└───────────────────────┘"
progressbar     = ["🕛  -=| ──────────────── |=-  🕛",
                   "🕐  -=| ━───────────────  |=-  🕐",
                   "🕑  -=|  ━━──────────────  |=-  🕑",
                   "🕒  -=|  ━━━─────────────  |=-  🕒",
                   "🕓  -=|  ━━━━────────────  |=-  🕓",
                   "🕔  -=|  ━━━━━───────────   |=-  🕔",
                   "🕕  -=|   ━━━━━━──────────   |=-  🕕",
                   "🕖  -=|   ━━━━━━━─────────   |=-  🕖",
                   "🕗  -=|   ━━━━━━━━────────   |=-  🕗",
                   "🕘  -=|   ━━━━━━━━━───────    |=-  🕘",
                   "🕙  -=|    ━━━━━━━━━━──────    |=-  🕙",
                   "🕚  -=|    ━━━━━━━━━━━─────    |=-  🕚",
                   "🕛  -=|    ━━━━━━━━━━━━────    |=-  🕛",
                   "🕐  -=|    ━━━━━━━━━━━━━───     |=-  🕐",
                   "🕑  -=|     ━━━━━━━━━━━━━━──     |=-  🕑",
                   "🕒  -=|     ━━━━━━━━━━━━━━━─     |=-  🕒",
                   "🕓  -=|     ━━━━━━━━━━━━━━━━     |=-  🕓"]
default_color   = 0xfdd835
colors          = [0xe53935, 0xd81b60, 0x8e24aa, 0x5e35b1, 0x3949ab, 0x1e88e5, 0x039be5, 0x00acc1, 0x00897b, 0x43a047, 0x7cb342, 0xc0ca33, 0xfdd835, 0xffb300, 0xfb8c00, 0xf4511e]
capsule_colors  = [0x2196f3, 0x4caf50, 0xef5350, 0xeceff1, 0xffeb3b, 0xd1c4e9]
capsules        = ["blue", "green", "red", "silver", "gold", "platinum"]
numbers         = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "0️⃣"]
# Testing server: custom_emojis   = {"ryou": "<:ryouu1:1004945368460578908>", "ticket": "<:gamaticket:1003394371883892826>", "fragment": "<:GachaTicketReg:1004959178814668881>", "exp": "<:exp:1005561171295879308>", "level": "<:level:1005563309124223067>"}
custom_emojis   = {"ryou": "<:ryouu1:1004945234108629113>", "ticket": "<:gachaticket:1003606286501412895>", "fragment": "<:GachaTicketReg:1004959142458446005>", "exp": "<:exp:1006052726603517954>", "level": "<:level:1006053105420484669>"}

# Conversion rate
conv_rate   = [1000000, 1] # [Ryou, Tickets]

# Intervals (seconds)
quest_wait      = 28800
dungeon_wait    = 43200
chat_earn_wait  = 300

# Ranges
chat_ryou_earn  = [1, 100] # [Min, Max]

# Boosts
role_boosts = {
    "Diamond-Oni": 100,
    "Gold-Oni": 60,
    "Silver-Oni": 40,
    "Oni": 10,
    "Demi-God": 10,
    "Exemplar": 20,
    "OniOG": 15,
    "Oni-Booster": 15
}
