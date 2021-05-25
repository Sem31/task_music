import apiRequests
import os

class TestCase:

    def test_create_song_API(self) :
        try :
            path = os.getcwd() + '/music/music.mp3'
            send_files = {'upload_song': open(path, 'rb')}
            payload = {
                "song_name" : "kamlesh"
            }
            data = apiRequests.post(payload, send_files)
            res = data.json()
            assert res['song_name'] == payload['song_name']
            assert data.status_code == 201
        except Exception as e:
            raise Exception(repr(e))
        finally :
            res = apiRequests.delete(res['id'])

    def test_get_song_API(self) :
        data = apiRequests.get()
        assert data.status_code == 200

    def test_delete_song_API(self) :
        path = os.getcwd() + '/music/music.mp3'
        send_files = {'upload_song': open(path, 'rb')}
        payload = {
            "song_name" : "kamlesh"
        }
        data = apiRequests.post(payload, send_files)
        res = data.json()
        data = apiRequests.delete(res['id'])
        assert data.status_code == 204

    def test_update_data(self) :
        path = os.getcwd() + '/music/music.mp3'
        send_files = {'upload_song': open(path, 'rb')}
        payload = {
            "song_name" : "kamlesh"
        }
        data = apiRequests.post(payload, send_files)
        res = data.json()
        try:
            payload = {
            "song_name" : "sem"
            }
            data = apiRequests.patch(res['id'],payload)
            res = data.json()
            assert data.status_code == 200
        except Exception as e:
            raise Exception(repr(e))
        finally :
            res = apiRequests.delete(res['id'])
        
            
