"""
random data file
"""
import re
import sys


# https://www.ssa.gov/oact/babynames/decades/names2010s.html
en_first_names_male = list(set(re.split(r"\s+", """
Noah Liam Jacob William Mason Ethan Michael Alexander James Elijah Benjamin Daniel Aiden Logan Jayden 
Matthew Lucas David Jackson Joseph Anthony Samuel Joshua Gabriel Andrew John Christopher Oliver Dylan 
Carter Isaac Luke Henry Owen Ryan Nathan Wyatt Caleb Sebastian Jack Christian Jonathan Julian Landon 
Levi Isaiah Hunter Aaron Charles Thomas Eli Jaxon Connor Nicholas Jeremiah Grayson Cameron Brayden Adrian 
Evan Jordan Josiah Angel Robert Gavin Tyler Austin Colton Jose Dominic Brandon Ian Lincoln Hudson Kevin 
Zachary Adam Mateo Jason Chase Nolan Ayden Cooper Parker Xavier Asher Carson Jace Easton Justin Leo 
Bentley Jaxson Nathaniel Blake Elias Theodore Kayden Luis Tristan Bryson Ezra Juan Brody Vincent Micah 
Miles Santiago Cole Ryder Carlos Damian Leonardo Roman Max Sawyer Jesus Diego Greyson Alex Maxwell Axel 
Eric Wesley Declan Giovanni Ezekiel Braxton Ashton Ivan Hayden Camden Silas Bryce Weston Harrison Jameson 
George Antonio Timothy Kaiden Jonah Everett Miguel Steven Richard Emmett Victor Kaleb Kai Maverick Joel 
Bryan Maddox Kingston Aidan Patrick Edward Emmanuel Jude Alejandro Preston Luca Bennett Jesse Colin Jaden 
Malachi Kaden Jayce Alan Kyle Marcus Brian Ryker Grant Jeremy Abel Riley Calvin Brantley Caden Oscar Abraham 
Brady Sean Jake Tucker Nicolas Mark Amir Avery King Gael Kenneth Bradley Cayden Xander Graham Rowan 
""".strip())))

en_first_names_female = list(set(re.split(r"\s+", """
Emma Olivia Sophia Isabella Ava Mia Abigail Emily Charlotte Madison Elizabeth Amelia Evelyn Ella Chloe 
Harper Avery Sofia Grace Addison Victoria Lily Natalie Aubrey Lillian Zoey Hannah Layla Brooklyn Scarlett 
Zoe Camila Samantha Riley Leah Aria Savannah Audrey Anna Allison Gabriella Claire Hailey Penelope Aaliyah 
Sarah Nevaeh Kaylee Stella Mila Nora Ellie Bella Lucy Alexa Arianna Violet Ariana Genesis Alexis Eleanor 
Maya Caroline Peyton Skylar Madelyn Serenity Kennedy Taylor Alyssa Autumn Paisley Ashley Brianna Sadie 
Naomi Kylie Julia Sophie Mackenzie Eva Gianna Luna Katherine Hazel Khloe Ruby Melanie Piper Lydia Aubree 
Madeline Aurora Faith Alexandra Alice Kayla Jasmine Maria Annabelle Lauren Reagan Elena Rylee Isabelle 
Bailey Eliana Sydney Makayla Cora Morgan Natalia Kimberly Vivian Quinn Valentina Andrea Willow Clara London 
Jade Liliana Jocelyn Trinity Kinsley Brielle Mary Molly Hadley Delilah Emilia Josephine Brooke Ivy Lilly 
Adeline Payton Lyla Isla Jordyn Paige Isabel Mariah Mya Nicole Valeria Destiny Rachel Ximena Emery Everly 
Sara Angelina Adalynn Kendall Reese Aliyah Margaret Juliana Melody Amy Eden Mckenzie Laila Vanessa Ariel 
Gracie Valerie Adalyn Brooklynn Gabrielle Kaitlyn Athena Elise Jessica Adriana Leilani Ryleigh Daisy Nova 
Norah Eliza Rose Rebecca Michelle Alaina Catherine Londyn Summer Lila Jayla Katelyn Daniela Harmony Alana 
Amaya Emerson Julianna Cecilia Izabella""".strip())))

