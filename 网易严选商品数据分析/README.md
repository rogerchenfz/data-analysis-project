# 网易严选商品数据分析

## 数据介绍
commAttri.xlsx：商品属性
- itemId：商品ID
- minTime：商品评价的最早生成日期
- Ncmts：抓取数据时刻，商品的评价总量
- prodName：商品名称
- category：商品类别
- itemTagList：商品标签
- promTag：抓取数据时刻，商品的促销标签
- productPlace：商品产品标签
- price：抓取数据时刻，商品的标价

csv-cmt文件夹中每一个文件存储一个商品的全部评价数据。文件名前缀为商品ID，以此ID至商品属性表commAttri.xlsx的itemId列找到对应行，即可获取此商品的属性信息。文件中每一行为一条商品评论：
- itemId：商品ID
- star：商品评分
- content：评价内容
- createTime：评价生成时间

## 数据分析
根据已有的 2018 年网易严选商品属性和商品评价的数据，该项目主要通过 Python 进行一系列统计分析
- 对商品属性进行描述性统计分析，包括商品的类别、价格、销量、星级分布情况
- 对商品名称进行文本分析，用词云进行可视化
- 探究商品的价格和星级对销量的影响

# NetEase Yeation Product Data Analysis

## Data Introduction
commAttri.xlsx：Commodity Attribute
- itemId：item ID
- minTime：the earliest created date of comment of product
- Ncmts：number of comments of product
- prodName：product name
- category：product category
- itemTagList：product tag
- promTag：promotion label of product
- productPlace：place of production
- price：price of product

Each file in the csv-cmt folder stores all the comment data for a product. The file name is prefixed with the item ID, and the commodity attribute information can be obtained by using this ID to find the corresponding row in the itemID column of the item attribute table commAttri.xlsx. Each behavior in the document has a commodity review:
- itemId：item ID
- star：star of product
- content：content of comment
- createTime：created time of comment

## Data Analysis
According to the existing data of 2018 Netease Yeation product attributes and product evaluation, this project mainly carried out a series of statistical analysis through Python
- Conduct descriptive statistical analysis of product attributes, including product category, price, sales volume and star distribution
- Text analysis of product names and visualization of word cloud
- Explore the impact of product price and star rating on sales
