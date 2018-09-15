import gdata.youtube
import gdata.youtube.service
yt_service = gdata.youtube.service.YouTubeService()

yt_service.developer_key = 'AIzaSyB4npSjJ7nlyDpIyjC2eiDGVHnomLP_bNs'
# yt_service.client_id = '992095518153-ucsohpb3emcu3glri3ojn62e8fdkvi8g.apps.googleusercontent.com'

def GetAuthSubUrl():
    next = 'http://www.example.com/video_upload.pyc'
    scope = 'http://gdata.youtube.com'
    secure = False
    session = True

    yt_service = gdata.youtube.service.YouTubeService()
    return yt_service.GenerateAuthSubURL(next, scope, secure, session)

    authSubUrl = GetAuthSubUrl()
    print ('<a href="%s">Login to your Google account</a>' % authSubUrl)

