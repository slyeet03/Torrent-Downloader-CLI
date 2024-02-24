from qbittorrent import Client

# connecting to the web ui
qb= Client("http://127.0.0.1:8080/")

# creds
qb.login("admin", "password") # replace it with your user and password from qbittorrent

# downloading torrent
def torrent_download(magnet_link, output_path):
	qb.download_from_link(magnet_link, savepath=output_path)