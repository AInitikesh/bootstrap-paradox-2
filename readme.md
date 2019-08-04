Instructions to run

## Usage
 
 * Open in browser http://3.90.155.174:5000/#
 * click upload file
 * upload the .mp4 file > once uploaded successfully you will be redirected to home page
 * click start button to start the real time streaming
 * click stop button to stop the real time streaming
 * you can select between various models
* * DeepLab - 10-15 fps
* * MobileNet v2 - 20-25 fps
* * MobileNet v2_lite - 30+ fps


## Download models
make 'data' directory
copy below files from google drive to 'data' directory

|   Drive link                                                       | File Name                       |
| ------------------------------------------------------------------ | ------------------------------- |
| https://drive.google.com/open?id=1RNvExC2J0vror1-yqulrfSLDBxJD6WT3 | deeplab_frozen_graph.pb         |
| https://drive.google.com/open?id=1im-EYoMZmJAJaRruBnFLz87e5i_MT4fC | frozen_inference_graph_mv_lt.pb |
| https://drive.google.com/open?id=1Jd59ueTtU5BQUcRUS8ULDufNi7I9-e0F | frozen_inference_graph_mv2.pb   |

## Create anaconda environment

```
conda env create -f environment.yml
```

## Run the code 
```
python app.py
```

## Usage
 
 * Open in browser http://localhost:5000
 * click upload file
 * upload the .mp4 file > once uploaded successfully you will be redirected to home page
 * click start button to start the real time streaming
 * click stop button to stop the real time streaming
 * you can select between various models
* * DeepLab - 10-15 fps
* * MobileNet v2 - 20-25 fps
* * MobileNet v2_lite - 30+ fps

