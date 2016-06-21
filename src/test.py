from unittest2 import TestCase

class TestProcess(TestCase):
    def _parse_article(self, url, lang):
        # TODO: the super goose
        return

    def testEttoday(self):
        article = self._parse_article('http://www.ettoday.net/news/20160613/715878.htm', 'zh')

        # test basic information
        self.assertEqual(article.title, u'88歲翁離奇爬信義區四獸山亡　遺體坐涼亭、血沿石椅流地')
        self.assertEqual(len(article.sections), 1)
        self.assertEqual(len(article.paragraphs), 6)
        self.assertEqual(article.top_image, 'http://static.ettoday.net/images/1844/d1844704.jpg')
        self.assertEqual({
            'http://static.ettoday.net/images/1844/d1844704.jpg',
            'http://static.ettoday.net/images/1844/d1844309.jpg',
            'http://static.ettoday.net/images/1844/d1844307.jpg',
            'http://static.ettoday.net/images/1844/d1844706.jpg'
        }, set(article.images))

        self.assertEqual({'http://www.youtube.com/watch?v=hynF9ds0XTs'}, set(article.videos))

        # test section
        section = article.sections[0]
        self.assertEqual(len(section.paragraphs), 6)
        self.assertEqual(section.title, "")
        self.assertEqual({
            'http://static.ettoday.net/images/1844/d1844704.jpg',
            'http://static.ettoday.net/images/1844/d1844309.jpg',
            'http://static.ettoday.net/images/1844/d1844307.jpg',
            'http://static.ettoday.net/images/1844/d1844706.jpg'
        }, set(section.images))

        self.assertEqual({'http://www.youtube.com/watch?v=hynF9ds0XTs'}, set(section.videos))

        # test paragraph
        article.paragraphs[0].text = u'台北市四獸山步道發生離奇命案！一名88歲老翁13日被發現陳屍在山間的涼亭，且身上還有刀傷。家屬表示老翁前一天早上出門運動後，就再也沒有回家，隔天早上警方與家屬上山找人，才發現已經老翁坐在小屋涼亭，但已死亡多時。由於老翁生前交往單純，身上財物也沒有不見，究竟死因為何，檢警正在調查釐清。'
        article.paragraphs[1].text = u'88歲的李姓老翁每天風雨無阻，上山運動，12日一如往常揹著後背包、拄著登山杖，在清晨5點多到北市信義區福德街的四獸山爬山運動，沒想到12日上山後就再也沒有回家，家屬等到中午發現還沒有回家，先到警局報失蹤，13日早上在警方陪同下，上山找人。'
        article.paragraphs[2].text = u'警消人員發動搜山，13日中午在福德街221巷30號龍山洞附近的小路發現李姓老翁。老翁被發現時呈現坐姿，在龍山洞旁偏僻步道的涼亭內死亡，身上疑似有多處刀傷，警方立刻封鎖現場採證中，並出動義消垂降，希望能在現場尋找凶器。'
        article.paragraphs[3].text = u'離奇的是，李翁被發現時包括手臂和腳部有多處刀傷，但老翁身上的財物沒有不見，遺體還呈現坐姿，上半身沒穿衣服斜倒亭內石椅上，血沿著石椅流到地板，出門時穿襯衫，卻掛在涼亭右側。現場無打鬥、反抗痕跡，加上老翁錢財物品都沒被翻動。'
        article.paragraphs[4].text = u'因為他每天都會來這裡運動，附近居民對他並不陌生「這段山路比較少人來爬啦，也很少人知道，旁邊的老闆娘說，（老翁）都早上6點多來，7點多出去，都固定的啦。」'
        article.paragraphs[5].text = u'李翁的太太及女兒想到老翁竟然在每天上下山的必經小路死亡，相當難過，忍不住掩面痛哭。由於台北市信義區四獸山步道是許多人假日都會來爬山的地方，如今突然發生離奇命案，警方將查明死因為何，希望早日破案。'

    def testBNEXT(self):
        article = self._parse_article('http://www.bnext.com.tw/article/view/id/39963', 'zh')

        # test basic information
        self.assertEqual(article.title, u'[Meet創業之星]從女性角度出發主打華人圈，AiMM為你配對最理想對象')
        self.assertEqual(article.top_image, 'https://3.bp.blogspot.com/-za2l248UlyQ/V2e7d1wDCsI/AAAAAAAAMq8/49mEDXyOdrYwatelH-wJlix_ubSuyIg4ACKgB/s600/%25E8%2595%25AD%25E5%25AD%2598%25E6%2599%25BA%252B%25E7%258E%258B%25E4%25BA%25AD%25E5%25B5%2590%252B%25E9%2599%25B3%25E6%259D%25B1%25E9%2581%25A0%2528%25E5%258F%25B3%25E8%2587%25B3%25E5%25B7%25A6%2529_AiMM_%25E5%2589%25B5%25E6%25A5%25AD%25E5%258D%2588%25E9%25A4%2590%25E6%259C%2583_2016-05-27_%25E8%25B3%2580%25E5%25A4%25A7%25E6%2596%25B0%25E6%2594%259D%25E5%25BD%25B1_7334.JPG')
        self.assertEqual({
            'https://3.bp.blogspot.com/-za2l248UlyQ/V2e7d1wDCsI/AAAAAAAAMq8/49mEDXyOdrYwatelH-wJlix_ubSuyIg4ACKgB/s600/%25E8%2595%25AD%25E5%25AD%2598%25E6%2599%25BA%252B%25E7%258E%258B%25E4%25BA%25AD%25E5%25B5%2590%252B%25E9%2599%25B3%25E6%259D%25B1%25E9%2581%25A0%2528%25E5%258F%25B3%25E8%2587%25B3%25E5%25B7%25A6%2529_AiMM_%25E5%2589%25B5%25E6%25A5%25AD%25E5%258D%2588%25E9%25A4%2590%25E6%259C%2583_2016-05-27_%25E8%25B3%2580%25E5%25A4%25A7%25E6%2596%25B0%25E6%2594%259D%25E5%25BD%25B1_7334.JPG',
        }, set(article.images))

        self.assertEqual({'https://player.vimeo.com/video/140969370'}, set(article.videos))

        # test section
        section = article.sections[0]
        self.assertEqual(len(section.paragraphs), 2)
        self.assertEqual(section.title, "")
        self.assertEqual({
            'https://3.bp.blogspot.com/-za2l248UlyQ/V2e7d1wDCsI/AAAAAAAAMq8/49mEDXyOdrYwatelH-wJlix_ubSuyIg4ACKgB/s600/%25E8%2595%25AD%25E5%25AD%2598%25E6%2599%25BA%252B%25E7%258E%258B%25E4%25BA%25AD%25E5%25B5%2590%252B%25E9%2599%25B3%25E6%259D%25B1%25E9%2581%25A0%2528%25E5%258F%25B3%25E8%2587%25B3%25E5%25B7%25A6%2529_AiMM_%25E5%2589%25B5%25E6%25A5%25AD%25E5%258D%2588%25E9%25A4%2590%25E6%259C%2583_2016-05-27_%25E8%25B3%2580%25E5%25A4%25A7%25E6%2596%25B0%25E6%2594%259D%25E5%25BD%25B1_7334.JPG'
        }, set(section.images))

        section.paragraphs[0].text = u'上班族工作忙碌，沒有多餘的時間精力認識新對象，若想用線上交友軟體，則因為市面上太多種選擇，不知道哪一種最適合自己。現代美緣數位科技股份有限公司推出了一款交友軟體──AiMM　 APP，目標客群針對全球各地26至50歲的華人單身男女，企圖為他們配對，找到彼此心目中最符合理想條件的Ms. ／Mr. Right。'
        section.paragraphs[1].text = u'AiMM團隊的共同創辦人王亭嵐旅居在國外多年，在紐約的公司做過公關，也在台灣與先生經營過葡萄酒店。2013年時有了創業的念頭，起源於在台灣與國外生活時結交許多朋友，周遭的朋友時常向她諮詢感情問題。藉由朋友們的經驗，她覺得找到對的人非常重要，也發覺現代人的交友需求市場非常大，因此開始有創辦交友平台的想法，2015年創立現代美緣數位科技股份有限公司、2016年2月推出產品服務──AiMM　 APP，並且負責產品規劃及用戶開發。她的先生蕭智存也為共同創辦人，負責公司的營運管理。'

        section = article.sections[1]
        self.assertEqual(len(section.paragraphs), 2)
        self.assertEqual(section.title, u'會員影片自介更符合交友需求')
        self.assertEqual({'https://player.vimeo.com/video/140969370'}, set(section.videos))
        self.assertEqual(len(section.images), 0)

        section.paragraphs[0].text = u'AiMM團隊表示，市場上一般的交友軟體，還是主打迅速方便為主，使用者可以快速地藉由瀏覽「照片海」的方式，先找到符合外貌條件的對象後才瞭解對方的個性特色，決定是否和對方有更一進步的接觸。但是這種方式卻會使得使用者錯失一些交友機會，使用者只能將自己的照片上傳，加 上一點簡單敘述，把資訊曝光在陌生人眼中。團隊企圖做出差異化與其他交友軟體有所區隔，營造出更友善的交友環境。'
        section.paragraphs[1].text = u'APP其中的一項特色在於──使用者登入個人資料成為會員時，必須製作一段自我介紹的影片，使用者可以透過影片更清楚地瞭解對方的氣質、談吐和個人特色，在影片的最後才會秀出使用者年齡、身高等基本資訊。有別於傳統瀏覽照片的方式，使用者可以先瞭解對方的個人特質，而不是以外貌取勝。'

