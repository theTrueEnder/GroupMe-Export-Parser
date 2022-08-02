import html
import webbrowser

html_text = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GroupMe Conversation Export</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        XXX
    </body>
</html>
            '''
def string_to_html(string):
    string.replace('\n', '<br>')
    return html.escape(string, quote=True)

def image_to_html(image):
    return f'<img src="{image.url}" style="{image.style}">'

def video_to_html(video):
    return f'''
            <video width="{video.video_width}" height="{video.video_height}" controls>
                <source src="{video.url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            '''

def add(text):
    i = html_text.index('</body>') - 5
    html_text = html_text[:i] + text + html_text[i:]

def convert(msgs, filepath):
    ...
    with open(filepath, 'w') as f:
        f.write(html)


# image url:            "https://i.groupme.com/1242x2688.jpeg.80f237141d2c4ea5b24f2aab258c74af"
# video url:            "https://v.groupme.com/70094573/2022-05-05T17:17:04Z/7b6441f.1920x1080r90.mp4"
# video preview url:    "https://v.groupme.com/70094573/2022-05-05T17:17:04Z/7b6441f.1920x1080r90.jpg"


'''
Image HTML:
<img src=url style="width: 1242px; height: 2688px;">
<img src=self.image_url style=self.style>

Video HTML:
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

<video width=self.video_width height=self.video_height controls>
  <source src=self.url type="video/mp4">
  Your browser does not support the video tag.
</video>

'''