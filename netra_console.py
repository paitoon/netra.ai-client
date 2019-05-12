import os
import logging
from netra.netra_client import NetraClient

log = logging.getLogger(__name__)

class NetraConsole:
    def __init__(self):
        self.netraClient = NetraClient()
    
    def run(self):
        log.info("Netra Console...")

        self.netraClient.connect('localhost', 5000, False)
        authorizeService = self.netraClient.getAuthorizeService()

        ret, _ = authorizeService.login('admin', 'password')
        if ret:
            log.info("login success.")
        else:
            log.info("fail.")

        ''' --> PASS
        faceGroupService = self.netraClient.getFaceGroupService()

        #ret, data = faceGroupService.get('g-able')
        #ret, data = faceGroupService.list()
        imageFiles = os.listdir('samples/paitoon')
        imageFilePaths = [os.path.join('samples/paitoon', imageFile) for imageFile in imageFiles]
        log.info(imageFilePaths)
        ret, data = faceGroupService.upload('g-able', 'paitoon', imageFilePaths)
        if ret:
            log.info("data : {}".format(data))
        else:
            log.info("fail.")
        '''
        
        ''' --> PASS
        objectDetectionService = self.netraClient.getObjectDetectionService()

        ret, data = objectDetectionService.getKnownObjects()
        if ret:
            log.info("data : {}".format(data))
        else:
            log.info("fail.")

        ret, data = objectDetectionService.detect('samples/hua-hin-railway-station.jpg', interestedObjects='person, dog')
        if ret:
            log.info("data : {}".format(data))
        else:
            log.info("fail.")
        '''

        faceService = self.netraClient.getFaceService()

        ret, data = faceService.detect('samples/people1.jpeg', attributes="gender")
        if ret:
            log.info("data : {}".format(data))
        else:
            log.info("fail.")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)-30.30s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.FileHandler("{0}/{1}.log".format("log", "netra-ai")),
            logging.StreamHandler()
        ])
    netraConsole = NetraConsole()
    netraConsole.run()
