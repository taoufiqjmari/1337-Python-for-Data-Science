from datetime import datetime

now = datetime.now()
ts = datetime.timestamp(now)

print(f"Second since January 1, 1970: {ts:,.4f} ", end="")
print(f"or {ts:.2e} in scientific notation")
print(f"{now.strftime('%b %d %Y')}")
