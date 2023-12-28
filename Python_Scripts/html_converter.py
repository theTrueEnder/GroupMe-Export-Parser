import html
import webbrowser

HEADER = '''<!DOCTYPE html>
<html lang="en">

<head>
    <title>GroupMe Conversation Export</title>
    <link rel="stylesheet" href="styles.scss">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=PT+Sans&family=Vollkorn:wght@700&display=swap" rel="stylesheet"> 
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
'''


def string_to_html(string):
    string.replace('\n', '<br>')
    return html.escape(string, quote=True)


def append_html_message(msg, body, settings):
    hh_mm, date = msg.time.split(' ')
    name = msg.nickname if settings['nicknames'] else msg.name 
    image_attachment_html = ''
    for a in msg.attachments:
        if a.type == 'image':
            image_attachment_html = f'<img src="{a.image_url}" class="card__image__attachment" alt="GroupMe Image" />'
            break # only one image per message ###############################

    html_text = \
    f'''
    <div class="card">
        <img src="{msg.avatar_url}" class="card__image" alt="GroupMe Image"/>
        <div class="card__content">
        <time datetime="{hh_mm}" class="card__date"> <b>{name}</b> at {hh_mm} on {date}</time>
        <span class="card__title">{msg.text}<span>
        </div>
            {image_attachment_html}
    </div>
    '''
    # body += html_text
    return html_text


def convert(msgs, settings, filepath):
    body = ''
    count = 0
    for msg in msgs:
        count += 1
        t = append_html_message(msg, body, settings)
        try:
            with open(filepath + 'output.html', 'a', errors='namereplace') as f:
                f.write(t)
        except Exception as e:
            print('Line', count)
            print(t)
            
    
    # try:
    #     with open(filepath + 'output.html', 'w') as f:
    #         f.write(string_to_html(HEADER + body))
    #     webbrowser.open(filepath + 'output.html')
    # except Exception as e:
    #     print()
# <p class="special">What color am I?</p>

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