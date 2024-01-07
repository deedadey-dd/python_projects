cookie_number = "11,000,0 cookies"
cookies_info = cookie_number.replace(',', '')
cookies_string = cookies_info.split('\n')[0].split()[0]
cookies = int(cookies_string)
print(cookies)

print(type(cookies))
