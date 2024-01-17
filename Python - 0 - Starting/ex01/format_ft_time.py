from datetime import datetime

now = datetime.now()
current_timestamp = datetime.timestamp(now)

print(f"Second since January 1, 1970: \
      {current_timestamp:,.4f} or {current_timestamp:.2e} \
        in scientific notation")
print(f"{now.strftime('%b %d %Y')}")
