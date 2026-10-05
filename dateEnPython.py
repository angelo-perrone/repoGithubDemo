from datetime import datetime

maintenant = datetime.now()

mm = str(maintenant.month)
dd = str(maintenant.day)
yyyy = str(maintenant.year)
heure = str(maintenant.hour)
mi = str(maintenant.minute)
ss = str(maintenant.second)

print("Date en python nous dit : " + mm + "/" + dd + "/" + yyyy + "/" + heure + ":" + mi + ":" + ss)
