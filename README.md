
# Digoo

Python script to use Digoo ip cams.


**Note**: Tested with **Digoo BB-M1X** (*Digoo Camera M-series M1X*) also called *Digoo BB-MIX Mini IP Camera* over Linux. It should work with other Digoo IP cams like *Digoo BB-M1Q*.


## How to use

### Initialization:

```python
from digoo import Digoo
d = Digoo('<your-cam-ip-address>')
```


### Movements

To move **horizontally**, you can use:

```python
d.move_left()
```

and

 ```python
d.move_right()
  ```

To move **vertically** you can use:

```python
d.move_up()
```

and

 ```python
d.move_down()
  ```

### Video streaming

It's possible to play video streaming using VLC Player.

```python
d.play_video()
```

In this moment, errors are shown in console, however you can use the script and move the camera without stopping the video.

You can also play a **low quality video** streaming adding `hd=False`

```python
d.play_video(hd=False)
```

To stop the video streaming just use:

```python
d.stop_video()
```


### Video snapshot

It's possible to take a snapshot from the currently streaming video (experimental feature). To do it just use:

```python
d.take_snapshot()
```

The quality of the image depends of the quality of the streaming video (low quality or high definition). If there is not streaming video playing, a notice is going to be shown on console and no snapshot is going to be taken.

*Note: It seems that there is a bug in VLC 2 that doesn't allow to take snapshots (https://bugs.launchpad.net/ubuntu/+source/vlc/+bug/1608232).
If you need this feature try to update to VLC 3.*


## Requirements

### Python Requirements

* requests
* python-vlc

### System Requirements

* Python 3
* VLC


## Acknowledgments

Based on some ideas taken from:  https://github.com/felixsteghofer/digoo-m1x_hacks


## Next/TODO

I would like to hide VLC error messages.


## License

GPLv3
