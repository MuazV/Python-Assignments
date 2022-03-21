Kullanıcı_name = input("Lütfen İsim giriniz:")


Database = {"Kullanıcı Adı:" : "Muaz"}

if Kullanıcı_name == Database.get("Kullanıcı Adı:"):
    print(f"Hello, {Kullanıcı_name}! The password is:W@12")
else:
    print(f"Hello {Kullanıcı_name}! See you later.")