# -*- coding: utf-8 -*-

import ex39_hashmap

provinces = ex39_hashmap.new()
ex39_hashmap.set(provinces, '浙江', '浙')
ex39_hashmap.set(provinces, '江苏', '苏')
ex39_hashmap.set(provinces, '安徽', '皖')
ex39_hashmap.set(provinces, '广东', '粤')
ex39_hashmap.set(provinces, '上海', '沪')

ex39_hashmap.list(provinces)
ex39_hashmap.get(provinces, '江苏')

cities = ex39_hashmap.new()
ex39_hashmap.set(cities, '浙', '杭州')
ex39_hashmap.set(cities, '苏', '扬州')
ex39_hashmap.set(cities, '皖', '合肥')
ex39_hashmap.set(cities, '粤', '深圳')
ex39_hashmap.set(cities, '沪', '静安')

ex39_hashmap.list(cities)
ex39_hashmap.delete(cities, '浙')
ex39_hashmap.list(cities)
ex39_hashmap.get(cities, '苏')

ex39_hashmap.get(cities, ex39_hashmap.get(provinces, '上海'))
