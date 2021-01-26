<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="images/socket.png" alt="Logo" width="308" height="320">
    </br>
    Image by <a href="https://pixabay.com/users/clker-free-vector-images-3736/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=43918">Clker-Free-Vector-Images</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=43918">Pixabay</a>

  <h2 align="center">Smart plug</h2>

  <p align="center">
    Never worry about plugging your laptop again
  </p>
  </br>

</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

For a good care of your battery you must be really careful when plugging and unplugging your laptop to an outlet. Letting the battery run out to 0% reduces the remaining battery cycles. On the other side, letting the battery go over 100% could potentially damage it over time.

In this scenario it is really difficult to have a fully functional workstation with your laptop as you need to take care of your battery several times a day. The goal of this project is to take care of your laptop battery for you.

### Built With

* [IFTTT](https://ifttt.com)
* [SmartThings](https://www.smartthings.com)
* [Amazon Alexa](https://apps.apple.com/us/app/amazon-alexa/id944011620)
* [Smart plug](https://www.amazon.com.mx/dp/B07CJW3DFK?tag=googhydr0mx-20&hvadid=472472174621&hvpos=&hvexid=&hvnetw=g&hvrand=14840612331741170348&hvpone=&hvptwo=&hvqmt=e&hvdev=c&ref=pd_sl_2qmk3c6rgz_e&hvtargid=kwd-314688103100)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
* [python 3](https://www.python.org/downloads/)
* pip
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
* [IFTTT account](https://ifttt.com/join)
* [SmartThings account](https://us.account.samsung.com/accounts/v1/ST/terms#)
* [Amazon Alexa app](https://www.amazon.com.mx/gp/help/customer/display.html?nodeId=GMR4JYXHYDSTNQRK)
* [Amazon smart plug](https://www.amazon.com.mx/dp/B07CJW3DFK?tag=googhydr0mx-20&hvadid=472472174621&hvpos=&hvexid=&hvnetw=g&hvrand=14840612331741170348&hvpone=&hvptwo=&hvqmt=e&hvdev=c&ref=pd_sl_2qmk3c6rgz_e&hvtargid=kwd-314688103100): You can get one from less than 28 dollars


### Installation

1. Clone the repository
```sh
git clone git@github.com:Diezaztek/Smart-plug.git
```

2. Change to the project folder
```sh
cd Smart-plug
```

3. Install python dependencies in the requirements file
```sh
pip install -r requirements.txt
```

4. Login in Smarthings Developer and go to My Device Handlers then click on Create New Device Handler

5. Select create from code and paste the content of simulated-alexa-button.groovy. Feel free to change line 15 with a custom name and namespace
![Create new device handler Screen Shot][create-new-device]
>This code was based on [SmartThing-Alexa by bjpierron](https://github.com/bjpierron/SmartThings-Alexa/blob/master/devicetypes/bjpierron/simulated-alexa-button.src/simulated-alexa-button.groovy)

6. In the menu go to My Locations and the click on New Location
![Create new location Screen Shot][new-location]

7. In the menu go to My Devices and the click on New Device. On name and Device network Id you can write whatever you want, on type you should look for the Device Handler we created on step 5 (Usually at the end of the list) and in location select the location you just created
![Create device][create-device]

8. Go to your Alexa app and search for the SmartThings skill
![Search SmarThings Skill Screen Shot][search-skill-screenshot]

9. After you activate the skill, it will prompt a window were you need to login with your Samsung SmartThings account
![Login Samsung SmartThings Screen Shot][login-samsung-screenshot]

10. Authorize Amazon Alexa to access your devices in your SmartThings account
![Authorize Alexa Screen Shot][allow-alexa-screenshot]

11. A success message should appear
![Link Accounts Message Screen Shot][link-accounts-screenshot]

12. When closing the success message, it will ask you to start detecting your virtual devices
![Scan devices Screen Shot][scan-devices-screenshot]

13. Wait until the scan ends
![Searching Devices Screen Shot][searching-devices-screenshot]

14. It will find the new device you just created on SmartThings. You can now close your alexa app
![Device Found Screen Shot][device-found-screenshot]

15. Login into IFTTT and click on [create](https://ifttt.com/create)
![Create Screen Shot][create-screenshot]

16. In the If part search for webhook
![Webhook Screen Shot][webhook-screenshot]

17. Select the Receive a web request service
![Web Request Screen Shot][web-request-screenshot]

18. Connect
![Connect Webhook Screen Shot][connect-webhook-screenshot]

19. Name the event as plug_on and create the trigger
![Name event][event-name]

20. In the Then That part search for SmartThings
![SmartThings Applet Screen Shot][smart-things-screenshot]

21. Select switch on action
![Switch On Action Screen Shot][switch-on-screenshot]

22. Click on connect and login with your Samsung SmartThings account to allow access
![Login in SmarThings with IFTTT Screen Shot][ifttt-samsung-login-screenshot]

23. Select the location and devices you want to add. You only need to select the Switch we create
![Set Permissions Screen Shot][allow-switch-screenshot]

24. Click on create action
![Create Switch Action Screen Shot][create-switch-action-screenshot]

25. Click on continue in your recipe
![Confirm IFTTT Screen Shot][confirm-ifttt-screenshot]

26. Optionally you can turn on the Receive notifications button and click on finish
![Confirm IFTTT Screen Shot][finish-ifttt-screenshot]
>For getting notifications you need to download the app on your cellphone and login with your IFTTT account

27. Repeat steps 16 to 27 for the plug_off event (In the if part the event name should be named something like plug_off and in the Then That part you should select the switch off action)

28. Go back to your Alexa app and configure your Smart Plug with your Amazon Account. You can found the official instructions for doing that [here](https://www.amazon.com/gp/help/customer/display.html?nodeId=GJL9P9S22S2HBUDF)

29. Then go to routines and create a new one. On the when part you will select smart house
![Alexa When Screen Shot][alexa-when-screenshot]

30. Select your virtual device that you created in Samsung SmartThings
![Alexa When Device Screen Shot][alexa-when-device-screenshot]

31. Select the state that you want to trigger your routine, in this case the trigger will be when the plug is open
![Alexa When Device Status Screen Shot][alexa-when-device-status-screenshot]

32. The action will be also in smart house
![Alexa Then Screen Shot][alexa-then-screenshot]

33. And then select the Smart plug that you set previously in the step 28 Change the status to on
![Alexa Then Status Screen Shot][alexa-then-status-screenshot]

34. Save this routine and repeat steps 29 to 32 now for turning off the smart plug

35. Go to the folder where you clone the repository and create a .env file with the .env.example template

36. Go back to IFTTT, explore and look for the webhook service
![Webhook Service Screen Shot][explore-webhook-screenshot]

37. Click on the documentation button that is at the right top
![Webhook Documentation Button Screen Shot][documentation-webhook-screenshot]

38. You will find the key at the top of the window
![Webhook Key Screen Shot][webhook-key-screenshot]

39. Copy and paste your key in the .env file

41. Now in your console create a new cronjob for running the script every 5 minutes
```sh
crontab -e
```

```
*/5 * * * * /path/to/file/main.py
```

>If you are using MacOS be sure that cron and your terminal has permissions to execute the file


<!-- USAGE EXAMPLES -->
## Usage

You can modify the frequency the python script will be executed by changing the cronjob. Also for change the range whereas the plug should turn or on off, you just need to edit the lines 24 and 28 in the main.py file

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Diezaztek/Smart-plug](https://github.com/Diezaztek/Smart-plug)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[create-screenshot]: images/create.png
[webhook-screenshot]: images/webhook.png
[web-request-screenshot]: images/web-request.png
[connect-webhook-screenshot]: images/connect-webhook.png
[event-name]: images/event-name.png
[create-new-device]: images/create-new-device.png
[new-location]: images/new-location.png
[create-device]: images/create-device.png
[search-skill-screenshot]: images/search-skill.jpg
[login-samsung-screenshot]: images/login-samsung.jpg
[allow-alexa-screenshot]: images/allow-alexa.jpg
[link-accounts-screenshot]: images/link-accounts.jpg
[scan-devices-screenshot]: images/scan-devices.jpg
[searching-devices-screenshot]: images/searching-devices.jpg
[device-found-screenshot]: images/device-found.jpg
[smart-things-screenshot]: images/smartthings-applet.png
[switch-on-screenshot]: images/switch-on-action.png
[ifttt-samsung-login-screenshot]: images/ifttt-samsung-login.png
[allow-switch-screenshot]: images/allow-switch.png
[create-switch-action-screenshot]: images/create-action-switch.png
[confirm-ifttt-screenshot]: images/confirm-ifttt.png
[finish-ifttt-screenshot]: images/finish-ifttt.png
[alexa-when-screenshot]: images/alexa-when.jpg
[alexa-when-device-screenshot]: images/alexa-when-device.jpg
[alexa-when-device-status-screenshot]: images/alexa-when-device-status.jpg
[alexa-then-screenshot]: images/alexa-then.jpg
[alexa-then-status-screenshot]: images/alexa-then-status.jpg
[explore-webhook-screenshot]: images/explore-webhook.png
[documentation-webhook-screenshot]: images/documentation-webhook.png
[webhook-key-screenshot]: images/webhook-key.png
