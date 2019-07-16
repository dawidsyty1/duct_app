from duct import settings
import requests
import logging


class AuthorizeOpenBankError(Exception):
    """ Authorization Open bank exception """
    pass


class AuthorizeOpenBank(object):
    @property
    def login_url(self):
        return '{0}/my/logins/direct'.format(settings.ODB_BASE_URL)

    @property
    def login_header(self):
        content = 'DirectLogin username={username},password={password},consumer_key={consumer_key}'.format(
            username=settings.CONSUMER_USERNAME,
            password=settings.CONSUMER_PASSWORD,
            consumer_key=settings.CONSUMER_PASSWORD
        )

        return {'Authorization': content}

    @property
    def authorization_token(self):
        response = requests.post(self.login_url, headers=self.login_header)

        logging.debug("Authorization response.status_code {} content {}".format(response.status_code, response.content))

        if response.status_code == 201:
            token = response.json()['token']
            logging.debug(token)

        # return redirect(url_for('general.home'))
