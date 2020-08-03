from flask import Flask, render_template, request, abort
from news_search import search_keyword,search_writer
app = Flask(__name__)


@app.route('/')
def keyword_index():
    return render_template('keyword.html')


@app.route('/writer')
def writer_index():
    return render_template('writer.html')


@app.route("/keyword_result", methods=['GET'])
def keyword_result():
    if request.method == 'GET':
        keyword = request.args.get('keyword')
        if keyword == '':
            abort(400, 'keyword is not inserted, pleased try again')
        operator = request.args.getlist('operator')
        start = request.args.get('start')
        if start == '':
            start = None

        end = request.args.get('end')
        if end == '':
            end = None

    result, total = search_keyword(keyword=keyword, operator=operator, start =start, end = end)
    return render_template('keyword_result.html', keyword=keyword, result = result, total=total)


@app.route("/writer_result", methods=['GET'])
def writer_result():
    if request.method == 'GET':
        writer = request.args.get('writer')
        if writer == '':
            abort(400, 'writer is not inserted, pleased try again')
        operator = request.args.getlist('operator')
        start = request.args.get('start')
        if start == '':
            start = None

        end = request.args.get('end')
        if end == '':
            end = None

    result, total = search_writer(writer=writer, operator=operator, start =start, end = end)
    return render_template('keyword_result.html', writer = writer, result = result, total=total)


if __name__ == '__main__':
    app.run(use_reloader=False)
