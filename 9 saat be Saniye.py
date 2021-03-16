
print('lotfan be forme moghabel saat ru vared konid: HH:MM:SS')
Saat = input()

t = Saat.split(':')
Saniye = int(t[0])*3600 + int(t[1]) * 60 + int(t[2])
print(Saniye)