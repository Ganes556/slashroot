linux = ''
for filename in "88ca5e7b2819c56ffc2ab2fc4af49881", "4f4806b0-ab28-49c3-af01-1886c7afc227":
    try:
        value = filename
    except OSError:
        continue

    if value:
        linux += value
        break
print(linux)