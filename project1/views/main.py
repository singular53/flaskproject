from flask import render_template,Blueprint

book = {
    'title': '天下无双',
    'name': '失落叶',
    'article': [
        {
            'id': 1,
            'chapter': '第一章 -  惊变',
            'content': '一阵尖利的刹车声在公路上响起，鲜血横流，一个女人躺在了马路上，身下满是鲜血，出车祸了！'
        },
        {
            'id': 2,
            'chapter': '第二章 -  死灵剑士',
            'content': '吃掉了半斤牛肉，喝掉几杯酒，身体却并不是很暖和，很是奇怪。'
        },
        {
            'id': 3,
            'chapter': '第三章 -  超级大耳兔',
            'content': '这是我的第一反应，嗯，该冲上去把它做了，说不定能把手里的法杖爆出来，这法杖看起来不错的样子。'
        }
    ]
}


mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    articles = book['article']
    return render_template('index.html', **locals())


@mainbp.route('/<int:pk>')
def detail(pk):
    article = None
    for a in book['article']:
        if a['id'] == pk:
            article = a
    return render_template('detail.html', **locals())