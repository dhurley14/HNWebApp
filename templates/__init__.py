from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def final (greeting,greeting2):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<center>\n'])
    extend_([u'<title>HN Birthday Countdown</title>\n'])
    extend_([u'<div style="background-color:#ff6600;min-height:25px;width:85%;">\n'])
    extend_([u'</div>\n'])
    extend_([u'<h1 style="font-family:Verdana;">HN Birthday Countdown!</h1>\n'])
    extend_([u'<body style="font-family:Verdana;background-color:#f6f6ef;">\n'])
    extend_([escape_(greeting, True), u'<br>', escape_(greeting2, True), u'\n'])
    extend_([u'</center>\n'])
    extend_([u'</body>\n'])
    extend_([u'<footer style="width:100%;height:28px;border-top:1px solid #000000;left:0px;text-align:center;position:absolute;bottom:0;font-size:8pt;">\n'])
    extend_([u'Made by dev1n on HN using the very cool <a href="https://www.hnsearch.com/api">HNSearch</a> API\n'])
    extend_([u'</footer>\n'])

    return self

final = CompiledTemplate(final, 'templates/final.html')
join_ = final._join; escape_ = final._escape

# coding: utf-8
def register(form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<title>HN Birthday Countdown</title>\n'])
    extend_([u'<center>\n'])
    extend_([u'<div style="background-color:#ff6600;min-height:25px;width:85%;">\n'])
    extend_([u'</div>\n'])
    extend_([u'<h1 style="font-family:Verdana;">HN Birthday Countdown!</h1>\n'])
    extend_([u'<body style="font-family:Verdana;background-color:#f6f6ef;">\n'])
    extend_([u'Your HN Birthday is the day you created an account on HN!<br>To find out how long\n'])
    extend_([u'until your next HN Birthday, enter your username below!\n'])
    extend_([u'<form method="POST">\n'])
    extend_([u'    ', escape_(form.render(), False), u'\n'])
    extend_([u'</form>\n'])
    extend_([u'</body>\n'])
    extend_([u'</center>\n'])
    extend_([u'<center>\n'])
    extend_([u'<footer style="width:100%;height:28px;border-top:1px solid #000000;left:0px;text-align:center;position:absolute;bottom:0;font-size:8pt;">\n'])
    extend_([u'Made by dev1n on HN using the very cool <a href="https://www.hnsearch.com/api">HNSearch</a> API\n'])
    extend_([u'</footer>\n'])
    extend_([u'</center>\n'])

    return self

register = CompiledTemplate(register, 'templates/register.html')
join_ = register._join; escape_ = register._escape

