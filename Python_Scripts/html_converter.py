import html
import webbrowser

def string_to_html(string):
    string.replace('\n', '<br>')
    return html.escape(string, quote=True)

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