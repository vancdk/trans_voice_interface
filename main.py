from flask import Flask
from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

app = Flask(__name__)


@app.route("/")
def index():
    return "Félicitations, c'est en ligne!"

@app.route("/<media>")
def voice_analysis(media):
	seg = Segmenter()
	segmentation = seg(media)
	segmentation_dispayed =  ', '.join(map(str,segmentation))
	return segmentation_dispayed


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

