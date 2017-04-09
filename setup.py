from setuptools import setup

def isInt(value):
	return isinstance(value, (int,))

def formatversion(major, minor, maintenance = None):
	assert(isInt(major) and isInt(minor))
	version = [major, minor]
	if(maintenance is not None):
		assert(isInt(maintenance))
		version.append(maintenance)
	return ".".join(str(n) for n in version)

VERSION = formatversion(1,0,0)
GIT_REPO = "https://github.com/wrenoud/em_datagram"

setup(
  name = 'em_datagram',
  packages = ['em_datagram'], # this must be the same as the name above
  version = VERSION,
  description = 'Module for parsing EM Series datagram formats',
  author = 'Weston Renoud',
  author_email = 'wrenoud@gmail.com',
  url = GIT_REPO, # use the URL to the github repo
  download_url = '{}/tarball/v{}'.format(GIT_REPO, VERSION),
  keywords = ['struct', 'binary', 'data structures'], # arbitrary keywords
  classifiers = [],
  install_requires=[
    'structobject',
  ],
)
