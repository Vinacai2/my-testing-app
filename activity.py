import pypresence
import time

client_id = '1387050760029863996'
RPC = pypresence.Presence(client_id)
RPC.connect()

try:
    RPC.update(
        state="She tied me up",
        details="Leglocked by Jingliu",
        large_image="my_wife_icon",
        large_text="My wife ❤",
        buttons=[
            {"label": "Leak!!?11!?1!1?!!11", "url": "http://vinacai2.free.nf/"}
        ]
    )
    print("Rich Presence updated successfully!")
except Exception as e:
    print(f"Error updating Rich Presence: {e}")

while True:
    time.sleep(15)
