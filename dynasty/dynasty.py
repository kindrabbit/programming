#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 朝代数据模型

country = {
    "name": "",
    "start_year": 0,
    "end_year": 0,
    "creator": "",
    "dynasty": "",
    "area": "",
    "capital": ""
}

# 朝代原始数据列表
china_countries = [
    {
        "name": "夏",
        "start_year": -2070,
        "end_year": -1600,
        "creator": "禹",
        "dynasty": "夏",
        "area": "山西",
        "capital": "安邑"
    },
    {
        "name": "商",
        "start_year": -1600,
        "end_year": -1046,
        "creator": "汤",
        "dynasty": "商",
        "area": "河南",
        "capital": "亳"
    },
    {
        "name": "西周",
        "start_year": -1046,
        "end_year": -771,
        "creator": "周文王姬发",
        "dynasty": "周",
        "area": "陕西",
        "capital": "镐京"
    },
    {
        "name": "东周",
        "start_year": -770,
        "end_year": -256,
        "creator": "周平王姬宜臼",
        "dynasty": "周",
        "area": "河南",
        "capital": "洛邑"
    },
    {
        "name": "春秋",
        "start_year": -770,
        "end_year": -476,
        "creator": "周平王姬宜臼",
        "dynasty": "周",
        "area": "河南",
        "capital": "洛邑"
    },
    {
        "name": "战国",
        "start_year": -475,
        "end_year": -221,
        "creator": "周平王姬宜臼",
        "dynasty": "周",
        "area": "河南",
        "capital": "洛邑"
    },
    {
        "name": "秦",
        "start_year": -221,
        "end_year": -207,
        "creator": "始皇帝嬴政",
        "dynasty": "秦",
        "area": "陕西",
        "capital": "咸阳"
    },
    {
        "name": "西汉",
        "start_year": -206,
        "end_year": 8,
        "creator": "汉高祖刘邦",
        "dynasty": "汉",
        "area": "陕西",
        "capital": "长安"
    },
    {
        "name": "新",
        "start_year": 9,
        "end_year": 23,
        "creator": "王莽",
        "dynasty": "汉",
        "area": "陕西",
        "capital": "长安"
    },
    {
        "name": "东汉",
        "start_year": 25,
        "end_year": 220,
        "creator": "汉光武帝刘秀",
        "dynasty": "汉",
        "area": "河南",
        "capital": "洛阳"
    },
    {
        "name": "魏",
        "start_year": 220,
        "end_year": 265,
        "creator": "魏文帝曹丕",
        "dynasty": "三国",
        "area": "河南",
        "capital": "洛阳"
    },
    {
        "name": "蜀汉",
        "start_year": 221,
        "end_year": 263,
        "creator": "汉昭烈帝刘备",
        "dynasty": "三国",
        "area": "四川",
        "capital": "成都"
    },
    {
        "name": "吴",
        "start_year": 222,
        "end_year": 280,
        "creator": "吴大帝孙权",
        "dynasty": "三国",
        "area": "江苏",
        "capital": "建业"
    },
    {
        "name": "西晋",
        "start_year": 265,
        "end_year": 316,
        "creator": "晋武帝司马炎",
        "dynasty": "晋",
        "area": "河南",
        "capital": "洛阳"
    },
    {
        "name": "东晋",
        "start_year": 317,
        "end_year": 420,
        "creator": "晋元帝司马睿",
        "dynasty": "晋",
        "area": "江苏",
        "capital": "建康"
    },
    {
        "name": "宋",
        "start_year": 420,
        "end_year": 479,
        "creator": "宋武帝刘裕",
        "dynasty": "南朝",
        "area": "江苏",
        "capital": "建康"
    },
    {
        "name": "齐",
        "start_year": 479,
        "end_year": 502,
        "creator": "齐高帝萧道成",
        "dynasty": "南朝",
        "area": "江苏",
        "capital": "建康"
    },
    {
        "name": "梁",
        "start_year": 502,
        "end_year": 557,
        "creator": "梁武帝萧衍",
        "dynasty": "南朝",
        "area": "江苏",
        "capital": "建康"
    },
    {
        "name": "陈",
        "start_year": 557,
        "end_year": 589,
        "creator": "陈武帝陈霸先",
        "dynasty": "南朝",
        "area": "江苏",
        "capital": "建康"
    },
    {
        "name": "北魏",
        "start_year": 386,
        "end_year": 534,
        "creator": "魏道武帝拓跋珪",
        "dynasty": "北朝",
        "area": "山西",
        "capital": "平城"
    },
    {
        "name": "东魏",
        "start_year": 534,
        "end_year": 550,
        "creator": "魏孝静帝元善见",
        "dynasty": "北朝",
        "area": "河北",
        "capital": "邺"
    },
    {
        "name": "西魏",
        "start_year": 535,
        "end_year": 556,
        "creator": "魏文帝元宝炬",
        "dynasty": "北朝",
        "area": "陕西",
        "capital": "长安"
    },
    {
        "name": "北齐",
        "start_year": 550,
        "end_year": 577,
        "creator": "齐文宣帝高洋",
        "dynasty": "北朝",
        "area": "河北",
        "capital": "邺"
    },
    {
        "name": "北周",
        "start_year": 557,
        "end_year": 581,
        "creator": "周孝闵帝宇文觉",
        "dynasty": "北朝",
        "area": "陕西",
        "capital": "长安"
    },
    {
        "name": "隋",
        "start_year": 581,
        "end_year": 618,
        "creator": "隋文帝杨坚",
        "dynasty": "隋",
        "area": "陕西",
        "capital": "大兴"
    },
    {
        "name": "唐",
        "start_year": 618,
        "end_year": 907,
        "creator": "唐高祖李渊",
        "dynasty": "唐",
        "area": "陕西",
        "capital": "长安"
    },
    {
        "name": "后梁",
        "start_year": 907,
        "end_year": 923,
        "creator": "梁太祖朱晃",
        "dynasty": "五代十国",
        "area": "河南",
        "capital": "汴"
    },
    {
        "name": "后唐",
        "start_year": 923,
        "end_year": 936,
        "creator": "唐庄宗李存勖",
        "dynasty": "五代十国",
        "area": "河南",
        "capital": "洛阳"
    },
    {
        "name": "后晋",
        "start_year": 936,
        "end_year": 947,
        "creator": "晋高祖石敬瑭",
        "dynasty": "五代十国",
        "area": "河南",
        "capital": "汴"
    },
    {
        "name": "后汉",
        "start_year": 947,
        "end_year": 950,
        "creator": "汉高祖刘暠",
        "dynasty": "五代十国",
        "area": "河南",
        "capital": "汴"
    },
    {
        "name": "后周",
        "start_year": 951,
        "end_year": 960,
        "creator": "周太祖郭威",
        "dynasty": "五代十国",
        "area": "河南",
        "capital": "汴"
    },
    {
        "name": "南吴",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "南唐",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "吴越",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "前蜀",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "后蜀",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "北汉",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "荆楚",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "南汉",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "南平",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "闵国",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "桀燕",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "岐国",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "赵国",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "北平国",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "殷国",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "武平军节度使",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "清源军节度使",
        "start_year": 902,
        "end_year": 979,
        "creator": "...",
        "dynasty": "五代十国",
        "area": "...",
        "capital": "..."
    },
    {
        "name": "北宋",
        "start_year": 960,
        "end_year": 1127,
        "creator": "宋太祖赵匡胤",
        "dynasty": "宋",
        "area": "河南",
        "capital": "开封"
    },
    {
        "name": "南宋",
        "start_year": 1127,
        "end_year": 1279,
        "creator": "宋高宗赵构",
        "dynasty": "宋",
        "area": "浙江",
        "capital": "临安"
    },
    {
        "name": "辽",
        "start_year": 907,
        "end_year": 1125,
        "creator": "辽太祖耶律阿保机",
        "dynasty": "辽",
        "area": "辽宁",
        "capital": "皇都"
    },
    {
        "name": "大理",
        "start_year": 937,
        "end_year": 1254,
        "creator": "太祖段思平",
        "dynasty": "大理",
        "area": "云南",
        "capital": "太和城"
    },
    {
        "name": "西夏",
        "start_year": 1032,
        "end_year": 1227,
        "creator": "景宗李元昊",
        "dynasty": "西夏",
        "area": "云南",
        "capital": "兴庆府"
    },
    {
        "name": "金",
        "start_year": 1115,
        "end_year": 1234,
        "creator": "金太祖阿骨打",
        "dynasty": "金",
        "area": "阿城",
        "capital": "会宁"
    },
    {
        "name": "元",
        "start_year": 1206,
        "end_year": 1368,
        "creator": "元世祖忽必烈",
        "dynasty": "元",
        "area": "北京",
        "capital": "大都"
    },
    {
        "name": "明",
        "start_year": 1368,
        "end_year": 1644,
        "creator": "明太祖朱元璋",
        "dynasty": "明",
        "area": "北京",
        "capital": "北京"
    },
    {
        "name": "清",
        "start_year": 1616,
        "end_year": 1911,
        "creator": "清太宗皇太极",
        "dynasty": "清",
        "area": "北京",
        "capital": "北京"
    },

]


