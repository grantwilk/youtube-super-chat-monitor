# YouTube Super Chat Monitor

The YouTube Super Chat Monitor (YTSCM) is a simplified API for live Super
Chat monitoring on YouTube. It enables you to easily poll the YouTube API for
new Super Chats and execute a custom function upon receipt of one.

To learn more about YTSCM, see the sections below.

## Setup / Tutorial

#### Step 1: Create an OAuth 2.0 Client ID
This library does not come packaged with an API key or OAuth Client ID, so
you will need to create your own. To create an OAuth Client ID, 
 
1. Create or select a project in the [Google API Console](https://console.developers.google.com/).
2. In the [library panel](https://console.developers.google.com/apis/library), 
search for the YouTube Data API v3. Click into the listing for that API
and make sure the API is enabled for your project.
3. In the [credentials panel](https://console.developers.google.com/apis/credentials),
create an OAuth 2.0 Client ID. Set the application type to **Other**.
4. You may also be required to make an OAuth consent screen.
5. Once the OAuth 2.0 Client ID has been created, return to the
[credentials panel](https://console.developers.google.com/apis/credentials) and 
download the JSON file that contains your credentials. It should have a name
like `client_secret_CLIENTID.json`, where `CLIENTID` is the client ID for your
project.

#### Step 2: Install YTSCM from PyPI
YTSCM is readily available on PyPI and can be installed with pip. Simple open
a command line and enter the following command.

`python -m pip install --upgrade ytscm`

Once installed, YTSCM is ready to be imported into your projects.

#### Step 3: Run Through an Example Program
Before you go running off on your own, lets walk through an example use-case 
so you have a better understanding of how YTSCM works.

Start by retyping or copying and pasting the script below into a local python
file.

```python
from ytscm import YTSCMonitor


def main():
    
    # create a new super chat monitor
    monitor = YTSCMonitor("YOUR_CLIENT_SECRET.json", update_function)

    # start monitoring super chats (update every 5 seconds)
    monitor.start(interval=5)

    # stop monitoring super chats
    # monitor.stop()


def update_function(super_chat_event):
    """
    This function gets called when our monitor detects a new Super Chat!
    Prints out the name and amount of the supporter's Super Chat. 
    :param super_chat_event - the new Super Chat event
    """

    # get an object containing information about the supporter
    supporter_details = super_chat_event.get_supporter_details()

    # get the supporter's channel name
    display_name = supporter_details.get_display_name()

    # get the amount of money our supporter donated as a string
    amount_string = super_chat_event.get_display_string()

    # print the name and amount that our supported donated
    print("{0} sent a {1} Super Chat!".format(display_name, amount_string))


if __name__ == '__main__':
    main()
```

Next, run the code. This can be done from within your IDE or from the
command line with the command `python YOUR_FILE.py`.

Upon running the file, you should be presented with the following message.

```
Please visit this URL to authorize this application: << CRAZY LONG URL >>
Enter the authorization code:
```

We need to give our test program permission to access our YouTube account via
the OAuth Client ID we created. 

Copy and paste the URL into your web browser, select the Google/Brand account
that you want to poll for updates and give the OAuth Client ID permission to
use your YouTube account data.

Copy the authorization code and paste it back into the console. Hit enter, 
and the monitor should start polling.

```
Please visit this URL to authorize this application: << CRAZY LONG URL >>
Enter the authorization code: << YOUR AUTHORIZATION CODE >>
Started monitoring Super Chats!
```

The monitor is now polling for new Super Chats every `interval = 5` 
seconds. Any Super Chats received while polling will trigger the
`update_function()` function, and will print the supporter's name and donation
amount to the console.

```
Obi-Wan Kenobi sent a $5.00 Super Chat!
C-3PO sent a $1.00 Super Chat!
Chewbacca sent a $10.00 Super Chat!
Darth Maul sent a $2.00 Super Chat!
```

Now, you can take this code and create something amazing with it!

## Class Structure Documentation

All YTSCM classes are derived from the JSON structure that Google specifies
on their [SuperChatEvents](https://developers.google.com/youtube/v3/live/docs/superChatEvents)
page. More specific information about class structure and attributes can be
found there.

#### YTSCMonitor
Monitors YouTube Super Chat events and triggers an update function if a new 
Super Chat is received.

| Method                                            | Description                                                          |
|---------------------------------------------------|----------------------------------------------------------------------|
| YTSCMonitor(client_secrets_file, update_function) | Creates a new YTSCMonitor.                                           |
| fetch()                                           | Manually fetches new Super Chats from YouTube one time.              |
| start(interval)                                   | Begins automatically fetching new Super Chats at a regular interval. |
| stop()                                            | Stops automatically fetching new Super Chats.                        |

#### YTSCEvent
Contains YouTube Super Chat event attributes. All attributes are read-only.

| Attribute         | Type                 | Getter Method           | Description                                                            |
|-------------------|----------------------|-------------------------|------------------------------------------------------------------------|
| id                | string               | get_id()                | An ID string unique to the Super Chat event.                           |
| channel_id        | string               | get_channel_id()        | The channel ID of the creator hosting the live event.                  |
| supporter_details | YTSCSupporterDetails | get_supporter_details() | Details about the supporter's channel.                                 |
| comment_text      | string               | get_comment_text()      | The text content of the supporter's comment.                           |
| created_at        | datetime (ISO 8601)  | get_created_at()        | The date and time when the Super Chat was sent.                        |
| amount_micros     | unsigned long        | get_amount_micros()     | The Super Chat amount, in micros of the purchase currency.             |
| currency          | string (ISO 4217)    | get_currency()          | The currency in which the Super Chat purchase was made.                |
| display_string    | string               | get_display_string()    | A string, like $1.00, that shows the amount and currency.              |
| message_type      | unsigned integer     | get_message_type()      | The tier for the paid message.                                         |

#### YTSCSupporterDetails
Contains YouTube Super Chat supporter details. All attributes are read-only.

| Attribute         | Type   | Getter Method           | Description                                  |
|-------------------|--------|-------------------------|----------------------------------------------|
| channel_id        | string | get_channel_id()        | The supporter's YouTube channel ID.          |
| channel_url       | string | get_channel_url()       | The URL of the supporter's channel.          |
| display_name      | string | get_display_name()      | The display name of the supporter's channel. |
| profile_image_url | string | get_profile_image_url() | The avatar URL for the supporter's channel.  |

## More Information
If you have any questions or concerns regarding this package, feel free to
reach out to me via email (available in my profile). Other than that, 
hopefully you find some awesome ways to apply this to help promote super
chats on your live streams!