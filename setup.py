from distutils.core import setup


setup(name='BitEx', version='2.0.0', author='Nils Diefenbach',
      author_email='23okrs20+pypi@mykolab.com',
      url="https://github.com/nlsdfnbch/bitex.git",
      packages=['bitex'],
      install_requires=['requests', 'websocket-client', 'autobahn',
                        'pusherclient', 'pyjwt'],
      description='Python3-based API Framework for Crypto Exchanges',
      license='MIT',  classifiers=['Development Status :: 4 - Beta',
                                   'Intended Audience :: Developers'],
      )

