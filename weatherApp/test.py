

import numpy as np
import keys
import requests
from matplotlib import pyplot as plt
from io import BytesIO
from PIL import Image

layer = "temp_new"
call = f"https://tile.openweathermap.org/map/{layer}/{0}/{0}/{0}.png?appid={keys.API_KEY}"

data = requests.get(call)
try:
    print(data.json())
except Exception:
    pass
im = BytesIO(data.content)
data = Image.open(im)
array = np.asarray(data)
print(array.shape)
# plt.imshow(data)
# plt.show()