en_last_names = list(set(re.split(r"\s+", """
Smith Johnson Williams Jones Brown Davis Miller Wilson Moore Taylor Anderson Thomas Jackson White Harris 
Martin Thompson Garcia Martinez Robinson Clark Rodriguez Lewis Lee Walker Hall Allen Young Hernandez King 
Wright Lopez Hill Scott Green Adams Baker Gonzalez Nelson Carter Mitchell Perez Roberts Turner Phillips 
Campbell Parker Evans Edwards Collins Stewart Sanchez Morris Rogers Reed Cook Morgan Bell Murphy Bailey 
Rivera Cooper Richardson Cox Howard Ward Torres Peterson Gray Ramirez James Watson Brooks Kelly Sanders 
Price Bennett Wood Barnes Ross Henderson Coleman Jenkins Perry Powell Long Patterson Hughes Flores Washington 
Butler Simmons Foster Gonzales Bryant Alexander Russell Griffin Diaz Hayes Myers Ford Hamilton Graham Sullivan 
Wallace Woods Cole West Jordan Owens Reynolds Fisher Ellis Harrison Gibson Mcdonald Cruz Marshall Ortiz Gomez 
Murray Freeman Wells Webb Simpson Stevens Tucker Porter Hunter Hicks Crawford Henry Boyd Mason Morales Kennedy 
Warren Dixon Ramos Reyes Burns Gordon Shaw Holmes Rice Robertson Hunt Black Daniels Palmer Mills Nichols Grant 
Knight Ferguson Rose Stone Hawkins Dunn Perkins Hudson Spencer Gardner Stephens Payne Pierce Berry Matthews 
Arnold Wagner Willis Ray Watkins Olson Carroll Duncan Snyder Hart Cunningham Bradley Lane Andrews Ruiz Harper 
Fox Riley Armstrong Carpenter Weaver Greene Lawrence Elliott Chavez Sims Austin Peters Kelley Franklin 
""".strip())))

zh_names_male = list(set(re.split(r"\s+", """德义 苍 鹏云 炎 和志 新霁 澜 星泽 驰轩 楚 宏深 全 波涛 飞文 波 振国 凯 光启 经略 乐天 
志强 作人 英叡 英华 星阑 景龙 鹏鲸 采 浩然 举 芬 鸿才 卫 嘉纳 旭东 玉泽 祺瑞 荫 茂德 博 鸿羲 彦 涵衍 开诚 鸿远 凯歌 星华 玉宇 潍 德华 甲 
梓 正阳 文乐 高杰 骄 腾逸 鸿畅 修平 飞扬 宏爽 乐康 和风 洁 令羽 承载 礼 昊硕 天瑞 安宁 高义 兴朝 颖 浩波 洲 颉 良骏 颜 锋 承业 彭泽 骏年 
坚白 运 承悦 钧 涵蓄 修雅 濮 天翰 经纬 天工 国源 奇迈 海逸 郁 俊侠 烨伟 昆峰 高旻 高超 鹏运 安 浩初 英逸 英豪 元甲 弘雅 温瑜 高雅 德明 慈 
良畴 良骥 康德 皓轩 涵忍 振锐 嘉石 浦泽 飞飙 子 安澜 奇略 英 学海 悦 明喆 兴昌 凯安 乐生 仕 凯泽 和煦 鸿才 伟懋 华美 怀 景行 鸿远 宜人 顺 
彭魄 宇文 景中 浩壤 奕 乐水 俊捷 高阳 云天 豪 驰翰 鑫鹏 鸾 伟诚 彤 华皓 安翔 正德 兴运 鸿达 硕 光济 博明 彭勃 阳曦 熠彤 泽语 睿德 原 令璟 
璞玉 明珠 许 宸 景明 春 子明 和昶 远航 枫 宜民 修然 巍然 卿 睿思 兴思 朔 高芬 容 长 鸿信 晨濡 俊哲 和悦 俊发 文曜 伟兆 昊天 宾""".strip())))

