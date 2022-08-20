# Програмний модуль **"xml2digest"** | Вступ

**Програмний модуль xml2digest – "Програмний модуль побудови дайджесту на основі повідомлень у XML"**, який написаний мовою програмування `Python`, призначений для побудови дайджесту з набору інформаційних повідомлень, що містяться у єдиному файлі формату `XML`.


### Зміст
- [Позначення та найменування програмного модуля](#name)
- [Програмне забезпечення, необхідне для функціонування програмного модуля](#software)
- [Функціональне призначення](#function)
- [Опис логічної структури](#structure)
- [Виклик та завантаження](#run)
- [Вхідні дані](#inputdata)
- [Вихідні дані](#outputdata)

<a name="name"></a>
<h2>Позначення та найменування програмного модуля</h2>

Програмний модуль має позначення **"xml2digest"**.

Повне найменування програмного модуля – **"рограмний модуль побудови дайджесту на основі повідомлень у XML"**.

<a name="software"></a>
<h2>Програмне забезпечення, необхідне для функціонування програмного модуля</h2>

Для функціонування програмного модуля, написаного мовою програмування `Python`, необхідне наступне програмне забезпечення та пакети:

- `python 3.8.0` or newer [v3.8.0](https://www.python.org/downloads/release/python-380/)
- `sklearn` [v.1.1.2](https://pypi.org/project/scikit-learn/1.1.2/)
- `scipy` [v1.8.1](https://pypi.org/project/scipy/1.8.1/)
- `numpy` [v1.23.0](https://pypi.org/project/numpy/1.23.0/)

<a name="function"></a>
<h2>Функціональне призначення</h2>

Програмний модуль **"xml2digest"** призначений для побудови дайджесту з набору інформаційних повідомлень, що містяться у єдиному файлі формату `XML`.

<a name="structure"></a>
<h2>Опис логічної структури</h2>

Програмний модуль складається з частин:
- `main.py` — головного скрипта, що здійснює порядкове зчитування вхідного `XML` та викликає наступні підмодулі:
	- `vectorProcessing.py` — підмодуль, що здійснює формування вектора - образа окремого повідомлення на основі ключових слів (функція `build()`) та накопичення векторів для подальшого формування матриці (функція `accumulate()`)
	- `clustering.py` — підмодуль, що здійснює кластеризацію та формування дайджесту

	
<a name="run"></a>
<h2>Виклик та завантаження</h2>

Для запуску програмного модуля **"xml2digest"** необхідно:
1. Клонувати репозиторій:
```sh
git clone https://github.com/OlehDmytrenko/xml2digest.git
```
2. Перейти в директорію склонованого репозиторія та запустити головний скрипт `main.py`, вказавши як параметр повний шлях `<full path>` до вхідного `XML` файлу з набором інформаційних повідомлень та кількість кластерів `<num clusters>`:
```sh
cd /DWNT
python main.py <full path> <num clusters>
```

<a name="inputdata"></a>
<h2>Вхідні дані</h2>

Вхідними даними є `XML` файл, що містить інформаційні повідомлення у наступному вигляді: 

```xml
<sphinx:document id="388_ok">
<subject>Заголовок</subject>
<content>Текст інформаційного повідомлення</content>
<lang>мова</lang>
<keyword>текст інформац повідомл</keyword>
<source>Джерело</source>
<datatime>20220811 23:16</datatime>
<url>https://souce.com/messages/1</url>
</sphinx:document>
```

<a name="outputdata"></a>
<h2>Вихідні дані</h2>

Вихідні дані - дайджест у форматі `JSON`, де в якості ключів - кластери, кожен з яких містить набір документів, відсортованих за близькістю до центроїда.

Зразок вихідних даних:

```json
{"0": {"491_ok": 1.4552555085074508, "443_ok": 1.531352775265723, "502_ok": 1.8247985661882045, "424_ok": 1.8289454126118785, "506_ok": 1.8330828779587491, "419_ok": 2.0217481457239668, "445_ok": 2.03668152280724, "429_ok": 2.0989634067606056, "401_ok": 2.2588973150388805, "402_ok": 2.2588973150388805, "406_ok": 2.2588973150388805, "417_ok": 2.2855697760300218, "455_ok": 2.2855697760300218, "459_ok": 2.2855697760300657, "504_ok": 2.2954920488985526, "458_ok": 2.2987899559785743, "442_ok": 2.302083138563764, "499_ok": 2.302083138563765, "462_ok": 2.3086554110916104, "394_ok": 2.3119345410962824, "530_ok": 2.4082331234453997, "422_ok": 2.4207835172657655, "525_ok": 2.4580502475099584, "457_ok": 2.4977951709965382, "501_ok": 2.5068775920870285, "396_ok": 2.5129143025601155, "427_ok": 2.601784723330616, "529_ok": 2.607601728957011, "522_ok": 2.622087785070746, "527_ok": 2.6508224203315294, "434_ok": 2.6764198363664806, "463_ok": 2.7045772852723484, "523_ok": 2.781902355628889, "409_ok": 2.8170818967902345, "447_ok": 2.8170818967902345, "403_ok": 2.8278183240493604, "468_ok": 2.8278183240493724, "481_ok": 2.8411818050921904, "460_ok": 2.8438469657733427, "465_ok": 2.8677219532412717, "500_ok": 2.875636233350218, "469_ok": 2.938183130812806, "470_ok": 2.938183130812806, "521_ok": 2.953612906442215, "528_ok": 2.956176705857342, "526_ok": 2.958738283695425, "423_ok": 2.9612976457216478, "473_ok": 2.98169345637151, "404_ok": 2.9893060086286356, "408_ok": 2.994370291651705, "400_ok": 3.004473249029238, "498_ok": 3.1641283142408883, "514_ok": 3.1713029710885787, "466_ok": 3.1784614328145944, "492_ok": 3.1879810445634553, "432_ok": 3.1998407329511673, "524_ok": 3.302369964573945, "475_ok": 3.3092449181610273, "511_ok": 3.3161056186178905, "480_ok": 3.316105618617898, "482_ok": 3.3206715441507115, "448_ok": 3.3229521542272695, "410_ok": 3.327508685125654, "477_ok": 3.32750868512566, "503_ok": 3.334331806380569, "389_ok": 3.33433180638059, "421_ok": 3.336603079509571, "464_ok": 3.341140993806751, "431_ok": 3.345672753094492, "518_ok": 3.3479363324218703, "474_ok": 3.3501983823501957, "420_ok": 3.3973535316895824, "437_ok": 3.3995827000435352, "456_ok": 3.4018104076486577, "451_ok": 3.4062614520746477, "418_ok": 3.4107066877984007, "441_ok": 3.417363699644413, "520_ok": 3.426219595451117, "440_ok": 3.4284299951150765, "486_ok": 3.432846524636343, "414_ok": 3.432846524636357, "433_ok": 3.4328465246363753, "490_ok": 3.4372573793667307, "438_ok": 3.4438630689191716, "471_ok": 3.4438630689192014, "412_ok": 3.446062151589402, "452_ok": 3.4460621515894028, "415_ok": 3.4482598318236706, "467_ok": 3.4504561123016786, "453_ok": 3.4504561123016977, "435_ok": 3.4504561123016986, "497_ok": 3.4548444846654074, "413_ok": 3.454844484665432, "425_ok": 3.4570365818681466, "444_ok": 3.4570365818681488, "428_ok": 3.45922728994875, "509_ok": 3.4636045492851864, "398_ok": 3.4636045492851966, "483_ok": 3.465791105791079, "390_ok": 3.4657911057910953, "489_ok": 3.4679762836749743, "485_ok": 3.4723425139860864, "461_ok": 3.4745235715975045, "487_ok": 3.4767032609554263, "510_ok": 3.4788815846317167, "450_ok": 3.4810585451901335, "436_ok": 3.483234145186448, "517_ok": 3.4854083871684525, "395_ok": 3.485408387168459, "397_ok": 3.485408387168468, "391_ok": 3.4854083871684822, "508_ok": 3.4854083871684907, "393_ok": 3.4875812736760254, "388_ok": 3.4875812736760587, "484_ok": 3.489752807241111, "516_ok": 3.489752807241123, "476_ok": 3.4897528072411244, "519_ok": 3.4897528072411257, "478_ok": 3.4897528072411363, "392_ok": 3.4940918256322835, "488_ok": 3.4940918256322844, "495_ok": 3.4940918256322884, "426_ok": 3.4962593154830217, "430_ok": 3.5005902689981863, "494_ok": 3.500590268998192, "513_ok": 3.500590268998205, "493_ok": 3.502753737640764, "507_ok": 3.502753737640766, "479_ok": 3.5027537376407696, "472_ok": 3.50275373764077, "496_ok": 3.5049158708459554, "512_ok": 3.5049158708459554}, "1": {"399_ok": 2.7386127875258293, "405_ok": 2.7386127875258293, "407_ok": 2.7748873851023204, "411_ok": 2.8106938645110375, "449_ok": 2.8106938645110375, "416_ok": 3.1144823004794855, "454_ok": 3.114482300479486, "505_ok": 3.3615472627943213, "515_ok": 3.449637662132067, "439_ok": 3.4496376621320675}}
```


© 2022 [Oleh Dmytrenko](https://github.com/OlehDmytrenko)
