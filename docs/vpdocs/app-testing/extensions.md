# appium 扩展

appium支持扩展，通过扩展来增强appium定位元素的能力。

## appium images-plugin

使用此插件支持的`-image`定位器策略，可以通过Appium指定想要定位的元素的图片文件。

* 安装Appium images-plugin插件。

```shell
> appium plugin install images
```

* 查看已安装的Appium插件。

```shell
> appium plugin list --installed
✔ Listing installed plugins
- images@2.1.8 [installed (npm)]
```

* 启动Appium server时指定使用OCR插件。

```shell
> appium server --address '127.0.0.1' -p 4723  --use-plugins=images
```

* 目录结构

```tree
├───test_appium_images.py
└───phone.jpg
```

* 编写App自动化测试脚本

```python
# test_appium_images.py
import seldom
from seldom.utils.file_extend import file
from seldom.appium_lab.android import UiAutomator2Options


class TestApp(seldom.TestCase):

    def test_app_images(self):
        self.wait(10)
        file_path = file.join(file.dir, "phone.jpg")
        self.click_image(file_path)


if __name__ == '__main__':
    capabilities = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "appPackage": "com.meizu.flyme.flymebbs",
        "appActivity": "com.meizu.myplus.ui.splash.SplashActivity",
        "noReset": True,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    seldom.main(app_server="http://127.0.0.1:4723", app_info=options)
```

通过`click_image()` 来点击图片匹配到整个页面上的元素的坐标位。

## Appium OCR plugin

* 安装Appium OCR plugin插件。

```shell
> appium plugin install images--source=npm appium-ocr-plugin
```

* 查看已安装的Appium插件。

```shell
> appium plugin list --installed
✔ Listing installed plugins
- ocr@0.2.0 [installed (npm)]
```

* 启动Appium server时指定使用OCR插件。

```shell
> appium server --address '127.0.0.1' -p 4723  --use-plugins=ocr
```

* 编写App自动测试脚本。

```python
# test_appium_orc.py
import seldom
from seldom.appium_lab.switch import Switch
from seldom.appium_lab.ocr_plugin import OCRCommand
from seldom.appium_lab.android import UiAutomator2Options


class TestApp(seldom.TestCase):
    def start(self):
        self.switch = Switch(self.driver)

    def test_orc_case(self):
        ocr = self.driver.ocr_command({})
        print(ocr)
        self.switch.switch_to_ocr()
        self.click(xpath='//words/item[text() = "Flyme"]')


if __name__ == '__main__':
    capabilities = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "appPackage": "com.meizu.flyme.flymebbs",
        "appActivity": "com.meizu.myplus.ui.splash.SplashActivity",
        "noReset": True,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    seldom.main(app_server="http://127.0.0.1:4723", app_info=options, extensions=[OCRCommand])
```

根据上面代码示例，打印ocr变量得到一个JSON结构体。

```json
{
  "words": [
    {
      "text": "mEngine",
      "confidence": 88.47775268554688,
      "bbox": {
        "x0": 86,
        "y0": 509,
        "x1": 308,
        "y1": 560
      }
    },
    {
      "text": "Flyme",
      "confidence": 91.3454818725586,
      "bbox": {
        "x0": 316,
        "y0": 1132,
        "x1": 420,
        "y1": 1172
      }
    },
    {
      "text": "A9",
      "confidence": 34.86248779296875,
      "bbox": {
        "x0": 1017,
        "y0": 2565,
        "x1": 1078,
        "y1": 2595
      }
    }
  ],
  "lines": [
    {
      "text": "mEngine BY Ni0vEh 1 Bl\n\n",
      "confidence": 21.003677368164062,
      "bbox": {
        "x0": 86,
        "y0": 500,
        "x1": 674,
        "y1": 560
      }
    },
    {
      "text": "Flyme\n\n",
      "confidence": 91.3454818725586,
      "bbox": {
        "x0": 316,
        "y0": 1132,
        "x1": 420,
        "y1": 1172
      }
    },
    {
      "text": "A9\n",
      "confidence": 34.86248779296875,
      "bbox": {
        "x0": 1017,
        "y0": 2565,
        "x1": 1078,
        "y1": 2595
      }
    }
  ],
  "blocks": [
    {
      "text": "mEngine BY Ni0vEh 1 Bl\n\n",
      "confidence": 21.003677368164062,
      "bbox": {
        "x0": 86,
        "y0": 500,
        "x1": 674,
        "y1": 560
      }
    },
    {
      "text": "Flyme\n\n",
      "confidence": 91.3454818725586,
      "bbox": {
        "x0": 316,
        "y0": 1132,
        "x1": 420,
        "y1": 1172
      }
    },
    {
      "text": "A9\n",
      "confidence": 34.86248779296875,
      "bbox": {
        "x0": 1017,
        "y0": 2565,
        "x1": 1078,
        "y1": 2595
      }
    }
  ]
}
```

JSON结构体说明：

* wrods - Tesseract识别的单个单词的列表。

* lines - Tesseract识别的文本行的列表。

* blocks - Tesseract识别连续文本块的列表。

每项都引用一个OCR对象，它们本身包含3个数据：

- text：识别的文本。
- confidence：Tesseract对于给定文本的OCR处理结果的置信度（范围在0到100之间）。
- bbox：发现文本的边界框，`边界框`标记为x0、x1、y0和y1的值的对象。分别表文本的上下左右坐标位置，其中。这里，x0表示发现文本的左边x坐标，x1表示右边x坐标，y0表示上部y坐标，y1表示下部y坐标。

