# Python Gurmukhi / Punjabi

During Image Processing, Pdf Writing Or Android Dvolpment Some Errors Occur Because Python Don't Render Gurmukhi Languge Correctly.
This Package Is Helpfull In Process That All Charecters Correctly.

## INSTALLATION
**Using Pip Or Pip3**
```shell
pip install pi7gurmukhi
```

## Pi7Gurmukhi Font 
**pi7font** Is A TTF(True Type Font) File Which Is Used For Process & Display Correct Text. 
You Can Download it From Here [`pi7gurmukhi.ttf`](https://github.com/shivjeetbhullar/pi7gurmukhi/raw/master/fonts/pi7gurmukhi.ttf) Or Check [`Github`](https://github.com/shivjeetbhullar/pi7gurmukhi/tree/master/fonts)

## How To Use?
We Will See How To Write Gurmukhi Font On Image With The Help Of Pillow Library.
`render_gurmukhi` Function Is Used To Modify Gurmukhi String & `pi7gurmukhi.ttf` File Is Used For Display Output
---
**NOTE**
Dont Forget To Download [`pi7gurmukhi.ttf`](https://github.com/shivjeetbhullar/pi7gurmukhi/raw/master/fonts/pi7gurmukhi.ttf) File And Use In Code.
---
```python
# -*- coding: utf-8 -*-
from pi7gurmukhi import render_gurmukhi
from PIL import Image, ImageDraw, ImageFont

# Dont Forget To Include pi7gurmukhi.ttf File Path Otherwise It Will Don't Work
Pi7TTfFile = "Path/To/pi7gurmukhi.ttf"
# Use render_gurmukhi Function For Correct Output
punjabi_text = render_gurmukhi(u"ਸ੍ਰੀ ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਜੀ \nਸ੍ਰੀ ਮੁਕਤਸਰ ਸਾਹਿਬ")

font_size=36
width=350
height=130
back_ground_color=(255,255,255)
font_color=(0,0,0)
im = Image.new ("RGB", (width,height), back_ground_color)
draw = ImageDraw.Draw (im)
unicode_font = ImageFont.truetype(Pi7TTfFile, font_size)
draw.text((10,10), punjabi_text, font=unicode_font, fill=font_color )
im.save("text.jpg")
```
### Output Using Pi7Gurmukhi Font And render_gurmukhi Function
**This Is Correct Output**
!["Correct Output"](https://raw.githubusercontent.com/shivjeetbhullar/pi7gurmukhi/master/images/correct.jpg)

### Output Without Pi7Gurmukhi Font And render_gurmukhi Function
**This Is Incorrect Output** Without Pi7Gurmukhi Font And Function.
!["Correct Output"](https://raw.githubusercontent.com/shivjeetbhullar/pi7gurmukhi/master/images/uncorrect.jpg)

Similarly You Can Use `pi7gurmukhi` For **Write Pdf Files**, **Devolpment Using Kivy, Tkinter etc**.
For Any Another Information Contact To `bhullarshivjeet@gmail.com` Or [`Message Me On Linkedin`](https://in.linkedin.com/in/shivjeet-bhullar-2ba36b169)