class Dynasty:
    data = []

    # 表格打印
    def print_dynasty(self):
        # 表头
        # print("%s %16s %10s %10s %10s %10s" % ("国家", "开始时间", "结束时间", "存在时长", "开国皇帝", "首都", "地区"))
        print("{0:<15}\t{1:<20}\t{2:<15}\t{3:<30}\t{4:<15}\t{5:<15}"
              .format("国家", "开始时间", "结束时间", "存在时长", "开国皇帝", "首都", "地区"))
        # 打印内容
        for item in self.data:

            name = item.get("name")

            start_year = item.get("start_year")
            start_year_text = None
            if start_year > 0:
                start_year_text = "公元" + str(start_year)
            else:
                start_year_text = "公元前" + str(-start_year)

            duration = item.get("end_year") - item.get("start_year")

            end_year = item.get("end_year")
            creator = item.get("creator")
            capital = item.get("capital")
            area = item.get("area")

            print("{0:<15}\t{1:<20}\t{2:<15}\t{3:<30}\t{4:<15}\t{5:<15}\t{6:<15}"
                  .format(name, start_year_text + "年", str(end_year) + "年", str(duration) + "年", creator, capital, area))

    # 打印所有国家的都城
    def print_country_capital(self):
        for country in self.data:
            if country.get("capital") != "...":
                print(country.get("capital"), country.get("area"), country.get("creator"))

    # 打印时间最短的国家
    def print_shortest_dynasty(self):
        shortest_country = self.data[0]
        shortest = shortest_country.get("end_year") -shortest_country.get("start_year")
        for country in self.data:
            if (country.get("end_year") - country.get("start_year")) < shortest:
                shortest_country = country
                shortest = country.get("end_year") - country.get("start_year")

        print(shortest_country.get("name"), str(shortest) + "年")

    def print_longest_dynasty(self):
        longest_country = self.data[0]
        longest = longest_country.get("end_year") - longest_country.get("start_year")
        for country in self.data:
            if (country.get("end_year") - country.get("start_year")) > longest:
                longest_country = country
                longest = country.get("end_year") - country.get("start_year")

        print(longest_country.get("name"), str(longest) + "年")


    # 打印时间最短的几个国家，num是数量
    def print_short_dynasty(self, num = 5):
        data = self.data[:]
        short_country_list = []
        if num > len(data):
            num = len(data)

        while len(short_country_list) < num:
            shortest_country = data[0]
            shortest = shortest_country.get("end_year") - shortest_country.get("start_year")
            shortest_country_index = 0
            for index in range(len(data)):
                country = data[index]
                # 把存续时间最短的国家下标找出来
                if (country.get("end_year") - country.get("start_year")) < shortest:
                    shortest_country_index = index
                    shortest_country = data[shortest_country_index]
                    shortest = shortest_country.get("end_year") - shortest_country.get("start_year")
            # # 把最短的国家添加到列表再移除，然后再找最短的国家
            short_country_list.append(shortest_country)
            data.pop(shortest_country_index)

        print("原始数据长度：", len(self.data), "=",
              "最短朝代列表长度:", len(short_country_list), "+", "剩余朝代的数据长度:", len(data))
        print(short_country_list)
        for country in short_country_list:
            print(country.get("name"), country.get("end_year") - country.get("start_year"))

    # 打印时间最长的几个国家，num是数量
    def print_longest_dynasty(self, num = 5):
        data = self.data[:]
        long_country_list = []
        if num > len(data):
            num = len(data)

        while len(long_country_list) < num:
            longest_country = data[0]
            longest = longest_country.get("end_year") - longest_country.get("start_year")
            longest_country_index = 0
            for index in range(len(data)):
                country = data[index]
                if (country.get("end_year") - country.get("start_year")) > longest:
                    longest_country_index = index
                    longest_country = data[longest_country_index]
                    longest = longest_country.get("end_year") - longest_country.get("start_year")

            long_country_list.append(longest_country)
            data.pop(longest_country_index)

        print(long_country_list)
        for country in long_country_list:
            print(country.get("name"), country.get("end_year") - country.get("start_year"))

    # 打印同一个首都的国家
    def print_same_capital(self):
        same_capital_dict = {
            # "capital_name": {
            #     "countries": []
            # }
        }
        for item in self.data:
            capital_key = item.get("capital")
            capital_dict = same_capital_dict.get(capital_key)
            if capital_dict is None:
                same_capital_dict[capital_key] = {
                    "countries": [item]
                }
            else:
                capital_dict["countries"].append(item)

        # print(same_capital_dict.keys())

        for key in same_capital_dict:
            countries_size = len(same_capital_dict[key].get("countries"))
            if countries_size > 1:
                if key == "...":
                    print("\n\n没有首都的国家有{0:<3}个".format(countries_size))
                else:
                    print("\n\n首都在 {0:<2} 的有{1:<2}个".format(key, countries_size))
                for item in same_capital_dict[key]["countries"]:
                    print(item["name"], end=" ")

    def print_same_period_danasty(self):


    # 打印同一地区的国家
    # def get_period(self):

    # 打印存在时间有交叠的国家

    # 打印存续时长相同的国家
    # def get_period(self):


###  以下开始测试 ###

dynasty = Dynasty()
dynasty.data = china_countries
print("打印全部国家")
#dynasty.print_dynasty()

print("打印全部国家的首都和地区")
# dynasty.print_country_capital()

print("打印时间最短的国家")
# dynasty.print_shortest_dynasty()

print("打印时间最长的国家")
# dynasty.print_longest_dynasty()

print("打印前5个时间最短的国家")
#dynasty.print_short_dynasty(5)

print("打印前5个时间最长的国家")
# dynasty.print_longest_dynasty()

print("打印相同首都的国家")
dynasty.print_same_capital()
