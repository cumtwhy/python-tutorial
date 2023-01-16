## baihui_book

### column

- book_name vchar(20)
  - xpath format: //div[@class="mysw"]//h1/text()
- book_page int(5): **单位: 页**
  - xpath format: //div[@class="mysw"]//div[@class="nr"]//h2[8]/text()
- book_size vachar(5): **单位: 开**
  - xpath format: //div[@class="mysw"]//div[@class="nr"]//h2[6]/text()
- book_weight int(5): **单位: 克**
  - xpath format: //div[@class="mysw"]//div[@class="nr"]//h2[3]/text()
- book_price double: **单位: 元**
  - xpath format: //div[@class="s1"]//h2//font[2]/text()
- book_origin_price double: **单位: 元**
  - xpath format: //div[@class="s1"]//h1/text()
- book_image BLOB +
- book_image_url vachar(50)
  - xpath format: //img[@class="simg"]/@src
- book_publisher vachar(10)
  - xpath format: //div[@class="mysw"]//div[@class="nr"]//h2[1]/text()
- book_type vachar(10)
  - xpath format: //ul[@class="navigation"]//li//ul//li//a/text()
  - lei: 187 青少课外名著类
  - lei: 181 幼儿教育启蒙类
  - lei: 188 青春言情小说类
  - lei: 184 孕产育儿家教类
  - lei: 199 字词典工具书类
  - lei: 186 生活养生保健类
  - lei: 185 经营管理励志类
  - lei: 183 社科文学哲理类
  - lei: 182 作文课外辅导类
  - lei: 179 59 元大全集（满 40 本厂家发货）
  - lei: 178 1---2 元特价区
  - lei: 177 精装套盒 12 套一箱厂家发货
  - lei: 202 红星图书系列
  - lei: 201 8.5 常春藤（满 28 本/箱厂家代发）
  - lei: 198 精品字帖 1.5 元系列
  - lei: 191 百汇图书精品专区
