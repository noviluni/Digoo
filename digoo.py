import requests
import vlc


class Digoo:

    def __init__(self, ip):
        """
        Create digoo instance

        :param ip: Camera IP
        """
        self.ip = ip
        self.headers = {'Content-Type': 'application/soap+xml'}
        self._hd_player = vlc.MediaPlayer('rtsp://admin:20160404@{}/onvif1'.format(self.ip))
        self._lq_player = vlc.MediaPlayer('rtsp://admin:20160404@{}/onvif2'.format(self.ip))

    #############
    # MOVEMENTS #
    #############

    def _generate_xml_body(self, x='0.0', y='0.0'):
        """
        Generate xml body to move camera (SOAP).

        :param x: Values can get are 0.0 or 1.0
        :param y: Values can get are 0.0 or 1.0
        :return:
        """
        data = '''<v:Envelope 
            xmlns:i="http://www.w3.org/2001/XMLSchema-instance" 
            xmlns:d="http://www.w3.org/2001/XMLSchema" 
            xmlns:c="http://www.w3.org/2003/05/soap-encoding" 
            xmlns:v="http://www.w3.org/2003/05/soap-envelope">
            <v:Header>
                <Security v:mustUnderstand="1" 
                    xmlns="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
                    <UsernameToken 
                        xmlns="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
                        <Username>admin</Username>
                        <Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">tada_your_non_exisisting_password=</Password>
                        <Nonce>non_existing_nonce</Nonce>
                        <Created 
                            xmlns="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">2018-01-16T11:43:32Z
                        </Created>
                    </UsernameToken>
                </Security>
            </v:Header>
            <v:Body>
                <ContinuousMove 
                    xmlns="http://www.onvif.org/ver20/ptz/wsdl">
                    <ProfileToken>IPCProfilesToken0</ProfileToken>
                    <Velocity>
                        <PanTilt 
                            xmlns="http://www.onvif.org/ver10/schema" x="{}" y="{}"/>
                    </Velocity>
                </ContinuousMove>
            </v:Body>
        </v:Envelope>'''.format(x, y)
        return data

    def _move_camera(self, x='0.0', y='0.0'):
        """
        Move video to indicated coordenates.
        :param x: Values can get are 0.0 or 1.0
        :param y: Values can get are 0.0 or 1.0
        :return:
        """
        url = 'http://{}:5000/onvif/device_service'.format(self.ip)
        data = self._generate_xml_body(x, y)

        try:
            requests.post(url, headers=self.headers, data=data)
        except ConnectionError:
            ConnectionError('Cannot connect with the Digoo camera. Check that the camera is connected to the network '
                            'and powered on, your computer is in the same LAN and the IP address you have entered is '
                            'correct.')

    def move_left(self):
        """
        Move camera left

        :return:
        """
        self._move_camera(x='-1.0')

    def move_right(self):
        """
        Move camera right

        :return:
        """
        self._move_camera(x='1.0')

    def move_up(self):
        """
        Move camera up

        :return:
        """
        self._move_camera(y='1.0')

    def move_down(self):
        """
        Move camera down

        :return:
        """
        self._move_camera(y='-1.0')

    #########
    # VIDEO #
    #########

    def _play_hd_video(self):
        """
        Play video streaming with VLC

        :return:
        """
        self._hd_player.play()

    def _stop_hd_video(self):
        """
        Stop video streaming with VLC

        :return:
        """
        self._hd_player.stop()

    def _play_lq_video(self):
        """
        Play low quality video streaming with VLC

        :return:
        """
        self._lq_player.play()

    def _stop_lq_video(self):
        """
        Stop low quality video streaming with VLC

        :return:
        """
        self._lq_player.stop()

    def play_video(self, hd=True):
        """
        Play video streaming with VLC.

        :param hd: determine if video is in High Definition or in low quality
        :return:
        """
        if hd:
            self._play_hd_video()
        else:
            self._play_lq_video()

    def stop_video(self):
        """
        Stop video streaming with VLC

        :return:
        """

        if self._hd_player.is_playing() > 0:
            self._stop_hd_video()
        else:
            self._stop_lq_video()

    def take_snapshot(self, image_name=''):
        """
        Take a snapshot from video.

        Take a snapshot from video and save it with the given name (image_name). If no image_name is provided a default
        name is given. Needs VLC and video should be playing.

        NOTE: Seems that is not working on VLC 2.2 without changing configuration
         (https://bugs.launchpad.net/ubuntu/+source/vlc/+bug/1608232). If you need this
         function try to update VLC to 3.0 version.

        :param image_name:
        :return:
        """
        name = image_name if image_name else '.image.png'

        if self._hd_player.is_playing() > 0:
            self._lq_player.video_take_snapshot(0, name, 0, 0)

        elif self._lq_player.is_playing() > 0:
            self._lq_player.video_take_snapshot(0, name, 0, 0)
        else:
            print("It's necessary to play the video in order to take a snapshot.")
