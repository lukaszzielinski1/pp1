film={"title":"scott pilgrim vs the world","year":2010,
      "main_actors":["Michael Cera","Mary Elizabeth Winstead"],
      "director":"Edgar Wright","country":"USA"}
import json
f=open("favorite.json","w")
json.dump(film,f,indent=1)
f.close()