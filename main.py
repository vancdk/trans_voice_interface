from flask import Flask, render_template, request, redirect
from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

app = Flask(__name__)

#HOTFIX On initialise une fois pour toutes au debut
seg = Segmenter()

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/record")
def record_page():
	return render_template('record.html')


@app.route("/<media>")
def voice_analysis(media):
	app.logger.info('voice analysis', media)
#HOTFIX On  initialise une fois pour toutes au debut
#	seg = Segmenter()
	segmentation = seg(media)
	segmentation_dispayed =  ', '.join(map(str,segmentation))
	return segmentation_dispayed

@app.route("/result", methods=["GET", "POST"])
def result():
	app.logger.info('IN RESULT')
	segmentation=""
	#HOTFIX  On enregistre le fichier en local tmp
	if request.method == "POST":
		print("AUDIO DATA RECEIVED")
		app.logger.info('IN RESULT POSTPOST')
		print('request1', request)
		print('request2', request.files)
		print('request3', request.files['audio_data'])
		request.files['audio_data'].save('/tmp/toto.wav')
#		if "file" not in request.files:
#			return redirect(request.url)
#			
#		print('request2', request.file)
#		file = request.files["file"]
#		if file.filename == "":
#			return redirect(request.url)
#
#		if file:
#		seg = Segmenter()
		segmentation = seg('/tmp/toto.wav')
		segmentation_dispayed =  ', '.join(map(str,segmentation))
		print(segmentation_dispayed)
	app.logger.info('IN RESULT END')
	return render_template('result.html', segmentation=segmentation)






if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

