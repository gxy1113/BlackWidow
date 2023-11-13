from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import json
import pprint
import argparse

from Classes import *

app_url =  {
     "wordpress":"http://webapp1.csl.toronto.edu:8080/wp-login.php",
     "wordpress2":"http://wordpressnf5.csl.toronto.edu/wp-login.php",
     "drupal":"http://webapp1.csl.toronto.edu:9200/user/login",
     "humhub":"http://webapp1.csl.toronto.edu:8300/index.php?r=user%2Fauth%2Flogin",
     "impresscms":"http://webapp1.csl.toronto.edu:8600/user.php",
     "matomo":"http://matomoxss.csl.toronto.edu/",
     "hotcrp":"http://webapp1.csl.toronto.edu:8500/testconf/",
     "gitlab":"http://gitlab1101.csl.toronto.edu/",
     "opencart":"http://webapp1.csl.toronto.edu:8800/test/",
     "dokuwiki":"http://webapp1.csl.toronto.edu:8400/doku.php?id=wiki:welcome&do=login",
     "kanboard":"http://webapp1.csl.toronto.edu:8200/",
     "phpbb": "http://webapp1.csl.toronto.edu:8700/index.php",
     "wackopicko": "http://10.99.0.187:8080/users/login.php"
}


parser = argparse.ArgumentParser(description='Crawler')
parser.add_argument("--debug", action='store_true',  help="Dont use path deconstruction and recon scan. Good for testing single URL")
parser.add_argument("--url", help="Custom URL to crawl")
parser.add_argument("--app", help="Custom Application to crawl")
parser.add_argument("--crawler", action='store_true', help="Only run the crawler")
parser.add_argument("--form_tester", action='store_true', help='Run the form tester')
args = parser.parse_args()

url = args.url
if args.app:
    url = app_url[args.app]
print("URL: " + url)

# Clean form_files/dynamic
root_dirname = os.path.dirname(__file__)
dynamic_path = os.path.join(root_dirname, 'form_files', 'dynamic')
for f in os.listdir(dynamic_path):
    os.remove(os.path.join(dynamic_path, f))

WebDriver.add_script = add_script


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-xss-auditor")

# launch Chrome
driver = webdriver.Chrome(chrome_options = chrome_options)



#driver.set_window_position(-1700,0)

# Read scripts and add script which will be executed when the page starts loading
## JS libraries from JaK crawler, with minor improvements
driver.add_script( open("js/lib.js", "r").read() )
driver.add_script( open("js/property_obs.js", "r").read() )
driver.add_script( open("js/md5.js", "r").read() )
driver.add_script( open("js/addeventlistener_wrapper.js", "r").read() )
driver.add_script( open("js/timing_wrapper.js", "r").read() )
driver.add_script( open("js/window_wrapper.js", "r").read() )
# Black Widow additions
driver.add_script( open("js/forms.js", "r").read() )
driver.add_script( open("js/xss_xhr.js", "r").read() )
driver.add_script( open("js/remove_alerts.js", "r").read() )
#rrweb additions
#driver.add_script( open("js/rrweb-record.min.js", "r").read() )
#driver.add_script( open("js/event.js", "r").read() )


if args.url or args.app:
    if args.form_tester:
        Crawler(driver, url).form_test(driver, args.debug)
    else:
        Crawler(driver, url).start(args.debug, args.crawler)
else:
    print("Please use --url")


