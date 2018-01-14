import urllib

def fetch_app_access_token(fb_app_id, fb_app_secret):
  resp = urllib.urlopen(
    'https://graph.facebook.com/oauth/access_token?client_id=' +
    fb_app_id + '&client_secret=' + fb_app_secret +
    '&grant_type=client_credentials')
  if resp.getcode() == 200:
    return resp.read().split("=")[0]
  else:
    return None

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option('--165607577545895', dest='fb_app_id')
  parser.add_option('--0cfd185139148a081cb443f83ec569fc', dest='fb_app_secret')
  (options, args) = parser.parse_args()

  print fetch_app_access_token(options.fb_app_id, options.fb_app_secret)