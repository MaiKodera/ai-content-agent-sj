from prompt_loader import build_prompt
from claude_client import generate_text
from discord_sender import send_to_discord

prompt = build_prompt()

response = generate_text(prompt)

send_to_discord(response)