zh_names_female = list(set(re.split(r"\s+", """海莹 曼珠 虹影 凝安 淳美 清润 旋 馨香 骊霞 水丹 长文 怀薇 平卉 向露 秀敏 青柏 尔阳 奥婷 
智美 雅可 骊燕 燕珺 白曼 春枫 谷之 暖姝 易绿 娅欣 欢 半梅 忆彤 宇 茗 芳洁 双文 艳芳 珍丽 杨 若星 松 葳 晓畅 菱华 新荣 觅露 冰夏 初柳 迎蕾 
海宁 香 妙颜 靖之 冰莹 天菱 诗丹 思思 玄素 安波 依秋 香巧 蕙 朝旭 怡 赞悦 梓彤 婉静 庄静 冬卉 冷雪 冰海 吟怀 月灵 优瑗 清嘉 悦爱 迎荷 旎旎 
秋柳 巧春 美偲 忆灵 谷兰 雅娴 靖易 曼冬 溶溶 冷之 幼 芳蔼 妃 惜蕊 曼彤 傲之 愫 雪儿 以轩 丹秋 格 若云 骏 雅洁 朝雨 合美 馥 绿柳 慕凝 静曼 
品韵 易容 娅芳 月怡 琲 如云 格格 溪 儿 璠瑜 丁辰 秀媚 岚岚 筱 听 元冬 白山 乃 茉 寄蕾 倚 傲儿 谷 淑君 帅 凡灵 语林 叶 幻珊 山雁 涵涵 灿 
绮梅 平宁 天真 迎丝 水蓉 灵韵 甜恬 盼盼 韵宁 渟 安荷 智 虹英 访烟 玲玲 正思 霏 寄灵 友琴 绿柏 觅儿 娅玟 书琴 天蓉 宝 巧 寒雁 云韶 青旋 凝安 
清懿 依云 以松 妙珍 灵阳 韶美 梓珊 未 初雪 姝艳 采梦 苒 若山 绚 彤彤 家 春娇 梦云 溪蓝 以松 半烟 孤云 玑 元绿 如曼 痴瑶 灵雨 梦寒 湘云 涵畅 
玲琳 素华 """.strip())))

zh_last_name = list(set(re.split(r"\s+", """赵 钱 孙 李 周 吴 郑 王 冯 陈 褚 卫 蒋 沈 韩 杨 朱 秦 尤 许 何 吕 施 张 孔 曹 严 华 金 
魏 陶 姜 戚 谢 邹 喻 柏 水 窦 章 云 苏 潘 葛 奚 范 彭 郎 鲁 韦 昌 马 苗 凤 花 方 俞 任 袁 柳 酆 鲍 史 唐 费 廉 岑 薛 雷 贺 倪 汤 
滕 殷 罗 毕 郝 邬 安 常 乐 于 时 傅 皮 卞 齐 康 伍 余 元 卜 顾 孟 平 黄 和 萧 尹 湛 汪 祁 毛 禹 狄 米 贝 成 戴 谈 宋 茅 庞 熊 纪 
舒 屈 项 祝 董 梁 杜 阮 蓝 闵 席 季 麻 强 贾 路 娄 危 江 童 颜 郭 梅 盛 林 刁 钟 徐 邱 骆 高 夏 蔡 田 樊 胡 凌 霍 虞 万 支 柯 昝 
管 卢 莫 白 房 裘 缪 干 解 应 宗 丁 宣 贲 邓 郁 单 杭 洪 包 诸 左 石 崔 吉 钮 龚 程 嵇 邢 滑 裴 陆 荣 翁 荀 羊 宇文 尉迟 延陵 羊舌 
羊角 乐正 诸葛 颛孙 仲孙 仲长 长孙 钟离 宗政 左丘 主父 宰父 子书 子车 子桑 百里 北堂 北野 哥舒 谷梁 闻人 王孙 王官 王叔 巫马 微生 淳于 
单于 成公 叱干 叱利 褚师 端木 东方 东郭 东宫 东野 东里 东门 第二 第五 公祖 公玉 公西 公孟 公伯 公仲 公孙 公广 公上 公冶 公羊 公良 公户 
公仪 公山 公门 公坚 公乘 欧阳 濮阳 青阳 漆雕 壤驷 上官 司徒 司马 司空 司寇 士孙 申屠 叔孙 叔仲 侍其 令狐 梁丘 闾丘 刘傅 慕容 万俟 谷利 
高堂 南宫 南门 南荣 南野 女娲 纳兰 澹台 拓跋 太史 太叔 太公 秃发 夏侯 西门 鲜于 轩辕 相里 皇甫 赫连 呼延 胡母 亓官 夹谷 即墨 独孤 段干 
达奚""".strip())))

