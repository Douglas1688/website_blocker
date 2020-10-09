cadena=['127.0.0.1 www.instagram.com\n', '\n', '127.0.0.1 www.facebook.com\n', '\n', '\n', '127.0.0.1 www.google.com\n', '\n']
redirect="127.0.0.1 "
nueva_cadena = []
for elem in cadena:
    if elem =="\n":
        continue
    else:
        nueva_cadena.append(elem.lstrip(redirect).strip())

print(nueva_cadena)

#print("127.0.0.1 www.facebook.com".lstrip(cadena))