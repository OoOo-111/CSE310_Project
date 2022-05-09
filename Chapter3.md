```
# Chapter 3
```
In Chapter03 folder we did followings in Raspberry pi

First of downloaded the dependencies with

- Pip3 install -r requirements.text

Then

- Flask run

If it gives pigpiod error , start the pigpiod deamon

- Sudo pigpiod

After flask run works correctly server should be running. It runs on 192.168.43.127:5000 in
our network.

Then we opened the client html file in our computer. Computer and raspberry pi connected
the same network. So we open the 192.168.43.127:5000 url with client html file. We were
able to change the light brightness value with the bar.

**Curl**

Curl -d “level=0” -X POST [http://192.168.43.127:5000/led](http://192.168.43.127:5000/led)

It changes the value of brightness with the curl. Instead of 0 we can type whatever we want.

Video Link: https://www.youtube.com/shorts/jgfSkuKdUOg