# via: http://www.lipsum.com/feed/html
# russian is from: http://masterrussian.com/vocabulary/most_common_words.htm
# japanese (4bytes) are from: http://www.i18nguy.com/unicode/supplementary-test.html
ascii_paragraphs = '''
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus
pharetra urna sit amet magna. Donec posuere porta velit. Vestibulum sed libero.
Ut vestibulum sodales arcu. Proin vulputate, mi quis luctus ornare, elit ligula fringilla nisi,
eu tempor purus felis a enim. Phasellus in justo et nisi rhoncus porttitor. Donec ligula felis,
sagittis at, vestibulum eu, vehicula sed, nisl. Aenean convallis pharetra nisl. Mauris imperdiet
libero eu urna ultrices vulputate. Donec semper nunc et nibh. In hac habitasse platea dictumst.
Fusce et ipsum semper velit tempor pharetra. Donec pretium sollicitudin purus. Cras mi velit,
egestas id, ultrices vitae, viverra sit amet, justo.

Quisque cursus tristique nunc. Fusce varius, orci et pellentesque aliquet,
nibh ipsum sodales lorem, iaculis tincidunt massa metus ut erat. Fusce dictum,
dolor ut laoreet aliquam, massa urna placerat nibh, vitae tristique nisl neque posuere mi.
Aliquam at orci. Nulla sem. Nullam risus. Nullam pharetra dapibus mauris. Mauris mollis pretium arcu.
Vestibulum sem massa, tempor a, dictum id, rutrum eu, ligula. Class aptent taciti sociosqu ad
litora torquent per conubia nostra, per inceptos himenaeos. Curabitur ultrices dignissim nibh.
Aenean nisl.

Integer bibendum pharetra orci. Suspendisse commodo, lorem elementum egestas hendrerit,
metus elit rutrum sapien, quis aliquam nibh nisi at ligula. Nam lobortis commodo mauris.
Vivamus semper, leo vel accumsan mattis, nulla elit vestibulum augue, vitae pharetra dolor nibh
sit amet odio. Pellentesque scelerisque ipsum id elit. Nulla aliquet semper dolor. Praesent ut lorem.
Curabitur dictum, magna eu porttitor rutrum, ipsum justo porttitor erat, sit amet tristique est ante
ut elit. Mauris vel est. In cursus, velit quis pharetra adipiscing, purus quam sagittis mi,
eget molestie leo lectus ac lacus. Curabitur ante massa, aliquam ut, scelerisque a, condimentum at,
eros. Nunc vitae neque. Nam sagittis scelerisque magna. Class aptent taciti sociosqu ad litora
torquent per conubia nostra, per inceptos himenaeos. Donec cursus pede. Quisque a mauris nec
turpis convallis scelerisque. Donec quam lorem, mollis vestibulum, euismod in, hendrerit et, sapien.
Curabitur felis.

Morbi pretium lorem imperdiet dui. Maecenas quis ligula. Morbi tempor velit sit amet felis.
Donec at dui. Donec neque. Quisque quis mauris a libero ultrices iaculis. Integer congue feugiat justo.
Quisque imperdiet lectus eu orci. Class aptent taciti sociosqu ad litora torquent per conubia nostra,
per inceptos himenaeos. Vivamus id lectus. Phasellus odio nisi, auctor eu, hendrerit quis,
iaculis sit amet, felis. Sed blandit mollis nunc. Sed velit magna, tristique tristique, porttitor ut,
dictum a, arcu. In hac habitasse platea dictumst. Cras semper bibendum tortor. Cum sociis natoque
penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti.
In hac habitasse platea dictumst. Fusce mi sem, varius vitae, molestie ut, gravida venenatis, nibh.
Nam risus lectus, interdum at, condimentum eu, aliquet et, ipsum.

Mauris mi tortor, elementum ut, mattis eget, aliquam a, tellus.
Suspendisse porttitor orci. Donec rutrum diam non est. Duis ac nunc. Cras sollicitudin aliquet mi.
Cras in pede. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
Nam vehicula est at metus. Suspendisse sapien. Nunc lobortis tortor sed purus hendrerit pellentesque.
Nunc laoreet. Morbi pharetra. Integer cursus molestie turpis. Nam cursus sodales sem.
Maecenas non lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames
ac turpis egestas. Nam vel nibh eu nulla blandit facilisis. Sed varius turpis ac neque.
Curabitur vel erat. Morbi sed purus id erat tincidunt ullamcorper.
'''

