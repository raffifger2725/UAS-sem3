password1 = input("Masukkan password anda: ")
password2 = input("Masukkan kembali password: ")
if password1 == password2:
    print("Terima Kasih")
elif password1.lower() == password2.lower():
    print("Saya Pasti Bisa")
else:
    print("Sukses Selalu")