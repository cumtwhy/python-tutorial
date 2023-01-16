/*
Navicat MySQL Data Transfer

Source Server         : aliyun
Source Server Version : 50724
Source Host           : *.*.*.*:3306
Source Database       : baihui_book

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-03-11 14:19:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for baihui_book
-- ----------------------------
DROP TABLE IF EXISTS `baihui_book`;
CREATE TABLE `baihui_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(50) NOT NULL,
  `book_type` varchar(10) DEFAULT NULL,
  `book_price` double(10,2) DEFAULT NULL,
  `book_origin_price` double(10,2) DEFAULT NULL,
  `book_page` varchar(6) DEFAULT '0',
  `book_weight` varchar(10) DEFAULT NULL,
  `book_size` varchar(10) DEFAULT NULL,
  `book_publisher` varchar(20) DEFAULT NULL,
  `book_image` blob,
  `book_image_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
