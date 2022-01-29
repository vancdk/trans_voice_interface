from flask import Flask, render_template, request, redirect
from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/record")
def record_page():
	return render_template('record.html')


@app.route("/<media>")
def voice_analysis(media):
	seg = Segmenter()
	segmentation = seg(media)
	segmentation_dispayed =  ', '.join(map(str,segmentation))
	return segmentation_dispayed

@app.route("/result", methods=["GET", "POST"])
def result():
	segmentation=""
	if request.method == "POST":
		print("AUDIO DATA RECEIVED")
		if "file" not in request.files:
			return redirect(request.url)

		file = request.files["file"]
		if file.filename == "":
			return redirect(request.url)

		if file:
			seg = Segmenter()
			segmentation = seg(file)
			segmentation_dispayed =  ', '.join(map(str,segmentation))
			print(segmentation_dispayed)
	return render_template('result.html', segmentation=segmentation)






if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

