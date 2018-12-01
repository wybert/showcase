
import pandas as pd
import json

project_data_dir = "/media/kandy/Elements/work/socialmediaphotostudy/data/"
pic_geo = pd.read_csv(project_data_dir + "processed/pic_geo_bi_samples.csv")
# samples = pic_geo.sample(n=100)
# samples.head()

c_map = {5:"#ff0000",
            4:"#cc00ff",
            3:"#ff9900",
            2:"#ffff00",
            1:"#3c34ff",
            0:"#ccff99"}


jj = []
for k, attr in pic_geo.iterrows():
    # print(k,attr)
    template = {
        "geometry": {
            "type": "Point",
            "coordinates": [
                116.300522,
                39.865687999999999
            ]
        },
        "type": "Feature",
        "properties": {
            "1": False,
            "2": False,
            "3": False,
            "marker-color": "#ff0000",
            "description": "<img width=\"280\" src=\"http://ww2.sinaimg.cn/large/4b1c96dfjw1ei9ncglxwpj20hs0dcmzr.jpg\" /> ",
            "6": False,
            "7": False,
            "8": False,
            "9": False,
            "4": False,
            "5": False,
            "title": "\u4e30\u53f0\u5317\u8def\u4e0e\u6ce5\u6d3c\u8def\u4ea4\u63a5\u8def\u53e3\u5df2\u7ecf\u53d8\u6210\u9732\u5929\u5783\u573e\u573a\u4e86\uff0c\u9a6c\u8def\u4e0a\u548c\u4eba\u884c\u9053\u4e0a\u90fd\u662f\u6cb9\u817b\u817b\u7684\uff0c\u590f\u5929\u4e86\u6076\u81ed\u8086\u610f\u98d8\u6563\u3001\u5df2\u7ecf\u5f88\u957f\u65f6\u95f4\u4e86\uff0c\u6709\u4eba\u7ba1\u4e48\uff1f@\u5317\u4eac\u4ea4\u901a\u5e7f\u64ad @\u5317\u4eac\u65b0\u95fb\u5e7f\u64ad @\u5317\u4eac\u73af\u5883 @\u5317\u4eac\u8def\u653f @\u5317\u4eac\u73af\u4fdd\u5c40  http://t.cn/z8ilSRt",
            "marker-size": "small"
        }
    }

    url = attr["url"]
    image = '''<img width="280" src="%s" />''' % (url)

    template["geometry"]["coordinates"] = [attr["lat"], attr["lon"]]
    template["properties"]["title"] = attr['text_x']
    template["properties"]["description"] = image
    
    for i in range(6):
        if int(attr['label']) == i:
                template["properties"][str(i)] = True 
                template["properties"]["marker-color"] = c_map[i]
    
    
    jj.append(template)

with open("VIS/pic_geo.json", 'w') as f:

    f.write(json.dumps(jj))

