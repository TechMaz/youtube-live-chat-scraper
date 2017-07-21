# youtube-live-chat-scraper
Selenium Python app to scrape html from a Youtube Live Chat window.  

Run locally and call `http://localhost:5000/scrape/<id>`, with `<id>` being the video id from Youtube, to get an array of json chat messages from that live stream.

This service is accessed by [https://github.com/TechMaz/youtube-live-parser/](https://github.com/TechMaz/youtube-live-parser/) in order to display chats side by side with live video. Please refer to that repository for more information.
