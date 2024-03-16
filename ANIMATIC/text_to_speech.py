from speechkit import model_repository, configure_credentials, creds


# TEXT = 'Tell me, how do I get to the city center?'


def synthesize(text):
    
    configure_credentials(
        yandex_credentials=creds.YandexCredentials(
            api_key='AQVN0Oheok-sOHDYyn3HpCBFj2XDRxdA-x3IDv8E'
        )
    )

    model = model_repository.synthesis_model()
    model.voice = 'john'  # 'anton' - ru, 'john' - en
    # model.role = 'good'
    model.speed = 1.2
    result = model.synthesize(text, raw_format=False)
    result.export('test.wav', 'wav')


# if __name__ == '__main__':
# synthesize('Give me time to think!')
# tts
