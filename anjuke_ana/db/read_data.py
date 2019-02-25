from functools import reduce

from anjuke.items import AnjukeBean
from anjuke_ana.db.base import read_sql, get_sql_session


def get_all_locate_a():
    '''
    获取所有行政区
    :return:
    '''
    r = read_sql("select distinct LOCATE_A from anjuke_sale_data")
    locate_a_list = [item[0] for item in r.values]
    return locate_a_list


def get_all_locate_b(locate_a):
    '''
    获取所有的二级行政区
    :param locate_a:
    :return:
    '''
    r = read_sql(
        "select distinct LOCATE_B from anjuke_sale_data where LOCATE_A = \"{locate_a}\"".format(locate_a=locate_a))
    locate_b_list = [item[0] for item in r.values]
    return locate_b_list


def calc_average_price(locate_a):
    df_o = read_sql("""select
                     locate_b,
                     count(*) as count,
                     sum(area) as total_area,
                     sum(price) as total_price
                    from anjuke_sale_data 
                    where locate_a = '%s' 
                    group by locate_b """ % locate_a)

    count = df_o['count']
    total_area = df_o['total_area']
    total_price = df_o['total_price']

    df_o['average_price'] = total_price / total_area
    df_o['average_area'] = total_area / count

    df_o = df_o.sort_values(by='average_price')
    return df_o


def calc_price(city, area):
    session = get_sql_session()
    area_list = session.query(AnjukeBean).filter(AnjukeBean.locate_b == area).all()
    all_area = reduce(lambda x, y: x.area + y.area, area_list)
    print(all_area)
    # .filter(AnjukeBean.locate_b == area and AnjukeBean.locate_a == city)\
    session.close()


if __name__ == '__main__':
    # calc_price('荆门', '掇刀')

    print(calc_average_price('洪山'))
    print(calc_average_price('江汉'))
    print(calc_average_price('江岸'))
    print(calc_average_price('汉阳'))
    # for locate_a in get_all_locate_b("东宝"):
    #     print(locate_a)
    #     df = calc_average_price(locate_a)
    #     print(df)

    # for locate_b in get_all_locate_b(locate_a):
    #     print("     " + locate_b)
