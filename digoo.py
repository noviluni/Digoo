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
        self.player = vlc.MediaPlayer('rtsp://admin:20160404@{}/onvif1'.format(self.ip))
        self.lq_player = vlc.MediaPlayer('rtsp://admin:20160404@{}/onvif2'.format(self.ip))

    def generate_xml_body(self, x='0.0', y='0.0'):
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

    def move_camera(self, x='0.0', y='0.0'):
        """
        Move video to indicated coordenates.
        :param x: Values can get are 0.0 or 1.0
        :param y: Values can get are 0.0 or 1.0
        :return:
        """
        url = 'http://{}:5000/onvif/device_service'.format(self.ip)
        data = self.generate_xml_body(x, y)

        try:
            requests.post(url, headers=self.headers, data=data)
        except ConnectionError:
            Exception('Cannot connect with camera. Check the IP and try again.')

    def move_left(self):
        """
        Move camera left

        :return:
        """
        self.move_camera(x='-1.0')

    def move_right(self):
        """
        Move camera right

        :return:
        """
        self.move_camera(x='1.0')

    def move_up(self):
        """
        Move camera up

        :return:
        """
        self.move_camera(y='1.0')

    def move_down(self):
        """
        Move camera down

        :return:
        """
        self.move_camera(y='-1.0')

    def play_video(self):
        """
        Play video streaming with VLC

        :return:
        """
        self.player.play()

    def play_lq_video(self):
        """
        Play low quality video streaming with VLC

        :return:
        """
        self.lq_player.play()

    def stop_video(self):
        """
        Stop video streaming with VLC

        :return:
        """
        self.player.stop()

    def stop_lq_video(self):
        """
        Stop low quality video streaming with VLC

        :return:
        """
        self.lq_player.play()

    # def take_snapshot(self):
    #     """
    #     Takes a snapshot from video. Needs VLC and low quality video should be playing.
    #
    #     Seems that is not working on VLC 2.2. without changing configuration
    #      (https://bugs.launchpad.net/ubuntu/+source/vlc/+bug/1608232)
    #
    #     :return:
    #     """
    #
    #     snapshot_done = self.lq_player.video_take_snapshot(0, '.imagen.png', 0, 0)
    #     if not snapshot_done:
    #         print('There was an error and no snapshot was taken')