unicode_paragraphs = '''
\u0437\u043d\u0430\u0442\u044c \u043c\u043e\u0439 \u0434\u043e \u0438\u043b\u0438 \u0435\u0441\u043b\u0438
\u0432\u0440\u0435\u043c\u044f \u0440\u0443\u043a\u0430 \u043d\u0435\u0442 \u0441\u0430\u043c\u044b\u0439
\u043d\u0438 \u0441\u0442\u0430\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u0434\u0430\u0436\u0435
\u0434\u0440\u0443\u0433\u043e\u0439 \u043d\u0430\u0448 \u0441\u0432\u043e\u0439 \u043d\u0443 \u043f\u043e\u0434
\u0433\u0434\u0435 \u0434\u0435\u043b\u043e \u0435\u0441\u0442\u044c \u0441\u0430\u043c \u0440\u0430\u0437
\u0447\u0442\u043e\u0431\u044b \u0434\u0432\u0430 \u0442\u0430\u043c \u0447\u0435\u043c \u0433\u043b\u0430\u0437
\u0436\u0438\u0437\u043d\u044c \u043f\u0435\u0440\u0432\u044b\u0439 \u0434\u0435\u043d\u044c \u0442\u0443\u0442
\u0432\u043e \u043d\u0438\u0447\u0442\u043e \u043f\u043e\u0442\u043e\u043c \u043e\u0447\u0435\u043d\u044c
\u0441\u043e \u0445\u043e\u0442\u0435\u0442\u044c \u043b\u0438 \u043f\u0440\u0438 \u0433\u043e\u043b\u043e\u0432\u0430
\u043d\u0430\u0434\u043e \u0431\u0435\u0437 \u0432\u0438\u0434\u0435\u0442\u044c \u0438\u0434\u0442\u0438
\u0442\u0435\u043f\u0435\u0440\u044c \u0442\u043e\u0436\u0435 \u0441\u0442\u043e\u044f\u0442\u044c
\u0434\u0440\u0443\u0433 \u0434\u043e\u043c \u0441\u0435\u0439\u0447\u0430\u0441 \u043c\u043e\u0436\u043d\u043e
\u043f\u043e\u0441\u043b\u0435 \u0441\u043b\u043e\u0432\u043e \u0437\u0434\u0435\u0441\u044c
\u0434\u0443\u043c\u0430\u0442\u044c \u043c\u0435\u0441\u0442\u043e \u0441\u043f\u0440\u043e\u0441\u0438\u0442\u044c
\u0447\u0435\u0440\u0435\u0437 \u043b\u0438\u0446\u043e \u0447\u0442\u043e \u0442\u043e\u0433\u0434\u0430
\u0432\u0435\u0434\u044c \u0445\u043e\u0440\u043e\u0448\u0438\u0439 \u043a\u0430\u0436\u0434\u044b\u0439
\u043d\u043e\u0432\u044b\u0439 \u0436\u0438\u0442\u044c \u0434\u043e\u043b\u0436\u043d\u044b\u0439
\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0447\u0435\u043c\u0443
\u043f\u043e\u0442\u043e\u043c\u0443 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043f\u0440\u043e\u0441\u0442\u043e
\u043d\u043e\u0433\u0430 \u0441\u0438\u0434\u0435\u0442\u044c \u043f\u043e\u043d\u044f\u0442\u044c
\u0438\u043c\u0435\u0442\u044c \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0434\u0435\u043b\u0430\u0442\u044c
\u0432\u0434\u0440\u0443\u0433 \u043d\u0430\u0434 \u0432\u0437\u044f\u0442\u044c \u043d\u0438\u043a\u0442\u043e
\u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0434\u0432\u0435\u0440\u044c \u043f\u0435\u0440\u0435\u0434
\u043d\u0443\u0436\u043d\u044b\u0439 \u043f\u043e\u043d\u0438\u043c\u0430\u0442\u044c
\u043a\u0430\u0437\u0430\u0442\u044c\u0441\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u0442\u0440\u0438
\u0432\u0430\u0448 \u0443\u0436 \u0437\u0435\u043c\u043b\u044f \u043a\u043e\u043d\u0435\u0446
\u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0430\u0441 \u0433\u043e\u043b\u043e\u0441
\u0433\u043e\u0440\u043e\u0434 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u043f\u043e\u043a\u0430
\u0445\u043e\u0440\u043e\u0448\u043e \u0434\u0430\u0432\u0430\u0442\u044c \u0432\u043e\u0434\u0430
\u0431\u043e\u043b\u0435\u0435 \u0445\u043e\u0442\u044f \u0432\u0441\u0435\u0433\u0434\u0430
\u0432\u0442\u043e\u0440\u043e\u0439 \u043a\u0443\u0434\u0430 \u043f\u043e\u0439\u0442\u0438
\u0441\u0442\u043e\u043b \u0440\u0435\u0431\u0451\u043d\u043e\u043a \u0443\u0432\u0438\u0434\u0435\u0442\u044c
\u0441\u0438\u043b\u0430 \u043e\u0442\u0435\u0446 \u0436\u0435\u043d\u0449\u0438\u043d\u0430
\u043c\u0430\u0448\u0438\u043d\u0430 \u0441\u043b\u0443\u0447\u0430\u0439 \u043d\u043e\u0447\u044c
\u0441\u0440\u0430\u0437\u0443 \u043c\u0438\u0440 \u0441\u043e\u0432\u0441\u0435\u043c
\u043e\u0441\u0442\u0430\u0442\u044c\u0441\u044f \u043e\u0431 \u0432\u0438\u0434 \u0432\u044b\u0439\u0442\u0438
\u0434\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043b\u044e\u0431\u0438\u0442\u044c
\u0441\u0442\u0430\u0440\u044b\u0439 \u043f\u043e\u0447\u0442\u0438 \u0440\u044f\u0434
\u043e\u043a\u0430\u0437\u0430\u0442\u044c\u0441\u044f \u043d\u0430\u0447\u0430\u043b\u043e
\u0442\u0432\u043e\u0439 \u0432\u043e\u043f\u0440\u043e\u0441 \u043c\u043d\u043e\u0433\u043e
\u0432\u043e\u0439\u043d\u0430 \u0441\u043d\u043e\u0432\u0430 \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c
\u043c\u0435\u0436\u0434\u0443 \u043f\u043e\u0434\u0443\u043c\u0430\u0442\u044c \u043e\u043f\u044f\u0442\u044c
\u0431\u0435\u043b\u044b\u0439 \u0434\u0435\u043d\u044c\u0433\u0438 \u0437\u043d\u0430\u0447\u0438\u0442\u044c
\u043f\u0440\u043e \u043b\u0438\u0448\u044c \u043c\u0438\u043d\u0443\u0442\u0430 \u0436\u0435\u043d\u0430
'''

