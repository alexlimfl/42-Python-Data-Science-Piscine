from datetime import datetime

start_date = datetime(1970, 1, 1)
end_date = datetime.now()

dur = (end_date - start_date).total_seconds()
formatted_dur = f"{dur:,.4f}"
scientific_dur = f"{dur:.2e}"

print("Seconds since", start_date.strftime("%b %d, %Y")+":",
      formatted_dur, "or", scientific_dur, "in scientific notation")
print(end_date.strftime("%b %d, %Y"))
