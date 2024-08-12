from flask import render_template, redirect, request, url_for
import flask
from SmTools.fbExtractor import FacebookPostLinkExtractor
from SmTools.ytCounter import YoutubeCounter
from SmTools.twExtractor import TwitchExtractor

app = flask.Flask(__name__)
link_extractor = FacebookPostLinkExtractor()
views_counter = YoutubeCounter()
tw_extractor = TwitchExtractor()

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/articles')
def articles():
    return render_template('articles.html', active_page='articles')

@app.route('/facebook-link-extractor', methods=['GET', 'POST'])
def facebook_link_extractor():
    if request.method == 'POST':
        link = request.form.get('facebook-link')
        post_link = link_extractor.get_facebook_post_link(link)
        return render_template('fb-tool.html', result=post_link, active_page='sm-tool')
    return render_template('fb-tool.html', active_page='sm-tool')

@app.route('/youtube-views-counter', methods=['GET', 'POST'])
def youtube_views_counter():
    if request.method == 'POST':
        link = request.form.get('youtube-link')
        view_count = views_counter.count_views(link)
        return render_template('yt-tool.html', result=view_count, active_page='sm-tool')
    return render_template('yt-tool.html', active_page='sm-tool')

@app.route('/twitch-clips-link-extractor', methods=['GET', 'POST'])
def twitch_clips_link_extractor():
    if request.method == 'POST':
        link = request.form.get('twitch-link')
        new_url = tw_extractor.create_url(link)
        return render_template('tc-tool.html', result=new_url, active_page='sm-tool')
    return render_template('tc-tool.html', active_page='sm-tool')

if __name__ == '__main__':
    app.run(debug=True)