# only add 4-byte unicode if 4-byte unicode is supported
if sys.maxunicode > 65535:
    unicode_paragraphs += '''
\U0002070e \U00020731 \U00020779 \U00020c53 \U00020c78 \U00020c96 \U00020ccf \U00020cd5 \U00020d15 \U00020d7c
\U00020d7f \U00020e0e \U00020e0f \U00020e77 \U00020e9d \U00020ea2 \U00020ed7 \U00020ef9 \U00020efa \U00020f2d
\U00020f2e \U00020f4c \U00020fb4 \U00020fbc \U00020fea \U0002105c \U0002106f \U00021075 \U00021076 \U0002107b
\U000210c1 \U000210c9 \U000211d9 \U000220c7 \U000227b5 \U00022ad5 \U00022b43 \U00022bca \U00022c51 \U00022c55
\U00022cc2 \U00022d08 \U00022d4c \U00022d67 \U00022eb3 \U00023cb7 \U000244d3 \U00024db8 \U00024dea \U0002512b
\U00026258 \U000267cc \U000269f2 \U000269fa \U00027a3e \U0002815d \U00028207 \U000282e2 \U00028cca \U00028ccd
\U00028cd2 \U00029d98
'''

ascii_words = re.split(r'\s+', ascii_paragraphs.strip())
unicode_words = re.split(r'\s+', unicode_paragraphs.strip())
words_str = ascii_words + unicode_words

mobile = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 195, 197,
          198]
unicom = [130, 131, 132, 145, 155, 156, 166, 175, 176, 185, 186, 196]
telecom = [133, 149, 153, 180, 181, 189, 173, 177, 190, 191, 193, 199]
