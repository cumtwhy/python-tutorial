## Common Question

1. UnicodeEncodeError: 'gbk' codec can't encode character u'\u200e' in position 43: illegal multibyte sequence
2. QUESTION:

   - 出现 UnicodeEncodeError: 说明是 Unicode 编码时候的问题
   - 'gbk' codec can’t encode character: 说明是将 Unicode 字符编码为 GBK 时候出现的问题

3. SOLUTION

   - 对 unicode 字符编码时，添加 ignore 参数，忽略无法无法编码的字符

     ```python
     gbkTypeStr = unicodeTypeStr.encode('GBK', 'ignore')
     ```

   - 将其转换为 GBK 编码的超集 GB18030

     ```python
     gb18030TypeStr = unicodeTypeStr.encode('GB18030')
     ```

## Recommend

1. about encoding tansfer

   ```python
   titleUni = titleHtml.decode('UTF-8', 'ignore')
   str.decode(encoding='UTF-8',errors='strict/ignore/replace/xmlcharrefreplace/backslashreplace')
   ```
