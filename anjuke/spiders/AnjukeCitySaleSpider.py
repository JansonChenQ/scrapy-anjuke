from anjuke.spiders.AnjukeBaseSpider import AnjukeBaseSpider, load_crt_page_index_cache


def gen_start_urls(city_list, area_list):
    '''
    生成起始url
    :param city_list:
    :param area_list:
    :return:
    '''
    start_urls = []
    for city in city_list:
        for area in area_list:
            start_url = "https://{city}.anjuke.com/sale/{area}/".format(city=city, area=area)
            start_urls.append(start_url)

    # 使用缓存数据
    # crt_page_index = load_crt_page_index_cache()
    crt_page_index = 0
    if crt_page_index != 0:

        for i in range(len(start_urls)):
            start_urls[i] += "p{num}".format(num=crt_page_index)

    return start_urls


class AnjukeJingMenListSaleSpider(AnjukeBaseSpider):
    name = "anjuke_jingmen"

    # 所有一级行政区
    city_list = ['jingmen']

    # 所有二级行政区
    area_list = ['duodao', 'dongbao']

    print("开始生成起始url")
    start_urls = gen_start_urls(city_list, area_list)
    print("开始爬取")


class AnjukehebListSaleSpider(AnjukeBaseSpider):
    name = "anjuke_heb"

    # 所有一级行政区
    city_list = ['heb']

    # 所有二级行政区
    area_list = ['daoli', 'nanganga', 'daowai']

    print("开始生成起始url")
    start_urls = gen_start_urls(city_list, area_list)
    print("开始爬取")


class AnjukeWuHanListSaleSpider(AnjukeBaseSpider):
    name = "anjuke_wuhan"

    # 所有一级行政区
    city_list = ['wuhan']

    # 所有二级行政区
    area_list = ['wuchanga', 'hongshana', 'jiangan','hanyang','jianghana'
        ,'qiaokou','jiangxiat','qingshan']

    print("开始生成起始url")
    start_urls = gen_start_urls(city_list, area_list)
    print("开始爬取")
