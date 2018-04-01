# Digoo

Python script to use Digoo ip cams.


**Note**: Tested with **Digoo BB-M1X** (*Digoo Camera M-series M1X*) also called *Digoo BB-MIX Mini IP Camera* over Linux. It should work with other Digoo IP cams.


## How to use

### Initialization:

```python
from digoo import Digoo
d = Digoo('<your-cam-ip>')
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


To stop video just use:

```python
d.stop_video()
```

You can also play a **low quality video** streaming with the next command:

```python
d.play_lq_video()
```

And stop it with:

```python
d.stop_lq_video()
```


## Requirements

### Python Requirements

* python-vlc

### System Requirements

* Python 3
* VLC


## Acknowledgments

Based on some ideas taken from:  https://github.com/felixsteghofer/digoo-m1x_hacks


## Next/TODO

It could be nice to implement a way to take an snapshot. Some code is written and commented.

I would like also to hide VLC error messages.


## License

GPLv3
