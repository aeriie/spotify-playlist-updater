# Spotify Playlist Updater


#### A Python script to update Spotify Playlist data every 5 minutes.  


## Description

An automatic playlist updater using Spotify API and Authorization code flow in Python to update a Playlist on a repeating time interval. 

## Getting Started
#### You will need Python to execute the script:

* Python 3
    * [Installation Link](https://www.python.org/downloads/)

#### Spotify Playlist Updater requires three dependencies: 

#

##### Pip

* A Package Management System for Python.
* [Installation Link](https://pip.pypa.io/en/stable/installation/)
* For Windows, you can run ```py -m ensurepip --upgrade``` in CMD to install. 

##### Schedule
* Python job scheduler to run the script on a timer.
* [Installation Link](https://schedule.readthedocs.io/en/stable/installation.html)
* For Windows, you can run ```-m pip install schedule --upgrade``` in CMD to install. 

##### A Web Domain

* No website required, only a web domain for redirecting the API request and retrieving the user authorization token. 
* If you don't already own a domain, you can create one at [https//wix.com](https://wix.com)

##### Spotipy
* Python library for the Spotify Web API
* [Installation Link](https://spotipy.readthedocs.io/en/2.19.0/#installation)
* For Windows, you can run ``` py -m pip install spotipy --upgrade ``` in CMD to install. 


### Set Up

##### Installing the Script

* Install the dependencies listed above. 
* Choose a location on your device (I'll refer to this as the working directory)
* Download the latest release of [spotify-playlist-updater](https://github.com/aeriie/spotify-playlist-updater/) to the working directory. 
* Save your playlist photo (if applicable) in the ``data`` folder of the working directory
    * The photo must be 150KB or less. If it is too large, resize the photo. 
    * You can use this website to resize your image: https://www.resizepixel.com/reduce-image-in-kb/

##### Set up Client ID, Client Secret and Redirect URI
* Login to Spotify Developer Account
    * Go to https://developer.spotify.com/dashboard/ and click Manage Dashboard. 
    * Then, sign in with your Spotify credentials and accept the latest Developer terms of service.
    * Note your Client ID, and Client Secret. 
* Create an App
    * In the Developer Dashboard, create an App. You can put whatever you'd like for the App name and description. 
    * Click Edit Settings. 
        * Add your domain address to the Redirected URI's field, and click Add. Make sure to Save. 

##### Adding your Playlist information
* Right click \spotify-playlist-updater.py from the working directory, and select "Edit with IDLE"
   * Put your Playlist Image path in place of: ```` "C:\\Users\\You\\YourWorkingDirectory\\Data\\PlaylistPhoto.jpeg" ````
   * Put your Spotify Username in place of: ```` 'username' ````
   * Put your Client ID in place of ```` 'clientid' ````
   * Put your Client Secret in place of ```` 'clientsecret' ````
   * Put your Web Domain Address in place of ```` 'http://yourdomain.com' ````
   * Put your Spotify Playlist Link in place of ```` 'https://open.spotify.com/playlist/yourplaylist' ````
   * Put your Playlist Description in place of ```` 'Playlist Name' ````
   * Put your Playlist Description in place of ```` 'Playlist Description' ````
* **Save the script once your changes are made.** 



### Running the Script

* Right click spotify-playlist-updater.py and Open. 
* The script updates the Playlist every 5 minutes. You can adjust the update frequency by changing the number value for ```` schedule.every(5).minutes.do(func) ````
* The script will restart if it runs into a timeout to prevent it from failing during an internet hiccup. 
    * If you have an unstable internet connection and run into issues, try removing the ```` continue ```` statement. 

## Thank you

If you enjoyed my project, please feel free to leave tips on my [Ko-Fi. https://ko-fi.com/autumntillman](https://ko-fi.com/autumntillman)
or [Paypal](https://www.paypal.com/paypalme/autterpop?locale.x=en_US).

## Help

To report issues, create a new issue on Github or email [autumn@videogamelofi.com](mailto:autumn@videogamelofi.com)

## Authors

[Aeriie](https://github.com/aeriie) on GitHub

## Version History

* 0.1
    * Initial Release

